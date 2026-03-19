import streamlit as st
from streamlit_google_auth import Authenticate

# --- 1. KONFIGURÁCIA ---
st.set_page_config(
    page_title="OmniTravel", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. INICIALIZÁCIA GOOGLE AUTH (Verzia "Istota") ---
# Načítame si údaje dopredu, aby sme videli, či nie sú prázdne
cid = st.secrets.get("google_client_id")
cs = st.secrets.get("google_client_secret")
ruri = st.secrets.get("redirect_uri")

# Ak niečo chýba, appka nám to teraz povie slušne, namiesto TypeError
if not all([cid, cs, ruri]):
    st.error("Chýbajú údaje v Secrets! Skontroluj google_client_id, google_client_secret a redirect_uri.")
    st.stop()

# Skúsime túto kombináciu parametrov
auth = Authenticate(
    client_id=cid,
    client_secret=cs,
    redirect_uri=ruri + "/component/streamlit_google_oauth.google_oauth/index.html",
    cookie_name="omnitravel_cookie",
    key="omni_secret_123"
)

auth.check_authenticity()
# --- 3. CSS DIZAJN ---
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

    div.stButton > button {
        width: 100% !important; background-color: #FFFFFF !important; color: #1E293B !important;
        padding: 16px !important; border-radius: 50px !important; font-weight: 600 !important;
        border: 1px solid #E2E8F0 !important; box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
        margin-top: 10px !important; transition: 0.3s;
    }
    div.stButton > button:hover { border-color: #4F46E5 !important; transform: translateY(-2px); }

    .brand-title { font-weight: 700; font-size: 2.2rem; color: #1E293B; margin-top: 15px; margin-bottom: 0px; }
    .brand-subtitle { color: #94A3B8; font-size: 1rem; margin-bottom: 40px; }

    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

def render_logo():
    st.markdown("""
        <div style="text-align:center; margin-bottom:10px;">
            <svg width="100" height="100" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="50" cy="50" r="48" stroke="#1E293B" stroke-width="1.5"/>
                <circle cx="50" cy="50" r="40" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="4 2"/>
                <path d="M50 20L58 50L50 46L42 50L50 20Z" fill="#4F46E5"/>
                <path d="M50 80L42 50L50 54L58 50L50 80Z" fill="#94A3B8"/>
                <circle cx="50" cy="50" r="3" fill="#1E293B"/>
            </svg>
        </div>
    """, unsafe_allow_html=True)

# --- 4. LOGIKA ---
if st.session_state.get('connected'):
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    render_logo()
    user = st.session_state['user_info']
    
    st.markdown(f"""
        <div style="background:white; padding:30px; border-radius:30px; border:1px solid #F1F5F9; width:100%; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
            <img src="{user.get('picture')}" style="width:80px; border-radius:50%; margin-bottom:15px; border: 3px solid #F1F5F9;">
            <h2 style="margin:0; color:#1E293B;">Ahoj, {user.get('name')}!</h2>
            <p style="color:#94A3B8;">{user.get('email')}</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("ODHLÁSIŤ SA"):
        auth.logout()
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    render_logo()
    st.markdown('<h1 class="brand-title">OMNITRAVEL</h1>', unsafe_allow_html=True)
    st.markdown('<p class="brand-subtitle">Vaše dobrodružstvo začína.</p>', unsafe_allow_html=True)
    
    # Google tlačidlo
    auth.login_button(color="white", width=320)
    
    st.markdown('<p style="color:#CBD5E1; font-size:0.8rem; margin:15px 0;">ALEBO</p>', unsafe_allow_html=True)
    
    if st.button("POUŽIŤ EMAIL"):
        st.info("Tradičné prihlásenie pripravujeme.")
        
    st.markdown('</div>', unsafe_allow_html=True)
