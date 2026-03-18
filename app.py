import streamlit as st
import os

# --- 1. KONFIGURÁCIA (Musí byť úplne hore!) ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# --- 2. PAMÄŤ A STAV ---
if 'lang' not in st.session_state: st.session_state.lang = "Slovenčina"
if 'page' not in st.session_state: st.session_state.page = "home"
if 'user_data' not in st.session_state:
    st.session_state.user_data = {"name": "", "city": "", "wheelchair": False}

# --- 3. SLOVNÍK PREKLADOV ---
translations = {
    "Slovenčina": {
        "login": "PRIHLÁSIŤ", "register": "REGISTROVAŤ", "select_lang": "VYBERTE JAZYK",
        "home": "DOMOVSKÁ STRÁNKA", "profile": "MÔJ PROFIL", "aimenu": "AI MENU",
        "scanner": "SKENER", "map": "MAPA OKOLIA", "community": "KOMUNITA",
        "wheelchair": "BEZBARIÉROVÝ PRÍSTUP", "save": "ULOŽIŤ PROFIL", "edit": "UPRAVIŤ PROFIL"
    },
    "English": {
        "login": "LOGIN", "register": "REGISTER", "select_lang": "SELECT LANGUAGE",
        "home": "HOME PAGE", "profile": "MY PROFILE", "aimenu": "AI MENU",
        "scanner": "SCANNER", "map": "MAP AREA", "community": "COMMUNITY",
        "wheelchair": "WHEELCHAIR ACCESS", "save": "SAVE PROFILE", "edit": "EDIT PROFILE"
    },
    "Deutsch": {
        "login": "ANMELDEN", "register": "REGISTRIEREN", "select_lang": "SPRACHE WÄHLEN",
        "home": "STARTSEITE", "profile": "MEIN PROFIL", "aimenu": "KI MENÜ",
        "scanner": "SCANNER", "map": "UMGEBUNGSKARTE", "community": "GEMEINSCHAFT",
        "wheelchair": "BARRIEREFREIHEIT", "save": "PROFIL SPEICHERN", "edit": "PROFIL BEARBEITEN"
    }
}
# Pridanie predvoleného jazyka ak by nastala chyba
T = translations.get(st.session_state.lang, translations["Slovenčina"])

# --- 4. FUNKCIE PRE OVLÁDANIE ---
def change_lang():
    st.session_state.lang = st.session_state.new_lang_val

def set_page(p):
    st.session_state.page = p

# --- 5. STYLING (BIELY DIZAJN) ---
st.markdown(f"""
<style>
    .stApp, [data-testid="stSidebar"] {{ background-color: #FFFFFF !important; }}
    .nav-top-auth {{ display: flex; background-color: #333333; color: white; text-align: center; }}
    .nav-auth-item {{ flex: 1; padding: 18px 0; font-size: 0.8rem; font-weight: 600; border-right: 1px solid #444; }}
    div.stButton > button {{
        width: 100% !important; border: none !important; border-bottom: 1px solid #F5F5F5 !important;
        background-color: transparent !important; color: #000000 !important;
        padding: 22px 20px !important; text-align: left !important;
        font-size: 0.95rem !important; border-radius: 0px !important;
    }}
    div.stButton > button:hover {{ background-color: #FBFBFB !important; }}
</style>
""", unsafe_allow_html=True)

# --- 6. SIDEBAR (BOČNÉ MENU) ---
with st.sidebar:
    st.markdown(f'<div class="nav-top-auth"><div class="nav-auth-item">{T["login"]}</div><div class="nav-auth-item" style="border-right:none;">{T["register"]}</div></div>', unsafe_allow_html=True)
    
    st.write("")
    st.selectbox("Lang", options=list(translations.keys()), 
                 index=list(translations.keys()).index(st.session_state.lang),
                 key="new_lang_val", on_change=change_lang, label_visibility="collapsed")
    
    st.write("---")
    st.button(T["home"], on_click=set_page, args=("home",))
    st.button(T["profile"], on_click=set_page, args=("profile",))
    st.button(T["aimenu"], on_click=set_page, args=("aimenu",))
    st.button(T["scanner"], on_click=set_page, args=("scanner",))
    st.button(T["map"], on_click=set_page, args=("map",))
    st.button(T["community"], on_click=set_page, args=("community",))

# --- 7. OBSAH STRÁNKY ---
page = st.session_state.page

if page == "profile":
    st.markdown(f"<h1 style='text-align:center;'>{T['profile']}</h1>", unsafe_allow_html=True)
    if st.session_state.user_data["name"] == "":
        with st.form("p_form"):
            n = st.text_input("Meno")
            c = st.text_input("Mesto")
            wc = st.toggle(T["wheelchair"], value=st.session_state.user_data["wheelchair"])
            if st.form_submit_button(T["save"]):
                st.session_state.user_data.update({"name": n, "city": c, "wheelchair": wc})
                st.rerun()
    else:
        st.success(f"Meno: {st.session_state.user_data['name']}")
        if st.session_state.user_data["wheelchair"]: st.info("♿ Bezbariérový prístup zapnutý")
        if st.button(T["edit"]):
            st.session_state.user_data["name"] = ""
            st.rerun()
else:
    st.markdown(f"<h1 style='text-align:center; margin-top:50px;'>{T[page]}</h1>", unsafe_allow_html=True)
