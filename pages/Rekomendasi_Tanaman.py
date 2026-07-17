import os
from datetime import datetime
import joblib
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Rekomendasi Tanaman",
    page_icon="🌱",
    layout="wide"
)

# =====================================================
# LOAD MODEL
# =====================================================
model = joblib.load("crop_model.pkl")
encoder = joblib.load("label_encoder.pkl")

# =====================================================
# LOAD CSS
# =====================================================
if os.path.exists("styles.css"):
    with open("styles.css", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================================
# NAMA TANAMAN
# =====================================================
nama_tanaman = {
    "rice": "Padi",
    "maize": "Jagung",
    "banana": "Pisang",
    "coffee": "Kopi",
    "cotton": "Kapas",
    "mango": "Mangga",
    "orange": "Jeruk",
    "papaya": "Pepaya",
    "watermelon": "Semangka",
    "coconut": "Kelapa",
    "grapes": "Anggur",
    "apple": "Apel",
    "lentil": "Lentil",
    "kidneybeans": "Kacang Merah",
    "blackgram": "Kacang Hitam",
    "mungbean": "Kacang Hijau",
    "chickpea": "Kacang Arab",
    "pigeonpeas": "Kacang Gude",
    "mothbeans": "Kacang Moth",
    "muskmelon": "Melon",
    "pomegranate": "Delima",
    "jute": "Jute"
}

# =====================================================
# HEADER
# =====================================================
st.markdown("""
<div class="hero">
    <h1>Rekomendasi Tanaman</h1>
    <h2>Artificial Intelligence Recommendation</h2>
    <p>
        Masukkan parameter tanah dan lingkungan untuk memperoleh rekomendasi tanaman 
        menggunakan algoritma <b>Random Forest Classifier</b>.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# =====================================================
# INPUT
# =====================================================
st.subheader("Parameter Tanah")
left, right = st.columns(2)

with left:
    N = st.slider("Nitrogen (N)", 0.0, 150.0, 90.0)
    P = st.slider("Fosfor (P)", 0.0, 150.0, 42.0)
    K = st.slider("Kalium (K)", 0.0, 210.0, 43.0)
    temperature = st.slider("Suhu", 0.0, 50.0, 20.8)

with right:
    humidity = st.slider("Kelembapan", 0.0, 100.0, 82.0)
    ph = st.slider("pH Tanah", 0.0, 14.0, 6.5)
    rainfall = st.slider("Curah Hujan", 0.0, 350.0, 202.0)

st.write("")

prediksi = st.button(
    "Analisis Tanaman",
    use_container_width=True
)

# =====================================================
# PREDIKSI & HASIL
# =====================================================
if prediksi:
    with st.spinner("Sedang menganalisis kondisi lahan..."):
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        
        prediction = model.predict(data)
        probabilities = model.predict_proba(data)
        
        crop_asli = encoder.inverse_transform(prediction)[0]
        crop = nama_tanaman.get(crop_asli, crop_asli)
        confidence = float(np.max(probabilities) * 100)

    st.success("Analisis berhasil dilakukan")
    st.write("")

    # Hasil Prediksi
    st.markdown(f"""
    <div class="result-card">
        <h2 style="margin-bottom:10px;">Hasil Rekomendasi</h2>
        <h1 style="color:#16A34A; font-size:48px; margin-bottom:5px;">{crop}</h1>
        <p>Tanaman dengan tingkat kecocokan paling tinggi berdasarkan kondisi lahan.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Confidence Score
    st.subheader("Tingkat Keyakinan Model")
    st.progress(confidence / 100)
    st.metric("Confidence Score", f"{confidence:.2f}%")
    st.write("")

    # Gauge Chart
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=confidence,
            number={"suffix": "%"},
            title={"text": "Confidence"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "green"},
                "steps": [
                    {"range": [0, 50], "color": "#FCA5A5"},
                    {"range": [50, 80], "color": "#FDE68A"},
                    {"range": [80, 100], "color": "#86EFAC"}
                ]
            }
        )
    )
    st.plotly_chart(fig, use_container_width=True)
    st.divider()

    # Top 3 Rekomendasi
    st.subheader("Tiga Rekomendasi Terbaik")
    top_index = np.argsort(probabilities[0])[::-1][:3]
    top_crop = encoder.inverse_transform(top_index)
    top_score = probabilities[0][top_index] * 100

    hasil = pd.DataFrame({
        "Tanaman": [nama_tanaman.get(i, i) for i in top_crop],
        "Probabilitas (%)": np.round(top_score, 2)
    })

    st.dataframe(hasil, use_container_width=True, hide_index=True)
    st.bar_chart(hasil.set_index("Tanaman"))
    st.divider()

    # Radar Chart
    st.subheader("Visualisasi Parameter Lahan")
    kategori = ["Nitrogen", "Fosfor", "Kalium", "Suhu", "Kelembapan", "pH", "Curah Hujan"]
    nilai = [N, P, K, temperature, humidity, ph, rainfall]

    radar = go.Figure()
    radar.add_trace(
        go.Scatterpolar(
            r=nilai,
            theta=kategori,
            fill="toself",
            name="Parameter"
        )
    )
    radar.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        showlegend=False
    )
    st.plotly_chart(radar, use_container_width=True)
    st.divider()

    # Analisis Kondisi Tanah
    st.subheader("Analisis Kondisi Tanah")
    kondisi = []

    if N >= 80:
        kondisi.append("Nitrogen berada pada kategori baik.")
    else:
        kondisi.append("Nitrogen masih rendah.")

    if P >= 40:
        kondisi.append("Fosfor mencukupi.")
    else:
        kondisi.append("Fosfor perlu ditingkatkan.")

    if K >= 40:
        kondisi.append("Kalium berada pada kondisi baik.")
    else:
        kondisi.append("Kalium masih rendah.")

    if 5.5 <= ph <= 7:
        kondisi.append("pH tanah berada pada kisaran ideal.")
    else:
        kondisi.append("pH tanah kurang ideal.")

    # Memperbaiki pembukaan tag HTML bertahap agar tidak merusak struktur Streamlit
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    for item in kondisi:
        st.write(f"• {item}")
    st.markdown("</div>", unsafe_allow_html=True)
    st.divider()

    # AI Insight
    st.subheader("Insight Artificial Intelligence")
    insight = f"""
    Model Random Forest Classifier merekomendasikan tanaman **{crop}** dengan tingkat keyakinan **{confidence:.2f}%**.
    
    Keputusan ini diperoleh dari hasil analisis terhadap kandungan Nitrogen, Fosfor, Kalium, Suhu, Kelembapan, pH Tanah, dan Curah Hujan.
    
    Semakin tinggi nilai keyakinan, semakin besar kecocokan tanaman terhadap kondisi lahan.
    """
    st.info(insight)
    st.divider()

    # Simpan Riwayat
    history = pd.DataFrame([{

    "Tanggal": datetime.now().strftime("%d-%m-%Y"),

    "Jam": datetime.now().strftime("%H:%M:%S"),

    "Nitrogen": N,

    "Fosfor": P,

    "Kalium": K,

    "Suhu": temperature,

    "Kelembapan": humidity,

    "pH": ph,

    "Curah Hujan": rainfall,

    "Tanaman": crop,

    "Confidence": round(confidence,2),

    "Top 1": nama_tanaman.get(top_crop[0], top_crop[0]),

    "Top 2": nama_tanaman.get(top_crop[1], top_crop[1]),

    "Top 3": nama_tanaman.get(top_crop[2], top_crop[2])

}])
    if os.path.exists("history.csv"):
        history.to_csv("history.csv", mode="a", header=False, index=False)
    else:
        history.to_csv("history.csv", index=False)

    st.success("Hasil berhasil disimpan ke Riwayat Prediksi.")
    st.divider()

    # Download Laporan
    laporan = f"""
==========================================
LAPORAN REKOMENDASI TANAMAN
==========================================

Tanggal : {datetime.now().strftime("%d-%m-%Y")}
Jam     : {datetime.now().strftime("%H:%M")}

Tanaman Direkomendasikan : {crop}
Confidence : {confidence:.2f} %

------------------------------------------

Nitrogen     : {N}
Fosfor       : {P}
Kalium       : {K}
Suhu         : {temperature}
Kelembapan   : {humidity}
pH Tanah     : {ph}
Curah Hujan  : {rainfall}

==========================================
Model : Random Forest Classifier
Smart Farming Assistant
"""

    st.download_button(
        "Unduh Laporan",
        laporan,
        file_name="laporan_rekomendasi_tanaman.txt",
        mime="text/plain",
        use_container_width=True
    )