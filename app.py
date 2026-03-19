import streamlit as st

# --- 1. KONFIGURÁCIA ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# Načítanie údajov zo Secrets
# Ak si ich v Streamlit Cloud zmazala, vlož ich tam znova (ID a Redirect URI)
CLIENT_ID = st.secrets.get("google_client_id", "")
REDIRECT_URI = st.secrets.get("redirect_uri", "https://omnitravel-final.streamlit.app")

# --- 2. DIZAJN ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif !important; background-color: #FFFFFF !important; }
    .main-container { display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; min-height: 80vh; margin: auto; max-width: 400px; }
    .brand-title { font-weight: 700; font-size: 2.2rem; color: #1E293B; margin-top: 15px; }
    .brand-subtitle { color: #94A3B8; font-size: 1rem; margin-bottom: 40px; }
    .google-btn {
        display: inline-block; width: 100%; padding: 14px; background-color: #FFFFFF; color: #1E293B;
        border-radius: 50px; border: 1px solid #E2E8F0; font-weight: 600; text-decoration: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03); transition: 0.3s;
    }
    .google-btn:hover { border-color: #4F46E5; transform: translateY(-2px); text-decoration: none; color: #1E293B; }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Logo
st.markdown('<div style="text-align:center;"><svg width="80" height="80" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" stroke="#1E293B" stroke-width="2" fill="none"/><path d="M50 20L60 50L50 45L40 50L50 20Z" fill="#4F46E5"/></svg></div>', unsafe_allow_html=True)

st.markdown('<h1 class="brand-title">OMNITRAVEL</h1>', unsafe_allow_html=True)

# Vytvorenie linku bez urllib
login_url = f"https://accounts.google.com/o/oauth2/v2/auth?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=token&scope=openid%20email%20profile"

# Kontrola prihlásenia cez query parametre
if "access_token" in st.query_params:
    st.success("Prihlásenie úspešné!")
    if st.button("VSTÚPIŤ DO APP"):
        st.query_params.clear()
        st.rerun()
else:
    st.markdown('<p class="brand-subtitle">Vaše dobrodružstvo začína.</p>', unsafe_allow_html=True)
    st.markdown(f'<a href="{login_url}" class="google-btn">Sign in with Google</a>', unsafe_allow_html=True)
    
    st.markdown('<p style="color:#CBD5E1; font-size:0.8rem; margin:15px 0;">ALEBO</p>', unsafe_allow_html=True)
    if st.button("POUŽIŤ EMAIL"):
        st.info("Pripravujeme...")

st.markdown('</div>', unsafe_allow_html=True)
