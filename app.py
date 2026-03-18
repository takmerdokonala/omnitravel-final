import streamlit as st

# --- 1. KONFIGURÁCIA ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CSS DIZAJN (Čistý, Biely, Vycentrovaný) ---
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
        height: 80vh;
        width: 100%;
    }

    /* Biele bubliny - tlačidlá */
    div.stButton > button {
        width: 300px !important;
        background-color: #FFFFFF !important;
        color: #1E293B !important;
        padding: 16px !important;
        border-radius: 50px !important; /* Plne zaoblené ako bublina */
        font-weight: 600 !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
        margin: 10px auto !important;
        display: block;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        border-color: #4F46E5 !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.08) !important;
        transform: translateY(-2px);
    }

    /* Názov OMNITRAVEL */
    .brand-title {
        font-weight: 700;
        font-size: 2.2rem;
        color: #1E293B;
        margin-top: 20px;
        margin-bottom: 0px;
    }

    .brand-subtitle {
        color: #94A3B8;
        font-size: 1rem;
        margin-bottom: 40px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. OBSAH (Logo, Text a Tlačidlá) ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# LOGO KOMPAS (SVG verzia pre maximálnu ostrosť)
st.markdown("""
    <svg width="100" height="100" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="48" stroke="#1E293B" stroke-width="1.5"/>
        <circle cx="50" cy="50" r="40" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="4 2"/>
        <path d="M50 15L58 45L50 40L42 45L50 15Z" fill="#4F46E5"/>
        <path d="M50 85L42 55L50 60L58 55L50 85Z" fill="#94A3B8"/>
        <circle cx="50" cy="50" r="4" fill="#1E293B"/>
    </svg>
""", unsafe_allow_html=True)

st.markdown('<h1 class="brand-title">OMNITRAVEL</h1>', unsafe_allow_html=True)
st.markdown('<p class="brand-subtitle">Vaše dobrodružstvo začína.</p>', unsafe_allow_html=True)

# TLAČIDLÁ (Biele bubliny pod sebou)
if st.button("PRIHLÁSENIE"):
    st.write("Klikli ste na prihlásenie")

if st.button("REGISTRÁCIA"):
    st.write("Klikli ste na registráciu")

st.markdown('</div>', unsafe_allow_html=True)
