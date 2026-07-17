# ============================================
# SMART FARMING ASSISTANT
# CONFIGURATION
# ============================================

APP_NAME = "Smart Farming Assistant"

APP_VERSION = "3.0"

MODEL_NAME = "Random Forest Classifier"

# ============================================
# USER LOGIN
# ============================================

USERS = {

    "admin": {
        "password": "admin123",
        "nama": "Administrator",
        "role": "Admin"
    },

    "junaidy": {
        "password": "2305101101",
        "nama": "Junaidy Muhtarom",
        "role": "Developer"
    },

    "dosen": {
        "password": "dosen123",
        "nama": "Dosen Penguji",
        "role": "Viewer"
    }

}

# ============================================
# DATASET
# ============================================

DATASET = {

    "nama": "Crop Recommendation Dataset",

    "jumlah_data": 2200,

    "jumlah_kelas": 22,

    "jumlah_parameter": 7

}

# ============================================
# INFORMASI SISTEM
# ============================================

SYSTEM = {

    "framework": "Streamlit",

    "bahasa": "Python",

    "machine_learning": "Scikit-Learn",

    "algoritma": "Random Forest Classifier"

}

# ============================================
# WARNA
# ============================================

THEME = {

    "primary": "#2E7D32",

    "secondary": "#43A047",

    "background": "#F4F7F9",

    "card": "#FFFFFF",

    "text": "#1F2937"

}