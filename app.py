import streamlit as st
import math
import base64
import os

# --- 1. KONFIGURÁCIA STRÁNKY ---
st.set_page_config(
    page_title="OmniTravel", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. SESSION STATE ---
if 'step' not in st.session_state: st.session_state.step = "login"

# =========================================================================
# ⚪️ FINAL LUXURY CLEAN STYLE (CSS)
# =========================================================================
STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;600&display=swap');

    /* Globálne nastavenie bieleho pozadia a čiernej farby */
    .stApp { 
        background-color: #FFFFFF !important; 
        color: #000000 !important; 
        font-family: 'Quicksand', sans-serif !important; 
    }

    /* Úprava hlavičky - čistá biela, aby tri čiarky vynikli */
    [data-testid="stHeader"] {
        background-color: #FFFFFF !important;
        border-bottom: 1px solid #F8F8F8;
    }

    /* Odstránenie prebytočného miesta pod hlavičkou */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        max-width: 100% !important;
    }

    /* Nadpisy a texty - ČIERNA */
    h1, h2, h3, p, span, label {
        color: #000000 !important;
        font-family: 'Quicksand', sans-serif !important;
        font-weight: 400 !important;
    }

    /* BOČNÉ MENU (SIDEBAR) */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #EEEEEE;
    }
    
    /* Texty v bočnom menu */
    [data-testid="stSidebarNav"] * {
        color: #000000 !important;
        font-size: 1.1rem !important;
    }

    /* Banner - hranatý a roztiahnutý */
    .banner-wrapper {
        width: 100%;
        margin: 0;
        line-height: 0;
    }
    .omni-banner {
        width: 100%;
        display: block;
        border-bottom: 1px solid #EEEEEE;
    }

    /* Karta príspevku */
    .feed-card {
        background: #FFFFFF;
        border: 1px solid #F5F5F5;
        padding: 20px;
        margin: 20px auto;
        max-width: 500px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }
</style>
"""

# =========================================================================
# 1. PRIHLÁSENIE
# =========================================================================
if st.session_state.step == "login":
    st.markdown(STYLE, unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; padding-top: 120px;">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/fluency-systems-filled/96/000000/globe.png", width=80)
    st.title("OmniTravel")
    st.write("Váš inteligentný sprievodca")
    if st.button("Vstúpiť do aplikácie"): 
        st.session_state.step = "app"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 2. HLAVNÁ APLIKÁCIA
# =========================================================================
elif st.session_state.step == "app":
    st.markdown(STYLE, unsafe_allow_html=True)
    
    # --- BOČNÉ MENU (Tri čiarky) ---
    with st.sidebar:
        st.markdown('<h2 style="text-align: left; padding-left: 10px;">OmniTravel</h2>', unsafe_allow_html=True)
        st.write("---")
        stranka = st.radio(
            "Navigácia", 
            ["Komunitný Feed", "Mapa Okolia", "Skener Menu", "Profil Používateľa"]
        )
        st.write("##")
        if st.button("Odhlásiť sa"):
            st.session_state.step = "login"
            st.rerun()

    # --- OBSAH ---
    if stranka == "Komunitný Feed":
        # Banner hneď pod hornou lištou
        if os.path.exists("header.png"):
            with open("header.png", "rb") as f:
                data = base64.b64encode(f.read()).decode()
            st.markdown(f'<div class="banner-wrapper"><img src="data:image/png;base64,{data}" class="omni-banner"></div>', unsafe_allow_html=True)
        
        st.markdown('<h1 style="text-align: center; margin-top: 40px; font-size: 2rem;">Čo nové v komunite</h1>', unsafe_allow_html=True)

        st.markdown("""
        <div class="feed-card">
            <p style="font-size: 1rem; margin-bottom: 10px;"><b>Maroš Svetobežník</b> • Nové Zámky</p>
            <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=600" style="width:100%; border-radius: 4px;">
            <p style="margin-top: 15px;">Konečne to vyzerá ako poriadna aplikácia. Tri čiarky sú späť a dizajn je čistý a elegantný.</p>
        </div>
        """, unsafe_allow_html=True)

    elif stranka == "Mapa Okolia":
        st.markdown('<div style="padding: 20px;"><h1>Mapa okolia</h1><p>Tu nájdete pamiatky v okolí Nových Zámkov.</p></div>', unsafe_allow_html=True)
    
    elif stranka == "Skener Menu":
        st.markdown('<div style="padding: 20px;"><h1>AI Skener</h1></div>', unsafe_allow_html=True)
        st.camera_input("Odfoťte menu")

    elif stranka == "Profil Používateľa":
        st.markdown('<div style="padding: 20px;"><h1>Môj Profil</h1><p>Level: Zlatý cestovateľ</p></div>', unsafe_allow_html=True)
