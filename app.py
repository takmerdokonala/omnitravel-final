import streamlit as st  # TOTO TU MUSÍ BYŤ AKO PRVÉ
import os

# --- 1. KONFIGURÁCIA ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# --- 2. PAMÄŤ (OPRAVENÁ SEKCE) ---
if 'lang' not in st.session_state: 
    st.session_state.lang = "Slovenčina"
if 'page' not in st.session_state: 
    st.session_state.page = "home"

# Inicializácia profilu vrátane bezbariérovosti
if 'user_data' not in st.session_state:
    st.session_state.user_data = {
        "name": "",
        "city": "",
        "wheelchair": False,  # Bezbariérový prístup
        "interests": []
    }

# --- 3. ROZŠÍRENÝ SLOVNÍK (Pridaná bezbariérovosť) ---
translations = {
    "Slovenčina": {
        "login": "PRIHLÁSIŤ", "register": "REGISTROVAŤ", "select_lang": "VYBERTE JAZYK",
        "home": "DOMOVSKÁ STRÁNKA", "profile": "MÔJ PROFIL", "aimenu": "AI MENU",
        "scanner": "SKENER", "map": "MAPA OKOLIA", "community": "KOMUNITA",
        "wheelchair": "BEZBARIÉROVÝ PRÍSTUP", "save": "ULOŽIŤ PROFIL"
    },
    "English": {
        "login": "LOGIN", "register": "REGISTER", "select_lang": "SELECT LANGUAGE",
        "home": "HOME PAGE", "profile": "MY PROFILE", "aimenu": "AI MENU",
        "scanner": "SCANNER", "map": "MAP AREA", "community": "COMMUNITY",
        "wheelchair": "WHEELCHAIR ACCESS", "save": "SAVE PROFILE"
    }
    # ... sem môžeš doplniť ostatné jazyky z predošlého kódu
}

T = translations.get(st.session_state.lang, translations["Slovenčina"])

# --- 4. FUNKCIE ---
def set_page(p):
    st.session_state.page = p

# --- 5. OBSAH STRÁNKY (PROFIL) ---
if st.session_state.page == "profile":
    st.markdown(f"## {T['profile']}")
    
    # Ak profil neexistuje, ukážeme formulár
    if st.session_state.user_data["name"] == "":
        with st.form("edit_profile"):
            name = st.text_input("Meno")
            city = st.text_input("Mesto")
            
            # Prepínač pre bezbariérovosť (Toggle)
            wc = st.toggle(T["wheelchair"], value=st.session_state.user_data["wheelchair"])
            
            submit = st.form_submit_button(T["save"])
            if submit:
                st.session_state.user_data.update({"name": name, "city": city, "wheelchair": wc})
                st.rerun()
    else:
        # Zobrazenie profilu
        st.success(f"Profil: {st.session_state.user_data['name']}")
        if st.session_state.user_data["wheelchair"]:
            st.info("♿ Aktívny bezbariérový režim")
        
        if st.button("Upraviť"):
            st.session_state.user_data["name"] = ""
            st.rerun()
