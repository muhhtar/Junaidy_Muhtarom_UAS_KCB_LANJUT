import streamlit as st
from config import USERS, APP_NAME, APP_VERSION

# ==========================================
# SESSION
# ==========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "nama" not in st.session_state:
    st.session_state.nama = ""

if "role" not in st.session_state:
    st.session_state.role = ""

# ==========================================
# LOGIN
# ==========================================

def login():

    st.markdown("""
    <div class="hero">
        <h1>🌱 Smart Farming Assistant</h1>
        <h2>Artificial Intelligence Platform</h2>
        <p>
        Sistem Rekomendasi Tanaman Berbasis
        Random Forest Classifier
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    c1, c2, c3 = st.columns([1,2,1])

    with c2:

        st.markdown("## Login")

        username = st.text_input(
            "Username",
            placeholder="Masukkan username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Masukkan password"
        )

        remember = st.checkbox(
            "Ingat saya"
        )

        login_btn = st.button(
            "LOGIN",
            use_container_width=True
        )

        if login_btn:

            if username in USERS:

                if USERS[username]["password"] == password:

                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.nama = USERS[username]["nama"]
                    st.session_state.role = USERS[username]["role"]

                    st.success("Login berhasil")

                    st.rerun()

                else:

                    st.error("Password salah.")

            else:

                st.error("Username tidak ditemukan.")

        st.write("")

        st.caption(
            f"{APP_NAME} v{APP_VERSION}"
        )

# ==========================================
# LOGOUT
# ==========================================

def logout():

    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.nama = ""
    st.session_state.role = ""

    st.rerun()

# ==========================================
# SIDEBAR USER
# ==========================================

def sidebar_user():

    with st.sidebar:

        st.success("Login Berhasil")

        st.write("### 👤 Pengguna")

        st.write(st.session_state.nama)

        st.caption(st.session_state.role)

        st.divider()

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            logout()