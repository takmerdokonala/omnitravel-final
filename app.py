import streamlit as st
from streamlit_google_auth import Authenticate

# --- 1. ZÁKLADNÁ KONFIGURÁCIA (Hneď na začiatku) ---
st.set_page_config(
    page_title="OmniTravel", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. INICIALIZÁCIA GOOGLE AUTH ---
# Kód číta údaje priamo z tvojho Streamlit Cloud Secrets
auth = Authenticate(
    secret_key=st.secrets["google_client_secret"],
    client_id=st.secrets["google_client_id"],
    redirect_uri=st.secrets["redirect_uri"] + "/component/streamlit_google_oauth.google_oauth/index.html",
    cookie_name="omnitravel_login_cookie"
)

# Kontrola, či sa používateľ práve vracia z Google prihlásenia
auth.check_authenticity()

# --- 3. DIZAJN (Tvoj biely štýl s kompasom) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] { 
        font-family: 'Plus Jakarta Sans', sans-serif !important; 
        background-color: #FFFFFF !important;
    }
    
    .main-container {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        text-align: center; min-height: 85vh; width: 100%; max-width: 400px; margin: auto;
    }

    /* Biele bublinové tlačidlá */
    div.stButton > button {
        width: 100% !important; background-color: #FFFFFF !important; color: #1E293B !important;
        padding: 16px !important; border-radius: 50px !important; font-weight: 600 !important;
        border: 1px solid #E2E8F0 !important; box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
        margin-top: 10px !important; transition: 0.3s;
    }
    div.stButton > button:hover { border-color: #4F46E5 !important;
