import streamlit as st
import os

# --- 1. KONFIGURÁCIA ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# --- 2. VEĽKÝ SLOVNÍK PREKLADOV ---
# Tu môžeš kedykoľvek pridať ďalšie riadky podľa rovnakého vzoru
translations = {
    "Slovenčina": {
        "login": "PRIHLÁSIŤ", "register": "REGISTROVAŤ", "select_lang": "VYBERTE JAZYK",
        "home": "DOMOVSKÁ STRÁNKA", "profile": "MÔJ PROFIL", "aimenu": "AI MENU",
        "scanner": "SKENER", "map": "MAPA OKOLIA", "community": "KOMUNITA"
    },
    "Čeština": {
        "login": "PŘIHLÁSIT", "register": "REGISTROVAT", "select_lang": "VYBERTE JAZYK",
        "home": "DOMOVSKÁ STRÁNKA", "profile": "MŮJ PROFIL", "aimenu": "AI MENU",
        "scanner": "SKENER", "map": "MAPA OKOLÍ", "community": "KOMUNITA"
    },
    "English": {
        "login": "LOGIN", "register": "REGISTER", "select_lang": "SELECT LANGUAGE",
        "home": "HOME PAGE", "profile": "MY PROFILE", "aimenu": "AI MENU",
        "scanner": "SCANNER", "map": "MAP AREA", "community": "COMMUNITY"
    },
    "Deutsch": {
        "login": "ANMELDEN", "register": "REGISTRIEREN", "select_lang": "SPRACHE WÄHLEN",
        "home": "STARTSEITE", "profile": "MEIN PROFIL", "aimenu": "KI MENÜ",
        "scanner": "SCANNER", "map": "UMGEBUNGSKARTE", "community": "GEMEINSCHAFT"
    },
    "Magyar": {
        "login": "BELÉPÉS", "register": "REGISZTRÁCIÓ", "select_lang": "NYELV VÁLASZTÁS",
        "home": "KEZDŐLAP", "profile": "PROFILOM", "aimenu": "AI MENÜ",
        "scanner": "SZKENNER", "map": "KÖRNYÉK TÉRKÉPE", "community": "KÖZÖSSÉG"
    },
    "Polski": {
        "login": "ZALOGUJ", "register": "ZAREJESTRUJ", "select_lang": "WYBIERZ JĘZYK",
        "home": "STRONA GŁÓWNA", "profile": "MÓJ PROFIL", "aimenu": "MENU AI",
        "scanner": "SKANER", "map": "MAPA OKOLICY", "community": "SPOŁECZNOŚĆ"
    },
    "Français": {
        "login": "CONNEXION", "register": "S'INSCRIRE", "select_lang": "CHOISIR LA LANGUE",
        "home": "ACCUEIL", "profile": "MON PROFIL", "aimenu": "MENU IA",
        "scanner": "SCANNER", "map": "CARTE", "community": "COMMUNAUTÉ"
    },
    "Español": {
        "login": "ACCESO", "register": "REGISTRARSE", "select_lang": "ELEGIR IDIOMA",
        "home": "PÁGINA DE INICIO", "profile": "MI PERFIL", "aimenu": "MENÚ IA",
        "scanner": "ESCÁNER", "map": "MAPA", "community": "COMUNIDAD"
    },
    "Italiano": {
        "login": "ACCEDI", "register": "REGISTRATI", "select_lang": "SCEGLI LINGUA",
        "home": "HOME PAGE", "profile": "IL MIO PROFILO", "aimenu": "MENU IA",
        "scanner": "SCANNER", "map": "MAPPA", "community": "COMMUNITÀ"
    },
    "Українська": {
        "login": "УВІЙТИ", "register": "РЕЄСТРАЦІЯ", "select_lang": "ВИБЕРІТЬ МОВУ",
        "home": "ГОЛОВНА", "profile": "МІЙ ПРОФІЛЬ", "aimenu": "AI МЕНЮ",
        "scanner": "СКАНЕР", "map": "КАРТА", "community": "СПІЛЬНОТА"
    }
}

# --- 3. PAMÄŤ A STAV ---
if 'lang' not in st.session_state: st.session_state.lang = "Slovenčina"
if 'page' not in st.session_state: st.session_state.page = "home"

T = translations[st.session_state.lang]

# --- 4. CALLBACKS ---
def change_lang():
    st.session_state.lang = st.session_state.new_lang_val

def set_page(p):
    st.session_state.page = p

# --- 5. CSS (Zachovaný biely dizajn) ---
st.markdown(f"""
<style>
    .stApp, [data-testid="stSidebar"] {{ 
        background-color: #FFFFFF !important; 
        font-family: 'Inter', sans-serif; 
    }}
    .nav-top-auth {{ 
        display: flex; background-color: #333333; color: white; text-align: center; 
    }}
    .nav-auth-item {{ 
        flex: 1; padding: 18px 0; font-size: 0.8rem; font-weight: 600; border-right: 1px solid #444; 
    }}
    .lang-box {{
        background-color: #F9F9F9; padding: 10px 20px; border-bottom: 1px solid #EEE;
    }}
    div.stButton > button {{
        width: 100% !important; border: none !important;
        border-bottom: 1px solid #F5F5F5 !important;
        background-color: transparent !important; color: #000000 !important;
        padding: 22px 20px !important; text-align: left !important;
        font-size: 0.95rem !important; border-radius: 0px !important;
    }}
    div.stButton > button:hover {{ background-color: #FBFBFB !important; }}
</style>
""", unsafe_allow_html=True)

# --- 6. SIDEBAR ---
with st.sidebar:
    st.markdown(f'''
        <div class="nav-top-auth">
            <div class="nav-auth-item">{T["login"]}</div>
            <div class="nav-auth-item" style="border-right:none;">{T["register"]}</div>
        </div>
    ''', unsafe_allow_html=True)

    st.markdown(f'<div class="lang-box"><small style="color:#999">{T["select_lang"]}</small></div>', unsafe_allow_html=True)
    st.selectbox(
        "Lang", options=list(translations.keys()), 
        index=list(translations.keys()).index(st.session_state.lang),
        key="new_lang_val", on_change=change_lang, label_visibility="collapsed"
    )

    st.write("") 
    st.button(T["home"], on_click=set_page, args=("home",))
    st.button(T["profile"], on_click=set_page, args=("profile",))
    st.button(T["aimenu"], on_click=set_page, args=("aimenu",))
    st.button(T["scanner"], on_click=set_page, args=("scanner",))
    st.button(T["map"], on_click=set_page, args=("map",))
    st.button(T["community"], on_click=set_page, args=("community",))

# --- 7. OBSAH ---
st.markdown(f'<h1 style="text-align:center; margin-top:50px; font-weight:300; text-transform:uppercase; letter-spacing:2px;">{T[st.session_state.page]}</h1>', unsafe_allow_html=True)
