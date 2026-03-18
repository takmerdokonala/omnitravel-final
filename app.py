import streamlit as st

# --- 1. KONFIGURÁCIA ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# --- 2. DIZAJN (CSS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] { 
        font-family: 'Plus Jakarta Sans', sans-serif !important; 
        background-color: #FFFFFF !important;
    }
    
    /* Vycentrovanie na stred obrazovky */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        height: 85vh;
        width: 100%;
    }

    /* Biele bubliny - presne podľa tvojho prvého obrázka */
    div.stButton > button {
        width: 320px !important;
        background-color: #FFFFFF !important;
        color: #1E293B !important;
        padding: 18px !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.04) !important;
        margin: 10px auto !important;
        display: block;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        border-color: #4F46E5 !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.08) !important;
        transform: translateY(-2px);
    }

    .brand-title {
        font-weight: 700;
        font-size: 2.5rem;
        color: #1E293B;
        margin-top: 15px;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }

    .brand-subtitle {
        color: #94A3B8;
        font-size: 1rem;
        margin-bottom: 50px;
    }

    /* Schovanie dekorácií */
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    [data-testid="stToolbar"] { display: none; }
</style>
""", unsafe_allow_html=True)

# --- 3. OBSAH ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# LOGO KOMPAS (SVG) - Presne podľa 1000116054.jpg
st.markdown("""
    <svg width="120" height="120" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="48" stroke="#1E293B" stroke-width="1.5"/>
        <circle cx="50" cy="50" r="40" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="4 2"/>
        <path d="M50 20L58 50L50 46L42 50L50 20Z" fill="#4F46E5"/>
        <path d="M50 80L42 50L50 54L58 50L50 80Z" fill="#94A3B8"/>
        <circle cx="50" cy="50" r="3" fill="#1E293B"/>
    </svg>
""", unsafe_allow_html=True)

st.markdown('<h1 class="brand-title">OMNITRAVEL</h1>', unsafe_allow_html=True)
st.markdown('<p class="brand-subtitle">Vaše dobrodružstvo začína.</p>', unsafe_allow_html=True)

# TLAČIDLÁ (Biele bubliny)
if st.button("PRIHLÁSENIE"):
    st.info("Pripravujem prihlasovací formulár...")

if st.button("REGISTRÁCIA"):
    st.info("Pripravujem registračný formulár...")

st.markdown('</div>', unsafe_allow_html=True)
