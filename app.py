import streamlit as st
import math
import base64
import os

# --- 1. ZÁKLADNÉ NASTAVENIE ---
st.set_page_config(
    page_title="OmniTravel", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. PAMÄŤ APLIKÁCIE ---
if 'step' not in st.session_state: st.session_state.step = "login"

# =========================================================================
# ⚪️ FINÁLNY LUXUSNÝ DIZAJN (CSS)
# =========================================================================
STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;600&display=swap');

    /* Celkové pozadie a font */
    .stApp { 
        background-color: #FFFFFF !important; 
        font-family: 'Quicksand', sans-serif !important; 
    }

    /* ÚPLNÉ ODSTRÁNENIE BIELYCH OKRAJOV A OPRAVA HLAVIČKY */
    [data-testid="stHeader"] {
        background-color: rgba(255,255,255,0) !important;
        border: none !important;
    }
    
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
    }

    /* ČIERNE A ELEGANTNÉ NÁPISY */
    h1, h2, h3, p, span, div {
        color: #000000 !important;
        font-weight: 400 !important;
    }

    /* BOČNÉ MENU - ČISTÉ A PREHĽADNÉ */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #EEEEEE;
    }
    
    [data-testid="stSidebarNav"] * {
        color: #000000 !important;
        font-size: 1.2rem !important;
    }

    /* BANNER - HRANATÝ, BEZ OKRAJOV, OD VRCHU */
    .banner-box {
        width: 100%;
        margin: 0;
        padding: 0;
        line-height: 0;
        margin-top: -50px; /* Posun pod tri čiarky */
    }
    
    .omni-banner {
        width: 100%;
        display: block;
        object-fit: cover;
    }

    /* ODDEĽOVAČ */
    .line {
        height: 1px;
        background-color: #F0F0F0;
        width: 100%;
        margin: 20px 0;
    }
</style>
"""

# =========================================================================
# 1. OBRAZOVKA: PRIHLÁSENIE
# =========================================================================
if st.session_state.step == "login":
    st.markdown(STYLE, unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; padding-top: 150px;">', unsafe_allow_html=True)
    st.markdown('<h1 style="font-size: 3rem;">OmniTravel</h1>', unsafe_allow_html=True)
    st.write("Cestovanie v najčistejšej forme")
    if st.button("VSTÚPIŤ"): 
        st.session_state.step = "app"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 2. HLAVNÁ APLIKÁCIA
# =========================================================================
elif st.session_state.step == "app":
    st.markdown(STYLE, unsafe_allow_html=True)
    
    # BOČNÉ MENU (Tri čiarky)
    with st.sidebar:
        st.markdown('<h1>Menu</h1>', unsafe_allow_html=True)
        stranka = st.radio("", ["Komunita", "Mapa", "Skener", "Môj Profil"])
        st.write("---")
        if st.button("Odhlásiť sa"):
            st.session_state.step = "login"
            st.rerun()

    # OBSAH STRÁNOK
    if stranka == "Komunita":
        # Banner úplne od vrchu
        if os.path.exists("header.png"):
            with open("header.png", "rb") as f:
                data = base64.b64encode(f.read()).decode()
            st.markdown(f'<div class="banner-box"><img src="data:image/png;base64,{data}" class="omni-banner"></div>', unsafe_allow_html=True)
        
        st.markdown('<h1 style="text-align: center; margin-top: 50px; font-size: 2.5rem;">Čo nové v komunite</h1>', unsafe_allow_html=True)
        st.markdown('<div class="line"></div>', unsafe_allow_html=True)

        # Príspevok vo feede
        st.markdown("""
        <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
            <p style="font-size: 1.2rem;"><b>Maroš Svetobežník</b> • Nové Zámky</p>
            <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=600" style="width:100%; border-radius: 0px; margin: 15px 0;">
            <p>Tento dizajn je presne to, čo sme hľadali. Čisté, čierne a bez zbytočností.</p>
        </div>
        """, unsafe_allow_html=True)

    elif stranka == "Mapa":
        st.markdown('<div style="padding: 50px; text-align: center;"><h1>Mapa okolia</h1></div>', unsafe_allow_html=True)
    elif stranka == "Skener":
        st.markdown('<div style="padding: 50px; text-align: center;"><h1>Skener menu</h1></div>', unsafe_allow_html=True)
        st.camera_input("")
    elif stranka == "Môj Profil":
        st.markdown('<div style="padding: 50px; text-align: center;"><h1>Môj Profil</h1></div>', unsafe_allow_html=True)
