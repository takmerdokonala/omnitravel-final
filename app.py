import streamlit as st
from streamlit_google_oauth import login_button

# --- 1. KONFIGURÁCIA ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# Načítanie údajov zo Secrets
CLIENT_ID = st.secrets.get("google_client_id")
CLIENT_SECRET = st.secrets.get("google_client_secret")
REDIRECT_URI = st.secrets.get("redirect_uri")

# --- 2. DIZAJN (Tvoj biely štýl) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif !important; background-color: #FFFFFF !important; }
    .main-container { display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; min-height: 80vh; margin: auto; max-width: 400px; }
    .brand-title { font-weight: 700; font-size: 2.2rem; color: #1E293B; margin-top: 15px; }
    .brand-subtitle { color: #94A3B8; margin-bottom: 40px; }
    div.stButton > button { width: 100% !important; background-color: #FFFFFF !important; border-radius: 50px !important; padding: 14px !important; border: 1px solid #E2E8F0 !important; font-weight: 600 !important; }
</style>
""", unsafe_allow_html=True)

def render_logo():
    st.markdown('<div style="text-align:center;"><svg width="80" height="80" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" stroke="#1E293B" stroke-width="2" fill="none"/><path d="M50 20L60 50L50 45L40 50L50 20Z" fill="#4F46E5"/></svg></div>', unsafe_allow_html=True)

# --- 3. LOGIKA PRIHLÁSENIA ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)
render_logo()
st.markdown('<h1 class="brand-title">OMNITRAVEL</h1>', unsafe_allow_html=True)

if not CLIENT_ID or not CLIENT_SECRET:
    st.error("Nastav si Secrets (ID a Secret)!")
else:
    # Tlačidlo z novej knižnice
    login_info = login_button(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
    )

    if login_info:
        access_token, user_id, user_email = login_info
        st.success(f"Vitaj, {user_email}!")
        if st.button("ODHLÁSIŤ SA"):
            st.rerun()
    else:
        st.markdown('<p class="brand-subtitle">Vaše dobrodružstvo začína.</p>', unsafe_allow_html=True)
        # Tlačidlo sa zobrazí automaticky funkciou login_button vyššie

st.markdown('</div>', unsafe_allow_html=True)
