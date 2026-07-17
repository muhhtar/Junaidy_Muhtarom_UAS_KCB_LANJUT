import streamlit as st
import os

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Tentang Sistem",
    page_icon="ℹ️",
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

Tentang Sistem

</h1>

<h2>

Smart Farming Assistant

</h2>

<p>

Platform Artificial Intelligence untuk
membantu menentukan tanaman yang paling sesuai
berdasarkan kondisi tanah dan lingkungan.

</p>

</div>

""", unsafe_allow_html=True)

st.write("")

# =====================================================
# OVERVIEW
# =====================================================

st.subheader("Deskripsi Sistem")

st.markdown("""

<div class="info">

Smart Farming Assistant merupakan aplikasi
berbasis Machine Learning yang dirancang
untuk membantu petani menentukan tanaman
yang paling sesuai berdasarkan kondisi lahan.

Sistem memanfaatkan algoritma
<b>Random Forest Classifier</b>
yang telah dilatih menggunakan
Crop Recommendation Dataset.

</div>

""", unsafe_allow_html=True)

st.write("")

# =====================================================
# INFORMASI
# =====================================================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("Model AI","Random Forest")

with c2:
    st.metric("Dataset","2200")

with c3:
    st.metric("Tanaman","22")

with c4:
    st.metric("Parameter","7")

st.divider()

# =====================================================
# PARAMETER
# =====================================================

st.subheader("Parameter yang Dianalisis")

p1,p2,p3 = st.columns(3)

with p1:

    st.success("Nitrogen (N)")
    st.success("Fosfor (P)")
    st.success("Kalium (K)")

with p2:

    st.info("Suhu")
    st.info("Kelembapan")
    st.info("pH Tanah")

with p3:

    st.warning("Curah Hujan")

st.divider()

# =====================================================
# ALUR SISTEM
# =====================================================

st.subheader("Alur Kerja Sistem")

st.markdown("""

1. Pengguna memasukkan parameter tanah.

2. Data diproses oleh model Random Forest.

3. Sistem menghitung probabilitas setiap tanaman.

4. Sistem memilih tanaman dengan probabilitas tertinggi.

5. Hasil prediksi disimpan ke Riwayat.

""")

st.divider()

# =====================================================
# TEKNOLOGI
# =====================================================

st.subheader("Teknologi yang Digunakan")

tech1,tech2=st.columns(2)

with tech1:

    st.markdown("""

- Python

- Streamlit

- Scikit-learn

- Pandas

- NumPy

""")

with tech2:

    st.markdown("""

- Plotly

- Joblib

- Random Forest Classifier

- Machine Learning

""")

st.divider()

# =====================================================
# KEUNGGULAN
# =====================================================

st.subheader("Keunggulan Sistem")

st.success("Prediksi cepat.")

st.success("Akurasi tinggi.")

st.success("Antarmuka sederhana.")

st.success("Mudah digunakan.")

st.success("Menyimpan riwayat prediksi.")

st.success("Visualisasi hasil analisis.")

st.divider()

# =====================================================
# PENGEMBANG
# =====================================================

st.subheader("Informasi Pengembang")

st.markdown("""

Nama Aplikasi :

**Smart Farming Assistant**

Versi :

**3.0**

Model :

**Random Forest Classifier**

Framework :

**Streamlit**

Bahasa :

**Python**

""")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.markdown("""

<div class="footer">

<b>Smart Farming Assistant v3.0</b>

<br>

Artificial Intelligence Based Crop Recommendation System

<br><br>

© 2026

</div>

""", unsafe_allow_html=True)