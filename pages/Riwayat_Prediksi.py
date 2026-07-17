import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(
    page_title="Riwayat Prediksi",
    page_icon="📋",
    layout="wide"
)

# ==========================
# LOAD CSS
# ==========================

if os.path.exists("styles.css"):

    with open("styles.css", encoding="utf-8") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================
# HEADER
# ==========================

st.markdown("""
<div class="hero">

<h1>Riwayat Prediksi</h1>

<h2>Smart Farming Assistant</h2>

<p>

Halaman ini menampilkan seluruh riwayat
prediksi yang pernah dilakukan menggunakan
model Random Forest Classifier.

</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================
# CEK FILE
# ==========================

if not os.path.exists("history.csv"):

    st.warning("Belum ada riwayat prediksi.")

    st.stop()

df = pd.read_csv("history.csv")

# ==========================
# FILTER
# ==========================

st.subheader("Filter Data")

c1, c2 = st.columns(2)

with c1:

    keyword = st.text_input(
        "Cari Nama Tanaman"
    )

with c2:

    if "Tanggal" in df.columns:

        tanggal = st.selectbox(

            "Pilih Tanggal",

            ["Semua"] +
            sorted(
                df["Tanggal"].astype(str).unique()
            )

        )

    else:

        tanggal = "Semua"

# ==========================
# FILTER DATA
# ==========================

hasil = df.copy()

if keyword:

    hasil = hasil[
        hasil["Tanaman"]
        .str.contains(
            keyword,
            case=False
        )
    ]

if tanggal != "Semua":

    hasil = hasil[
        hasil["Tanggal"] == tanggal
    ]

st.write("")

# ==========================
# STATISTIK
# ==========================

m1, m2, m3 = st.columns(3)

with m1:

    st.metric(
        "Total Prediksi",
        len(hasil)
    )

with m2:

    if len(hasil):

        st.metric(
            "Tanaman Berbeda",
            hasil["Tanaman"].nunique()
        )

with m3:

    if len(hasil):

        st.metric(
            "Confidence Rata-rata",
            f"{hasil['Confidence'].mean():.2f}%"
        )

st.write("")

# ==========================
# TABEL
# ==========================

st.subheader("Data Riwayat")

st.dataframe(

    hasil,

    use_container_width=True,

    hide_index=True

)

# ==========================
# GRAFIK
# ==========================

if len(hasil):

    st.subheader(
        "Frekuensi Rekomendasi Tanaman"
    )

    grafik = (

        hasil["Tanaman"]

        .value_counts()

        .reset_index()

    )

    grafik.columns = [

        "Tanaman",

        "Jumlah"

    ]

    fig = px.bar(

        grafik,

        x="Tanaman",

        y="Jumlah",

        color="Jumlah",

        text="Jumlah"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

# ==========================
# DOWNLOAD
# ==========================

st.subheader("Ekspor Data")

csv = hasil.to_csv(index=False)

st.download_button(

    "Unduh CSV",

    csv,

    file_name="riwayat_prediksi.csv",

    mime="text/csv",

    use_container_width=True

)

# ==========================
# HAPUS RIWAYAT
# ==========================

st.subheader("Manajemen Data")

if st.button(

    "Hapus Seluruh Riwayat",

    use_container_width=True

):

    os.remove("history.csv")

    st.success(

        "Riwayat berhasil dihapus."

    )

    st.rerun()