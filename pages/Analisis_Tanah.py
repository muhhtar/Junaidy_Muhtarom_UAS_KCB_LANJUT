import streamlit as st
import plotly.graph_objects as go
import os

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Analisis Tanah",
    page_icon="🧪",
    layout="wide"
)

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
# HEADER
# =====================================================

st.markdown("""

<div class="hero">

<h1>

Analisis Kondisi Tanah

</h1>

<h2>

Artificial Intelligence Soil Analysis

</h2>

<p>

Analisis kondisi unsur hara tanah untuk
membantu mengetahui kualitas lahan
sebelum proses penanaman.

</p>

</div>

""", unsafe_allow_html=True)

st.write("")

# =====================================================
# INPUT
# =====================================================

st.subheader("Masukkan Nilai Unsur Hara")

c1, c2, c3 = st.columns(3)

with c1:

    N = st.slider(
        "Nitrogen (N)",
        0,
        150,
        90
    )

with c2:

    P = st.slider(
        "Fosfor (P)",
        0,
        150,
        42
    )

with c3:

    K = st.slider(
        "Kalium (K)",
        0,
        210,
        43
    )

st.write("")

analisis = st.button(
    "Analisis Tanah",
    use_container_width=True
)

# =====================================================
# ANALISIS
# =====================================================

if analisis:

    with st.spinner("Sedang menganalisis kondisi tanah..."):

        pass

    st.success("Analisis selesai.")

    st.divider()

    # =====================================================
    # STATUS UNSUR HARA
    # =====================================================

    def status_nilai(nilai, rendah, sedang):

        if nilai < rendah:
            return "Rendah", "🔴"

        elif nilai < sedang:
            return "Sedang", "🟡"

        return "Tinggi", "🟢"

    statusN, iconN = status_nilai(N,50,100)
    statusP, iconP = status_nilai(P,30,60)
    statusK, iconK = status_nilai(K,30,60)

    s1, s2, s3 = st.columns(3)

    with s1:

        st.metric(
            "Nitrogen",
            f"{N}",
            statusN
        )

        st.write(iconN, statusN)

    with s2:

        st.metric(
            "Fosfor",
            f"{P}",
            statusP
        )

        st.write(iconP, statusP)

    with s3:

        st.metric(
            "Kalium",
            f"{K}",
            statusK
        )

        st.write(iconK, statusK)

    st.divider()

    # =====================================================
    # RADAR CHART
    # =====================================================

    st.subheader("Visualisasi Unsur Hara")

    radar = go.Figure()

    radar.add_trace(

        go.Scatterpolar(

            r=[N,P,K],

            theta=[
                "Nitrogen",
                "Fosfor",
                "Kalium"
            ],

            fill="toself",

            name="Tanah"

        )

    )

    radar.update_layout(

        polar=dict(

            radialaxis=dict(
                visible=True
            )

        ),

        showlegend=False

    )

    st.plotly_chart(
        radar,
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # REKOMENDASI PEMUPUKAN
    # =====================================================

    st.subheader("Rekomendasi")

    rekomendasi=[]

    if N < 50:

        rekomendasi.append(
            "Tambahkan pupuk kaya Nitrogen."
        )

    if P < 30:

        rekomendasi.append(
            "Tambahkan pupuk Fosfat."
        )

    if K < 30:

        rekomendasi.append(
            "Tambahkan pupuk Kalium."
        )

    if len(rekomendasi)==0:

        rekomendasi.append(
            "Kondisi tanah sudah cukup baik untuk proses budidaya."
        )

    for r in rekomendasi:

        st.success(r)

    st.divider()

    # =====================================================
    # AI INSIGHT
    # =====================================================

    st.subheader(
        "Insight Artificial Intelligence"
    )

    insight=f"""

Berdasarkan analisis unsur hara,
kondisi tanah menunjukkan:

• Nitrogen : {statusN}

• Fosfor : {statusP}

• Kalium : {statusK}

Data ini dapat digunakan sebagai
referensi sebelum melakukan
rekomendasi tanaman.

"""

    st.info(insight)

    st.divider()

    # =====================================================
    # SKOR KESEHATAN TANAH
    # =====================================================

    skor=((N/150)+(P/150)+(K/210))/3*100

    st.subheader("Skor Kesehatan Tanah")

    st.progress(skor/100)

    st.metric(
        "Soil Health Score",
        f"{skor:.1f}%"
    )

    st.divider()

    # =====================================================
    # KESIMPULAN
    # =====================================================

    if skor>=80:

        st.success(
            "Kondisi tanah sangat baik dan siap digunakan untuk budidaya."
        )

    elif skor>=60:

        st.warning(
            "Kondisi tanah cukup baik namun masih memerlukan perbaikan."
        )

    else:

        st.error(
            "Kondisi tanah kurang baik. Disarankan melakukan pemupukan terlebih dahulu."
        )