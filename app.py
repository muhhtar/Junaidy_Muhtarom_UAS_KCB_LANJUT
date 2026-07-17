import os
from datetime import datetime
import pandas as pd
import streamlit as st
from auth import login, sidebar_user
# =====================================================
# KONFIGURASI HALAMAN
# =====================================================
st.set_page_config(
    page_title="Smart Farming Assistant",
    page_icon="assets/sfa_logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# LOAD CSS
# =====================================================
def load_css():
    if os.path.exists("styles.css"):
        with open("styles.css", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()
# =====================================================
# LOGIN SYSTEM
# =====================================================

if not st.session_state.logged_in:
    login()
    st.stop()

sidebar_user()

# =====================================================
# KONSTANTA
# =====================================================

APP_NAME = "Smart Farming Assistant"
MODEL_NAME = "Random Forest Classifier"
DATASET_NAME = "Crop Recommendation Dataset"
AKURASI = "98%"
JUMLAH_DATA = "2200"
JUMLAH_TANAMAN = "22"
JUMLAH_PARAMETER = "7"

# =====================================================
# HISTORY
# =====================================================
if os.path.exists("history.csv"):
    history = pd.read_csv("history.csv")
else:
    history = pd.DataFrame()

total_prediksi = len(history)

# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:
    st.image("assets/sfa_logo.png", width=120)
    st.markdown("## Smart Farming Assistant")
    st.caption("Artificial Intelligence Platform")
    st.divider()
    
    st.success("Model Aktif")
    st.write(MODEL_NAME)
    st.divider()
    
    st.info(f"""
    Dataset :
    {JUMLAH_DATA} Data

    Jumlah Tanaman :
    {JUMLAH_TANAMAN}

    Parameter :
    {JUMLAH_PARAMETER}
    """)

# =====================================================
# HERO
# =====================================================
col1, col2 = st.columns([1, 4])

with col1:
    st.image("assets/sfa_logo.png", width=140)

with col2:
    st.markdown(f"""
    <div class="hero">
        <h1>Smart Farming Assistant</h1>
        <h2>Artificial Intelligence Based Crop Recommendation System</h2>
        <br>
        Menggunakan algoritma <b>{MODEL_NAME}</b> untuk memberikan rekomendasi tanaman 
        berdasarkan kondisi tanah dan lingkungan.
    </div>
    """, unsafe_allow_html=True)

st.write("")

# =====================================================
# DASHBOARD STATISTIK
# =====================================================
st.markdown("## Dashboard")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="card">
        <div class="stat-title">Total Prediksi</div>
        <div class="stat-value">{total_prediksi}</div>
        <div class="stat-sub">Seluruh riwayat prediksi</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
        <div class="stat-title">Dataset</div>
        <div class="stat-value">{JUMLAH_DATA}</div>
        <div class="stat-sub">Crop Recommendation Dataset</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="card">
        <div class="stat-title">Jenis Tanaman</div>
        <div class="stat-value">{JUMLAH_TANAMAN}</div>
        <div class="stat-sub">Kelas Tanaman</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="card">
        <div class="stat-title">Model AI</div>
        <div class="stat-value" style="font-size:22px;">Random Forest</div>
        <div class="stat-sub">Machine Learning</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# =====================================================
# AI INSIGHT
# =====================================================
st.markdown("""
<div class="info-box">
    <h3>Artificial Intelligence Insight</h3>
    <p>
        Smart Farming Assistant memanfaatkan algoritma <b>Random Forest Classifier</b> untuk menganalisis 
        tujuh parameter utama yaitu Nitrogen, Phosphorus, Potassium, Suhu, Kelembapan, pH Tanah, dan Curah Hujan.
    </p>
    <p>
        Model akan menghitung pola dari dataset Crop Recommendation sehingga mampu memberikan 
        rekomendasi tanaman yang paling sesuai berdasarkan kondisi lahan.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# =====================================================
# QUICK MENU
# =====================================================
st.markdown("## Menu Utama")
m1, m2 = st.columns(2)

with m1:
    st.markdown("""
    <div class="feature">
        <h3>Rekomendasi Tanaman</h3>
        <p>Menentukan tanaman terbaik berdasarkan kondisi tanah dan lingkungan menggunakan model Artificial Intelligence.</p>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="feature">
        <h3>Analisis Tanah</h3>
        <p>Melakukan analisis unsur hara tanah untuk membantu memahami kondisi lahan sebelum proses penanaman.</p>
    </div>
    """, unsafe_allow_html=True)

m3, m4 = st.columns(2)

with m3:
    st.markdown("""
    <div class="feature">
        <h3>Riwayat Prediksi</h3>
        <p>Menyimpan seluruh hasil rekomendasi yang pernah dilakukan sehingga dapat digunakan sebagai dokumentasi.</p>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="feature">
        <h3>Tentang Sistem</h3>
        <p>Informasi mengenai dataset, algoritma Random Forest, serta pengembangan aplikasi.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.divider()

# =====================================================
# RINGKASAN DATASET
# =====================================================
st.markdown("## Ringkasan Dataset")
left, right = st.columns([2, 1])

with left:
    st.markdown("""
    <div class="info">
        <h2>Crop Recommendation Dataset</h2>
        <p>Dataset yang digunakan berisi 2.200 data hasil pengamatan kondisi tanah dan lingkungan.</p>
        <p>Setiap data memiliki tujuh parameter utama yang digunakan untuk memprediksi 22 jenis tanaman.</p>
        <p>Model Random Forest mempelajari pola hubungan antar parameter sehingga mampu memberikan rekomendasi tanaman secara otomatis.</p>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="info">
        <h3>Informasi Model</h3>
        <b>Algoritma</b><br>Random Forest Classifier<br><br>
        <b>Dataset</b><br>Crop Recommendation<br><br>
        <b>Jumlah Data</b><br>2200<br><br>
        <b>Jumlah Kelas</b><br>22<br><br>
        <b>Jumlah Parameter</b><br>7
    </div>
    """, unsafe_allow_html=True)

st.write("")

# =====================================================
# PROGRESS MODEL
# =====================================================
st.markdown("## Performa Model")
st.write("Tingkat Akurasi Model")
st.progress(0.98)
st.success("Akurasi Model : 98%")
st.write("")

# =====================================================
# PARAMETER YANG DIGUNAKAN
# =====================================================
st.markdown("## Parameter Analisis")
p1, p2, p3, p4 = st.columns(4)

with p1:
    st.info("Nitrogen (N)")
with p2:
    st.info("Phosphorus (P)")
with p3:
    st.info("Potassium (K)")
with p4:
    st.info("Suhu")

p5, p6, p7 = st.columns(3)

with p5:
    st.info("Kelembapan")
with p6:
    st.info("pH Tanah")
with p7:
    st.info("Curah Hujan")

st.write("")

# =====================================================
# TIPS PERTANIAN
# =====================================================
st.markdown("## Tips Pertanian")
st.markdown("""
<div class="info-box">
    <h3>Rekomendasi</h3>
    <ul>
        <li>Lakukan pengujian pH tanah sebelum menentukan tanaman.</li>
        <li>Pastikan unsur Nitrogen, Phosphorus, dan Potassium berada pada kondisi optimal.</li>
        <li>Perhatikan curah hujan dan suhu lingkungan agar hasil prediksi lebih akurat.</li>
        <li>Gunakan hasil rekomendasi sebagai pendukung pengambilan keputusan, bukan sebagai satu-satunya acuan.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.write("")

# =====================================================
# STATUS SISTEM
# =====================================================
st.markdown("## Status Sistem")
status1, status2, status3 = st.columns(3)

with status1:
    st.success("Model AI Aktif")
with status2:
    st.success("Dataset Siap")
with status3:
    st.success("Sistem Berjalan Normal")

st.divider()