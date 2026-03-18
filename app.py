import streamlit as st

# --- 1. KONFIGURÁCIA ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# --- 2. PAMÄŤ ---
if 'is_registered' not in st.session_state: st.session_state.is_registered = False
if 'auth_step' not in st.session_state: st.session_state.auth_step = "welcome" # welcome / login / register

# --- 3. DIZAJN (CSS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }
    
    .stApp { background: white !important; }

    /* Centrujúci kontajner */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin-top: 80px;
    }

    /* Biele bubliny (Tlačidlá) */
    div.stButton > button {
        width: 300px !important;
        background-color: #FFFFFF !important;
        color: #1E293B !important;
        padding: 18px !important;
        border-radius: 50px !important; /* Maximálne zaoblenie - bublina */
        font-weight: 600 !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
        margin-bottom: 15px !important;
        transition: 0.3s all;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    
    div.stButton > button:hover {
        border-color: #4F46E5 !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.08) !important;
    }

    /* Odstránenie Streamlit dekorácií */
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
</style>
""", unsafe_allow_html=True)

# --- 4. LOGO A TEXT (VYCENTROVANÉ) ---
def show_welcome():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # SVG LOGO KOMPAS
    st.markdown("""
        <svg width="100" height="100" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-bottom: 20px;">
            <circle cx="50" cy="50" r="48" stroke="#1E293B" stroke-width="2"/>
            <circle cx="50" cy="50" r="40" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="4 2"/>
            <path d="M50 15L58 45L50 40L42 45L50 15Z" fill="#4F46E5"/>
            <path d="M50 85L42 55L50 60L58 55L50 85Z" fill="#94A3B8"/>
            <circle cx="50" cy="50" r="4" fill="#1E293B"/>
        </svg>
    """, unsafe_allow_html=True)
    
    # NÁZOV A PODNÁZOV
    st.markdown("""
        <h1 style="font-weight: 700; color: #1E293B; margin-bottom: 5px; font-size: 2.2rem;">OMNITRAVEL</h1>
        <p style="color: #64748B; font-size: 1rem; margin-bottom: 40px;">Vaše dobrodružstvo začína.</p>
    """, unsafe_allow_html=True)
    
    # BIELE BUBLINY (TLAČIDLÁ)
    if st.button("PRIHLÁSENIE"):
        st.session_state.auth_step = "login"
        st.rerun()
        
    if st.button("REGISTRÁCIA"):
        st.session_state.auth_step = "register"
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)

# --- 5. LOGIKA STRÁNOK ---
if not st.session_state.is_registered:
    if st.session_state.auth_step == "welcome":
        show_welcome()
    elif st.session_state.auth_step == "login":
        if st.button("← Späť"): 
            st.session_state.auth_step = "welcome"
            st.rerun()
        st.subheader("Prihlásenie")
        # Tu pôjde tvoj login formulár...
    elif st.session_state.auth_step == "register":
        if st.button("← Späť"): 
            st.session_state.auth_step = "welcome"
            st.rerun()
        st.subheader("Registrácia")
        # Tu pôjde tvoj registračný formulár...
else:
    st.success("Vitaj v aplikácii!")
