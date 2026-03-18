import streamlit as st

# --- 1. KONFIGURÁCIA ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# --- 2. SLOVNÍK PREKLADOV ---
translations = {
    "Slovenčina": {
        "login": "PRIHLÁSIŤ", "register": "REGISTROVAŤ", "select_lang": "VYBERTE JAZYK",
        "home": "DOMOVSKÁ STRÁNKA", "profile": "MÔJ PROFIL", "aimenu": "AI MENU",
        "scanner": "SKENER", "map": "MAPA OKOLIA", "community": "KOMUNITA",
        "welcome": "Vitajte v OmniTravel!"
    },
    "English": {
        "login": "LOGIN", "register": "REGISTER", "select_lang": "SELECT LANGUAGE",
        "home": "HOME PAGE", "profile": "MY PROFILE", "aimenu": "AI MENU",
        "scanner": "SCANNER", "map": "MAP AREA", "community": "COMMUNITY",
        "welcome": "Welcome to OmniTravel!"
    },
    "Deutsch": {
        "login": "ANMELDEN", "register": "REGISTRIEREN", "select_lang": "SPRACHE WÄHLEN",
        "home": "STARTSEITE", "profile": "MEIN PROFIL", "aimenu": "KI MENÜ",
        "scanner": "SCANNER", "map": "UMGEBUNGSKARTE", "community": "GEMEINSCHAFT",
        "welcome": "Willkommen bei OmniTravel!"
    }
}

# --- 3. PAMÄŤ ---
if 'lang' not in st.session_state: st.session_state.lang = "Slovenčina"
if 'page' not in st.session_state: st.session_state.page = "home"

# Skratka pre aktuálny preklad
T = translations[st.session_state.lang]

# --- 4. FUNKCIE ---
def change_lang():
    st.session_state.lang = st.session_state.new_lang_val

def set_page(p):
    st.session_state.page = p

# --- 5. CSS ---
st.markdown(f"""
<style>
    .stApp {{ background-color: #FFFFFF; font-family: 'Inter', sans-serif; }}
    .nav-top-auth {{ display: flex; background-color: #333333; color: white; text-align: center; }}
    .nav-auth-item {{ flex: 1; padding: 18px 0; font-size: 0.8rem; font-weight: 600; border-right: 1px solid #444; }}
    div.stButton > button {{
        width: 100%; border: none; border-bottom: 1px solid #F5F5F5;
        background-color: transparent; color: #000; padding: 20px;
        text-align: left; font-size: 1rem; border-radius: 0px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 6. SIDEBAR ---
with st.sidebar:
    # Login/Register s prekladom
    st.markdown(f'''
        <div class="nav-top-auth">
            <div class="nav-auth-item">{T["login"]}</div>
            <div class="nav-auth-item" style="border-right:none;">{T["register"]}</div>
        </div>
    ''', unsafe_allow_html=True)

    # Funkčný výber jazyka
    st.caption(f"🌍 {T['select_lang']}")
    st.selectbox(
        "Lang", options=list(translations.keys()), 
        index=list(translations.keys()).index(st.session_state.lang),
        key="new_lang_val", on_change=change_lang, label_visibility="collapsed"
    )

    st.write("---")

    # Menu s prekladom
    if st.button(T["home"]): set_page("home")
    if st.button(T["profile"]): set_page("profile")
    if st.button(T["aimenu"]): set_page("aimenu")
    if st.button(T["scanner"]): set_page("scanner")
    if st.button(T["map"]): set_page("map")
    if st.button(T["community"]): set_page("community")

# --- 7. OBSAH ---
st.markdown(f'<h1 style="text-align:center; margin-top:50px;">{T[st.session_state.page]}</h1>', unsafe_allow_html=True)
st.write(f"### {T['welcome']}")
