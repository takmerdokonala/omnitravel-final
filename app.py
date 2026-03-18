import streamlit as st
import base64
import os

# --- 1. KONFIGURÁCIA ---
st.set_page_config(
    page_title="OmniTravel", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. PAMÄŤ PRE NAVIGÁCIU ---
if 'page' not in st.session_state: st.session_state.page = "DOMOVSKÁ STRÁNKA"

# =========================================================================
# ⚪️ STABILNÝ DIZAJN (OPRAVA ZVISLÉHO TEXTU)
# =========================================================================
STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

    .stApp { background-color: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }
    [data-testid="stHeader"] { background-color: white !important; }
    .block-container { padding: 0rem !important; }

    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E0E0E0;
        width: 320px !important;
    }
    [data-testid="stSidebarUserContent"] { padding: 0rem !important; }

    /* HORNÁ AUTH SEKCIA (Login/Register) */
    .nav-top-auth {
        display: flex; background-color: #333333; color: white; text-align: center;
    }
    .nav-auth-item {
        flex: 1; padding: 18px 0; font-size: 0.85rem; font-weight: 500;
        border-right: 1px solid #444444; letter-spacing: 1px;
    }

    /* JAZYKOVÝ PÁSIK */
    .nav-lang-bar {
        display: flex; background-color: #F9F9F9; border-bottom: 1px solid #EEEEEE;
    }
    .nav-lang-item {
        flex: 1; padding: 12px 0; text-align: center; font-size: 0.85rem; color: #999999;
    }
    .nav-lang-active { color: #000000; font-weight: 600; }

    /* ŠTÝLOVANIE TLAČIDIEL AKO POLOŽIEK MENU */
    div.stButton > button {
        width: 100% !important;
        border: none !important;
        border-bottom: 1px solid #F5F5F5 !important;
        background-color: transparent !important;
        color: #000000 !important;
        padding: 25px 20px !important;
        text-align: left !important;
        font-size: 1rem !important;
        border-radius: 0px !important;
        font-weight: 400 !important;
        display: block !important;
    }
    
    div.stButton > button:hover {
        background-color: #FBFBFB !important;
        color: #000000 !important;
    }

    /* Banner a texty */
    .banner-box { width: 100%; line-height: 0; }
    .omni-banner { width: 100%; display: block; }
    h1 { color: #000000 !important; font-weight: 300 !important; text-align: center; text-transform: uppercase; letter-spacing: 2px; }
</style>
"""

st.markdown(STYLE, unsafe_allow_html=True)

# =========================================================================
# 📱 BOČNÉ MENU (SIDEBAR)
# =========================================================================
with st.sidebar:
    # 1. Horný panel
    st.markdown('<div class="nav-top-auth"><div class="nav-auth-item">LOGIN</div><div class="nav-auth-item" style="border-right:none;">REGISTER</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-lang-bar"><div class="nav-lang-item nav-lang-active">SK</div><div class="nav-lang-item" style="border-right:none;">EN</div></div>', unsafe_allow_html=True)

    # 2. Navigačné tlačidlá (Namiesto radio buttons pre stabilitu)
    if st.button("DOMOVSKÁ STRÁNKA"): st.session_state.page = "DOMOVSKÁ STRÁNKA"
    if st.button("MÔJ PROFIL"): st.session_state.page = "MÔJ PROFIL"
    if st.button("AI MENU"): st.session_state.page = "AI MENU"
    if st.button("SCANNER"): st.session_state.page = "SCANNER"
    if st.button("MAPA OKOLIA"): st.session_state.page = "MAPA OKOLIA"
    if st.button("KOMUNITA"): st.session_state.page = "KOMUNITA"

    st.markdown('<div style="padding: 40px 20px; color: #BBB; font-size: 0.7rem; text-align: center; letter-spacing: 2px;">OMNITRAVEL v1.0</div>', unsafe_allow_html=True)

# =========================================================================
# 🖼️ OBSAH STRÁNKY
# =========================================================================
page = st.session_state.page

if page == "DOMOVSKÁ STRÁNKA" or page == "KOMUNITA":
    if os.path.exists("header.png"):
        with open("header.png", "rb") as f:
            data = base64.b64encode(f.read()).decode()
        st.markdown(f'<div class="banner-box"><img src="data:image/png;base64,{data}" class="omni-banner"></div>', unsafe_allow_html=True)

st.markdown(f'<h1 style="margin-top: 50px;">{page}</h1>', unsafe_allow_html=True)

# Ukážka obsahu
if page == "DOMOVSKÁ STRÁNKA":
    st.markdown('<div style="text-align:center; padding: 20px; color:#666;">Vitajte v stabilnom a čistom OmniTravel rozhraní.</div>', unsafe_allow_html=True)
elif page == "SCANNER":
    st.camera_input("Odfoťte menu")
