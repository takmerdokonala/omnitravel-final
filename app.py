import streamlit as st
import base64

# --- 1. KONFIGURÁCIA STRÁNKY (Musí byť úplne hore!) ---
# Nastavíme 'wide' layout, ale v CSS ho obmedzíme pre mobilný vzhľad
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CSS DIZAJN (Tento blok zaručuje biele pozadie a stred) ---
st.markdown("""
<style>
    /* Vynútenie bieleho pozadia pre celú aplikáciu */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] { 
        font-family: 'Plus Jakarta Sans', sans-serif !important; 
        background-color: #FFFFFF !important;
    }

    /* Hlavný kontajner, ktorý vycentruje všetko na stred obrazovky (na výšku aj šírku) */
    .main-center-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        min-height: 85vh; /* Zabezpečí stred na výšku */
        width: 100%;
        max-width: 450px; /* Obmedzenie šírky pre mobilný vzhľad */
        margin: auto;
    }

    /* --- BIELE BUBLINOVÉ TLAČIDLÁ (Presne podľa tvojho vzoru) --- */
    div.stButton > button {
        width: 100% !important;
        max-width: 320px !important; /* Šírka pre biele bubliny */
        background-color: #FFFFFF !important;
        color: #1E293B !important;
        padding: 18px !important;
        border-radius: 50px !important; /* Maximálne zaoblenie - bublina */
        font-weight: 600 !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
        margin: 10px auto !important; /* Odstup pod sebou a vycentrovanie */
        display: block;
        transition: 0.3s all;
    }
    div.stButton > button:hover {
        border-color: #4F46E5 !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.06) !important;
    }

    /* Nadpis OMNITRAVEL */
    .brand-title {
        font-weight: 700;
        font-size: 2.2rem;
        color: #1E293B;
        margin-top: 15px;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }

    /* Podnadpis */
    .brand-subtitle {
        color: #94A3B8;
        font-size: 1rem;
        margin-bottom: 40px;
    }

    /* Odstránenie Streamlit dekorácií na vrchu stránky */
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
</style>
""", unsafe_allow_html=True)

# --- 3. OBSAH A LOGO KOMPASU (VYCENTROVANÉ) ---
# Otvoríme hlavný stredový kontajner
st.markdown('<div class="main-center-container">', unsafe_allow_html=True)

# SVG LOGO KOMPAS (Prekreslené pre perfektnú ostrosť a stred)
# Je to kompas z tvojho prvého obrázka
st.markdown("""
    <svg width="120" height="120" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="48" stroke="#1E293B" stroke-width="1.5"/>
        <circle cx="50" cy="50" r="40" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="4 2"/>
        <path d="M50 20L58 50L50 46L42 50L50 20Z" fill="#4F46E5"/>
        <path d="M50 80L42 50L50 54L58 50L50 80Z" fill="#94A3B8"/>
        <circle cx="50" cy="50" r="3" fill="#1E293B"/>
    </svg>
""", unsafe_allow_html=True)

# Názov a podnadpis
st.markdown('<h1 class="brand-title">OMNITRAVEL</h1>', unsafe_allow_html=True)
st.markdown('<p class="brand-subtitle">Vaše dobrodružstvo začína.</p>', unsafe_allow_html=True)

# TLAČIDLÁ (Biele bubliny pod sebou)
if st.button("PRIHLÁSENIE"):
    st.write("Navigácia na prihlásenie...")

if st.button("REGISTRÁCIA"):
    st.write("Navigácia na registráciu...")

# Koniec kontajnera
st.markdown('</div>', unsafe_allow_html=True)
