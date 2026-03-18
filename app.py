import streamlit as st
import base64
import os

# --- 1. KONFIGURÁCIA ---
st.set_page_config(
    page_title="OmniTravel", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. FUNKCIE PRE ZMENU STAVU (CALLBACKS) ---
def change_page(new_page):
    st.session_state.page = new_page

def change_lang():
    # Táto funkcia sa zavolá automaticky pri zmene v selectboxe
    st.session_state.lang = st.session_state.lang_selector

# --- 3. INICIALIZÁCIA PAMÄTE ---
if 'page' not in st.session_state: st.session_state.page = "DOMOVSKÁ STRÁNKA"
if 'lang' not in st.session_state: st.session_state.lang = "Slovenčina"

# =========================================================================
# ⚪️ CSS PRE KRAJŠÍ VZHĽAD
# =========================================================================
st.markdown("""
<style>
    .stApp { background-color: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }
    [data-testid="stSidebar"] { background-color: #FFFFFF !important; border-right: 1px solid #E0E0E0; }
    
    /* Horný tmavý pás */
    .nav-top-auth { display: flex; background-color: #333333; color: white; text-align: center; }
    .nav-auth-item { flex: 1; padding: 18px 0; font-size: 0.8rem; font-weight: 600; border-right: 1px solid #444; }

    /* Štýl tlačidiel v menu */
    div.stButton > button {
        width: 100% !important;
        border: none !important;
        border-bottom: 1px solid #F5F5F5 !important;
        background-color: transparent !important;
        color: #000 !important;
        padding: 20px !important;
        text-align: left !important;
        font-size: 1rem !important;
        border-radius: 0px !important;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================================
# 📱 SIDEBAR (BOČNÉ MENU)
# =========================================================================
with st.sidebar:
    # 1. Login/Register (statické)
    st.markdown('<div class="nav-top-auth"><div class="nav-auth-item">LOGIN</div><div class="nav-auth-item" style="border-right:none;">REGISTER</div></div>', unsafe_allow_html=True)

    # 2. VÝBER JAZYKA (S kľúčom a callbackom)
    st.write("")
    st.caption("🌍 VYBERTE JAZYK / SELECT LANGUAGE")
    
    seznam_jazykov = ["Slovenčina", "Čeština", "English", "Deutsch", "Français", "Español"]
    
    st.selectbox(
        "Jazyk",
        options=seznam_jazykov,
        index=seznam_jazykov.index(st.session_state.lang),
        key="lang_selector",
        on_change=change_lang,
        label_visibility="collapsed"
    )

    st.write("---")

    # 3. NAVIGÁCIA (Tlačidlá s callbackom)
    menu_items = ["DOMOVSKÁ STRÁNKA", "MÔJ PROFIL", "AI MENU", "SCANNER", "MAPA OKOLIA", "KOMUNITA"]
    
    for item in menu_items:
        st.button(item, on_click=change_page, args=(item,))

# =========================================================================
# 🖼️ HLAVNÝ OBSAH
# =========================================================================
# Nadpis sa mení podľa stlačenia tlačidla
st.markdown(f'<h1 style="text-align:center; margin-top:50px;">{st.session_state.page}</h1>', unsafe_allow_html=True)

# Kontrola, či sa jazyk mení
st.write(f"🌐 Aktuálne nastavený jazyk: **{st.session_state.lang}**")

if st.session_state.page == "SCANNER":
    st.camera_input("Odfoťte dokument")
