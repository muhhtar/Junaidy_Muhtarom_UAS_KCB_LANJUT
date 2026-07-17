import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Smart Farming Assistant",
    page_icon="assets/sfa_logo.png",
    layout="wide"
)

# ==========================
# CSS MODERN AGRITECH
# ==========================

st.markdown("""
<style>

/* Background */
.stApp{
    background-color:#F8FAF8;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#1E5631;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Judul */
h1,h2,h3{
    color:#1F2937 !important;
}

/* Metric */
[data-testid="metric-container"]{
    background:white;
    border:1px solid #E5E7EB;
    padding:20px;
    border-radius:18px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

/* Hero Banner */
.hero{
    background:linear-gradient(
        135deg,
        #2E7D32,
        #66BB6A
    );

    padding:40px;
    border-radius:25px;
    color:white;
}

/* Feature Card */
.feature{
    background:white;
    padding:25px;
    border-radius:18px;
    border-top:6px solid #4CAF50;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    min-height:230px;
}

/* Info Card */
.info{
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

/* Footer */
.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

/* Tombol */
.stButton button{
    background:#2E7D32 !important;
    color:white !important;
    border:none !important;
    border-radius:10px !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# DATA DASHBOARD
# ==========================

if os.path.exists("history.csv"):
    df = pd.read_csv("history.csv")
    total_prediksi = len(df)
else:
    total_prediksi = 0

# ==========================
# HEADER
# ==========================

col_logo, col_text = st.columns([1,4])

with col_logo:
    st.image(
        "assets/sfa_logo.png",
        width=130
    )

with col_text:

    st.markdown("""
    <div class="hero">

    <h1 style="color:white;">
    Smart Farming Assistant
    </h1>

    <p style="font-size:20px;">
    Sistem Rekomendasi Tanaman Berbasis Kecerdasan Buatan
    </p>

    <p>
    Membantu petani menentukan tanaman yang paling sesuai
    berdasarkan kondisi tanah dan lingkungan.
    </p>

    </div>
    """, unsafe_allow_html=True)

st.write("")

# ==========================
# METRIC
# ==========================

m1,m2,m3,m4 = st.columns(4)

with m1:
    st.metric(
        "Total Prediksi",
        total_prediksi
    )

with m2:
    st.metric(
        "Jumlah Tanaman",
        "22"
    )

with m3:
    st.metric(
        "Parameter Input",
        "7"
    )

with m4:
    st.metric(
        "Algoritma",
        "XGBoost"
    )

st.write("")
st.write("")

# ==========================
# FITUR SISTEM
# ==========================

st.subheader("Fitur Sistem")

c1,c2 = st.columns(2)

with c1:

    st.markdown("""
    <div class="feature">

    <h3>Rekomendasi Tanaman</h3>

    Sistem menganalisis kandungan unsur hara tanah,
    suhu, kelembapan, pH, dan curah hujan untuk
    menentukan tanaman yang paling sesuai.

    <br><br>

    Output:
    <ul>
    <li>Tanaman yang direkomendasikan</li>
    <li>Tingkat keyakinan model</li>
    <li>Riwayat prediksi</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="feature">

    <h3>Analisis Tanah</h3>

    Membantu pengguna memahami kondisi tanah
    berdasarkan kandungan Nitrogen, Phosphorus,
    dan Potassium.

    <br><br>

    Output:
    <ul>
    <li>Status unsur hara</li>
    <li>Kondisi tanah</li>
    <li>Rekomendasi penggunaan</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

st.write("")

c3,c4 = st.columns(2)

with c3:

    st.markdown("""
    <div class="feature">

    <h3>Riwayat Prediksi</h3>

    Menyimpan seluruh aktivitas rekomendasi
    yang pernah dilakukan pengguna.

    <br><br>

    Output:
    <ul>
    <li>Tanggal prediksi</li>
    <li>Nama tanaman</li>
    <li>Tingkat keyakinan</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

with c4:

    st.markdown("""
    <div class="feature">

    <h3>Laporan Hasil</h3>

    Menyediakan dokumentasi hasil prediksi
    yang dapat digunakan sebagai referensi
    pengambilan keputusan.

    <br><br>

    Output:
    <ul>
    <li>Data input</li>
    <li>Hasil rekomendasi</li>
    <li>Ringkasan analisis</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================
# INFORMASI PROYEK
# ==========================

left,right = st.columns([2,1])

with left:

    st.markdown("""
    <div class="info">

    <h2>Tentang Proyek</h2>

    Smart Farming Assistant merupakan aplikasi
    berbasis Machine Learning yang memanfaatkan
    algoritma XGBoost untuk memberikan rekomendasi
    tanaman berdasarkan kondisi tanah dan lingkungan.

    Aplikasi ini dikembangkan sebagai proyek
    Kecerdasan Buatan Lanjut untuk membantu
    proses pengambilan keputusan di bidang pertanian.

    </div>
    """, unsafe_allow_html=True)

with right:

    st.markdown("""
    <div class="info">

    <h3>Informasi Dataset</h3>

    <b>Dataset</b><br>
    Crop Recommendation Dataset

    <br><br>

    <b>Jumlah Data</b><br>
    2200 Data

    <br><br>

    <b>Jumlah Kelas</b><br>
    22 Tanaman

    <br><br>

    <b>Model</b><br>
    XGBoost Classifier

    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">

<hr>

Smart Farming Assistant v2.0

<br>

Proyek Kecerdasan Buatan Lanjut

</div>
""", unsafe_allow_html=True)