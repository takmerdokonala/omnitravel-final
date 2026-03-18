import streamlit as st
import base64
import os

# --- 1. KONFIGURÁCIA ---
st.set_page_config(
    page_title="OmniTravel", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. PAMÄŤ ---
if 'step' not in st.session_state: st.session_state.step = "app"

# =========================================================================
# ⚪️ FINÁLNA OPRAVA ZOBRAZENIA (BEZ EMOJI)
# =========================================================================
STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

    .stApp { 
        background-color: #FFFFFF !important; 
        font-family: 'Inter', sans-serif !important; 
    }

    /* SIDEBAR DEFINÍCIA */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E0E0E0;
        width: 320px !important;
    }
    [data-testid="stSidebarUserContent"] { padding-top: 0rem !important; }

    /* HORNÁ ČASŤ (LOGIN/REGISTER) */
    .nav-top-auth {
        display: flex;
        background-color: #333333;
        color: white;
        text-align: center;
    }
    .nav-auth-item {
        flex: 1;
        padding: 18px 0;
        font-size: 0.85rem;
        font-weight: 500;
        border-right: 1px solid #444444;
    }

    /* JAZYKY */
    .nav-lang-bar {
        display: flex;
        background-color: #F9F9F9;
        border-bottom: 1px solid #EEEEEE;
    }
    .nav-lang-item {
        flex: 1;
        padding: 12px 0;
        text-align: center;
        font-size: 0.85rem;
        color: #999999;
    }
    .nav-lang-active { color: #000000; font-weight: 600; }

    /* --- OPRAVA MENU: ABY TEXT NEZMIZOL --- */
    
    /* Nastavenie riadku v menu */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label {
        padding: 15px 20px !important;
        border-bottom: 1px solid #F5F5F5 !important;
        margin: 0 !important;
        width: 100%;
        display: flex !important;
        align-items: center !important;
    }

    /* Schovanie krúžku tak, aby text ostal */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label div:first-child {
        background-color: transparent !important;
        border: none !important;
        width: 0px !important;
        height: 0px !important;
        margin-right: -15px !important;
        visibility: hidden !important;
    }

    /* Vynútenie čiernej farby a viditeľnosti textu */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label div[data-testid="stMarkdownContainer"] p {
        color: #000000 !important;
        font-size: 1.05rem !important;
        font-weight: 500 !important;
        opacity: 1 !important;
        visibility: visible !important;
        text-align: left !important;
        padding-left: 10px !important;
    }

    /* Aktívna položka (pozadie) */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label[data-filled="true"] {
        background-color: #F0F0F0 !important;
    }

    .banner-box { width: 100%; line-height: 0; }
    .omni-banner { width: 100%; display: block; }
</style>
"""

st.markdown(STYLE, unsafe_allow_html=True)

# =========================================================================
# 📱 BOČNÉ MENU
# =========================================================================
with st.sidebar:
    # 1. Login / Register (Pevné HTML)
    st.markdown('<div class="nav-top-auth"><div class="nav-auth-item">LOGIN</div><div class="nav-auth-item" style="border-right:none;">REGISTER</div></div>', unsafe_allow_html=True)

    # 2. Jazyky
    st.markdown('<div class="nav-lang-bar"><div class="nav-lang-item nav-lang-active">SK</div><div class="nav-lang-item" style="border-right:none;">EN</div></div>', unsafe_allow_html=True)

    # 3. Samotné Menu (Texty bez emoji)
    stranka = st.radio(
        "Menu",
        [
            "Domovska stranka", 
            "Moj Profil", 
            "AI Menu", 
            "Scanner", 
            "Mapa okolia", 
            "Komunita"
        ],
        label_visibility="collapsed"
    )

    st.markdown('<div style="padding: 30px; color: #CCC; font-size: 0.7rem; text-align: center;">OMNITRAVEL v1.0</div>', unsafe_allow_html=True)

# =========================================================================
# 🖼️ OBSAH
# =========================================================================
if "Domovska" in stranka or "Komunita" in stranka:
    if os.path.exists("header.png"):
        with open("header.png", "rb") as f:
            data = base64.b64encode(f.read()).decode()
        st.markdown(f'<div class="banner-box"><img src="data:image/png;base64,{data}" class="omni-banner"></div>', unsafe_allow_html=True)

st.markdown(f'<h1 style="text-align: center; margin-top: 50px; font-weight: 400;">{stranka.upper()}</h1>', unsafe_allow_html=True)
