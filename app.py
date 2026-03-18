import streamlit as st
import base64
import os

# --- 1. KONFIGURÁCIA ---
st.set_page_config(
    page_title="OmniTravel", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. PAMÄŤ PRE STAV ---
if 'page' not in st.session_state: st.session_state.page = "DOMOVSKÁ STRÁNKA"
if 'lang' not in st.session_state: st.session_state.lang = "Slovenčina"

# =========================================================================
# ⚪️ CSS OPRAVA PRE FUNKČNOSŤ KLIKANIA
# =========================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

    .stApp { background-color: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }

    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E0E0E0;
    }
    [data-testid="stSidebarUserContent"] { padding: 0rem !important; }

    /* LOGIN / REGISTER PANEL */
    .nav-top-auth {
        display: flex; 
        background-color: #333333; 
        color: white; 
        text-align: center;
        width: 100%;
    }
    .nav-auth-item {
        flex: 1; 
        padding: 18px 0; 
        font-size: 0.8rem; 
        font-weight: 600;
        border-right: 1px solid #444;
        letter-spacing: 1px;
    }

    /* ÚPRAVA JAZYKOVÉHO POLA */
    .lang-container {
        background-color: #F9F9F9;
        padding: 10px 20px 5px 20px;
        border-bottom: 1px solid #EEE;
    }
    .lang-text {
        font-size: 0.7rem;
        color: #999;
        margin-bottom: 5px;
        text-transform: uppercase;
    }

    /* ŠTÝLOVANIE MENU TLAČIDIEL */
    div.stButton > button {
        width: 100% !important;
        border: none !important;
        border-bottom: 1px solid #F5F5F5 !important;
        background-color: transparent !important;
        color: #000 !important;
        padding: 22px 20px !important;
        text-align: left !important;
        font-size: 0.95rem !important;
        border-radius: 0px !important;
    }
    div.stButton > button:hover { background-color: #FBFBFB !important; }

</style>
""", unsafe_allow_html=True)

# =========================================================================
# 📱 SIDEBAR - JEDNODUCHÝ A FUNKČNÝ
# =========================================================================
with st.sidebar:
    # 1. Login a Register (Vizuálne)
    st.markdown('<div class="nav-top-auth"><div class="nav-auth-item">LOGIN</div><div class="nav-auth-item" style="border-right:none;">REGISTER</div></div>', unsafe_allow_html=True)

    # 2. Jazyky (Funkčné Streamlit pole)
    st.markdown('<div class="lang-container"><div class="lang-text">Jazyk / Language</div></div>', unsafe_allow_html=True)
    
    # Tento komponent je teraz "čistý" a prístupný pre kliknutie
    seznam_jazykov = ["Slovenčina", "Čeština", "English", "Deutsch", "Français", "Español", "Italiano"]
    
    st.session_state.lang = st.selectbox(
        "Zmeň jazyk",
        options=seznam_jazykov,
        index=seznam_jazykov.index(st.session_state.lang),
        label_visibility="collapsed"
    )

    st.write("") # Medzera

    # 3. Navigačné menu
    if st.button("DOMOVSKÁ STRÁNKA"): st.session_state.page = "DOMOVSKÁ STRÁNKA"
    if st.button("MÔJ PROFIL"): st.session_state.page = "MÔJ PROFIL"
    if st.button("AI MENU"): st.session_state.page = "AI MENU"
    if st.button("SCANNER"): st.session_state.page = "SCANNER"
    if st.button("MAPA OKOLIA"): st.session_state.page = "MAPA OKOLIA"
    if st.button("KOMUNITA"): st.session_state.page = "KOMUNITA"

# =========================================================================
# 🖼️ ZOBRAZENIE OBSAHU
# =========================================================================
st.markdown(f'<h1 style="text-align:center; margin-top:50px; font-weight:300;">{st.session_state.page}</h1>', unsafe_allow_html=True)
st.info(f"Aktuálny jazyk aplikácie: {st.session_state.lang}")
