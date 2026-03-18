import streamlit as st
import base64
import os

# --- 1. KONFIGURÁCIA ---
st.set_page_config(
    page_title="OmniTravel", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. PAMÄŤ PRE NAVIGÁCIU A JAZYK ---
if 'page' not in st.session_state: st.session_state.page = "DOMOVSKÁ STRÁNKA"
if 'lang' not in st.session_state: st.session_state.lang = "Slovenčina"

# =========================================================================
# ⚪️ ELEGANTNÝ GLOBÁLNY DIZAJN (CSS)
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

    /* JAZYKOVÁ SEKCIA - ŠTÝLOVANIE SELECTBOXU */
    .lang-label {
        padding: 10px 20px 0px 20px;
        font-size: 0.75rem;
        color: #999;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Úprava Streamlit selectboxu aby sedel do menu */
    div[data-testid="stSelectbox"] {
        padding: 0 15px 10px 15px !important;
    }

    /* ŠTÝLOVANIE TLAČIDIEL MENU */
    div.stButton > button {
        width: 100% !important;
        border: none !important;
        border-bottom: 1px solid #F5F5F5 !important;
        background-color: transparent !important;
        color: #000000 !important;
        padding: 22px 20px !important;
        text-align: left !important;
        font-size: 0.95rem !important;
        border-radius: 0px !important;
        font-weight: 400 !important;
    }
    
    div.stButton > button:hover {
        background-color: #FBFBFB !important;
    }

    /* Nadpisy */
    h1 { color: #000000 !important; font-weight: 300 !important; text-align: center; text-transform: uppercase; letter-spacing: 2px; }
</style>
"""

st.markdown(STYLE, unsafe_allow_html=True)

# =========================================================================
# 📱 BOČNÉ MENU (SIDEBAR)
# =========================================================================
with st.sidebar:
    # 1. Login / Register
    st.markdown('<div class="nav-top-auth"><div class="nav-auth-item">LOGIN</div><div class="nav-auth-item" style="border-right:none;">REGISTER</div></div>', unsafe_allow_html=True)

    # 2. Výber jazyka (Všetky jazyky sveta)
    st.markdown('<div class="lang-label">Vyberte jazyk / Select Language</div>', unsafe_allow_html=True)
    
    # Tu môžeš doplniť akékoľvek ďalšie jazyky
    seznam_jazykov = [
        "Slovenčina", "Čeština", "English", "Deutsch", "Français", 
        "Español", "Italiano", "Polski", "Magyar", "Tiếng Việt", "日本語"
    ]
    
    selected_lang = st.selectbox(
        "Language",
        seznam_jazykov,
        index=seznam_jazykov.index(st.session_state.lang),
        label_visibility="collapsed"
    )
    st.session_state.lang = selected_lang

    # 3. Navigačné menu (Stabilné tlačidlá)
    st.write("---") # Jemná deliaca čiara
    
    if st.button("DOMOVSKÁ STRÁNKA"): st.session_state.page = "DOMOVSKÁ STRÁNKA"
    if st.button("MÔJ PROFIL"): st.session_state.page = "MÔJ PROFIL"
    if st.button("AI MENU"): st.session_state.page = "AI MENU"
    if st.button("SCANNER"): st.session_state.page = "SCANNER"
    if st.button("MAPA OKOLIA"): st.session_state.page = "MAPA OKOLIA"
    if st.button("KOMUNITA"): st.session_state.page = "KOMUNITA"

    st.markdown(f'<div style="padding: 40px 20px; color: #BBB; font-size: 0.7rem; text-align: center; letter-spacing: 2px;">OMNITRAVEL v1.0 | {st.session_state.lang.upper()}</div>', unsafe_allow_html=True)

# =========================================================================
# 🖼️ OBSAH STRÁNKY
# =========================================================================
page = st.session_state.page

if page == "DOMOVSKÁ STRÁNKA" or page == "KOMUNITA":
    if os.path.exists("header.png"):
        with open("header.png", "rb") as f:
            data = base64.b64encode(f.read()).decode()
        st.markdown(f'<div style="width:100%; line-height:0;"><img src="data:image/png;base64,{data}" style="width:100%;"></div>', unsafe_allow_html=True)

st.markdown(f'<h1 style="margin-top: 50px;">{page}</h1>', unsafe_allow_html=True)

st.write(f"Zvolený jazyk rozhrania: **{st.session_state.lang}**")
