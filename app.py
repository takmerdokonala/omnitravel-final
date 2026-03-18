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
# ⚪️ CLEAN MODERN STYLE (CSS)
# =========================================================================
STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;600&display=swap');

    /* Odstránenie prebytočného miesta na vrchu */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
    }

    /* Úprava hlavičky aby nezavadzala, ale nechala menu viditeľné */
    [data-testid="stHeader"] {
        background-color: rgba(255,255,255,0.1) !important;
        color: #000000 !important;
    }

    .stApp { 
        background-color: #FFFFFF !important; 
        color: #000000 !important; 
        font-family: 'Quicksand', sans-serif !important; 
    }
    
    /* Nadpisy - ČISTÁ ČIERNA */
    h1, h2, h3, p, span {
        color: #000000 !important;
        font-family: 'Quicksand', sans-serif !important;
        font-weight: 400;
    }

    /* BOČNÉ MENU (SIDEBAR) - Elegantná biela */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #EEEEEE;
    }
    
    /* Nápisy v menu - Čierne a väčšie */
    [data-testid="stSidebarNav"] * {
        color: #000000 !important;
        font-size: 1.1rem !important;
        font-weight: 500 !important;
    }

    /* Banner od okraja po okraj */
    .banner-wrapper {
        width: 100%;
        margin-top: 0;
        line-height: 0;
    }
    .omni-banner {
        width: 100%;
        display: block;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }

    /* Karty feedu */
    .feed-card {
        background: #FFFFFF;
        border: 1px solid #F5F5F5;
        padding: 20px;
        margin: 20px auto;
        max-width: 600px;
        box-shadow: 0 2px 15px rgba(0,0,0,0.02);
    }
</style>
"""

# =========================================================================
# 1. PRIHLÁSENIE
# =========================================================================
if st.session_state.step == "login":
    st.markdown(STYLE, unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; padding-top: 100px;">', unsafe_allow_html=True)
    st.title("OmniTravel")
    st.write("Vstúpte do sveta bez hraníc")
    if st.button("Vstúpiť"): 
        st.session_state.step = "app"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 2. HLAVNÁ APLIKÁCIA (S TRI ČIARKAMI)
# =========================================================================
elif st.session_state.step == "app":
    st.markdown(STYLE, unsafe_allow_html=True)
    
    # --- BOČNÉ MENU ---
    with st.sidebar:
        st.markdown('<h2 style="margin-bottom:0;">OmniTravel</h2>', unsafe_allow_html=True)
        st.write("---")
        stranka = st.radio(
            "Menu", 
            ["Komunitný Feed", "Mapa Okolia", "Skener Menu", "Môj Profil"]
        )
        st.write("##")
        if st.button("Odhlásiť sa"):
            st.session_state.step = "login"
            st.rerun()

    # --- BANNER ÚPLNE HORE (iba vo Feede) ---
    if stranka == "Komunitný Feed":
        if os.path.exists("header.png"):
            with open("header.png", "rb") as f:
                data = base64.b64encode(f.read()).decode()
            st.markdown(f'<div class="banner-wrapper"><img src="data:image/png;base64,{data}" class="omni-banner"></div>', unsafe_allow_html=True)
        
        st.markdown('<h1 style="text-align: center; margin-top: 30px;">Čo nové v komunite</h1>', unsafe_allow_html=True)

        # Príspevok vo feede
        st.markdown("""
        <div class="feed-card">
            <p><b>Maroš Svetobežník</b> • Nové Zámky</p>
            <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=600" style="width:100%; margin: 15px 0;">
            <p>Konečne to vyzerá ako poriadna aplikácia. Tri čiarky sú základ!</p>
        </div>
        """, unsafe_allow_html=True)

    elif stranka == "Mapa Okolia":
        st.markdown('<div style="padding: 20px;"><h1>Mapa okolia</h1></div>', unsafe_allow_html=True)
    
    elif stranka == "Skener Menu":
        st.markdown('<div style="padding: 20px;"><h1>AI Skener</h1></div>', unsafe_allow_html=True)
        st.camera_input("Odfoťte menu")

    elif stranka == "Môj Profil":
        st.markdown('<div style="padding: 20px;"><h1>Môj Profil</h1></div>', unsafe_allow_html=True)
