import streamlit as st
import base64
import math
import os # Pre kontrolu súborov

# --- 1. KONFIGURÁCIA STRÁNKY ---
# layout="wide" je kľúčové pre hranatý banner od okraja po okraj
st.set_page_config(
    page_title="OmniTravel", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. SESSION STATE (PAMÄŤ APPKY) ---
if 'step' not in st.session_state: st.session_state.step = "login"

# --- 3. FUNKCIA NA VÝPOČET VZDIALENOSTI ---
def vypocitaj_vzdialenost(lat1, lon1, lat2, lon2):
    R = 6371 # Polomer Zeme v km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 2)

# =========================================================================
# ⚪️ ULTRA CLEAN WHITE STYLE (CSS)
# =========================================================================
WHITE_STYLE = """
<style>
    /* 1. Import fontov: Quicksand pre eleganciu, Roboto pre jednoduchosť */
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500;700&family=Roboto:wght@300;400&display=swap');

    /* 2. Globálne nastavenia pre čistý dizajn */
    .stApp { 
        background-color: #FFFFFF !important; 
        color: #1A1A1A !important; 
        font-family: 'Roboto', sans-serif !important; /* Základný font */
        font-weight: 300; 
    }
    
    /* 🚨 🚨 🚨 OPRAVA Sidebaru pre bielu 🚨 🚨 🚨 */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #F0F0F0;
    }
    
    /* Vynútenie tmavej farby pre texty v menu */
    [data-testid="stSidebarNav"] * {
        color: #4B0082 !important;
        font-weight: 600 !important;
    }

    /* Nadpisy (H2, H3) zbavené neon efektu */
    h2, h3 { 
        color: #8A2BE2 !important; 
        font-weight: 700; 
        font-family: 'Quicksand', sans-serif !important; 
        text-shadow: none !important;
    }
    
    /* Elegantné Biele Karty zbavené emoji */
    .card {
        background: #FFFFFF;
        border: 1px solid #F0F0F0;
        padding: 20px; border-radius: 15px; margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
        color: #1A1A1A !important;
    }

    /* Tlačidlá zbavené neon efektu */
    div.stButton > button {
        background-color: #FFFFFF;
        border: 1px solid #8A2BE2;
        color: #8A2BE2;
        border-radius: 20px;
        transition: 0.3s;
        text-shadow: none !important;
        box-shadow: none !important;
    }
    div.stButton > button:hover {
        background-color: #F8F0FF;
    }
</style>
"""

# =========================================================================
# FUNKCIE NA OVLÁDANIE KROKOV
# =========================================================================
def set_step_login(): st.session_state.step = "login"
def set_step_app(): st.session_state.step = "app"

# =========================================================================
# 1. OBRAZOVKA: PRIHLÁSENIE
# =========================================================================
if st.session_state.step == "login":
    st.markdown(WHITE_STYLE, unsafe_allow_html=True)
    st.write("##")
    st.markdown('<div style="text-align: center; padding-top: 50px;">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/fluency/96/000000/globe-earth.png", width=100)
    st.title("OmniTravel 2026")
    st.write("Vstúp do éry čistého cestovania.")
    if st.button("✨ Vstúpiť"): 
        set_step_app()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 2. HLAVNÁ APLIKÁCIA (S HAMBURGER MENU)
# =========================================================================
elif st.session_state.step == "app":
    st.markdown(WHITE_STYLE, unsafe_allow_html=True)
    
    # SIDEBAR
    with st.sidebar:
        st.markdown('<h2>💜 OmniTravel</h2>', unsafe_allow_html=True)
        st.write("---")
        # Názvy menu bez emoji
        stranka = st.radio(
            "HLAVNÉ MENU",
            ["Komunitný Feed", "Okres a Pamiatky", "Skener Menu", "Profil"]
        )
        st.write("##")
        if st.button("Odhlásiť sa"):
            set_step_login()
            st.rerun()

    # --- OBSAH STRÁNOK ---

    # --- A. KOMUNITNÝ FEED (BIELA VERZIA S VLOŽENÝM BANNEROM) ---
    if stranka == "Komunitný Feed":
        
        # 🚨 🚨 🚨 KĽÚČOVÁ ČASŤ: VLOŽENIE OBRÁZKA DO ČELA (Hranaté a od okraja) 🚨 🚨 🚨
        if os.path.exists("header.png"):
            with open("header.png", "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
            
            # Hranatý a od okraja po okraj (w-full, m-0)
            st.markdown(f"""
            <div style="width: 100%; overflow: hidden; margin: 0; padding: 0;">
                <img src="data:image/png;base64,{encoded_string}" style="width: 100%; object-fit: cover;">
            </div>
            """, unsafe_allow_html=True)
        else:
            # Ak zabudneš nahrať header.png na GitHub
            st.error("🚨 Chyba: Zabudla si nahrať 'header.png' na GitHub! Appka spadla. Nahraj ho prosím.")

        # --- NOVÝ ELEGANTNÝ NADPIS ---
        # Tu používame font Quicksand pre eleganciu
        st.write("###")
        st.markdown('<h1 style="color: #4B0082; font-family: Quicksand, sans-serif; font-weight: 300; text-align: center; font-size: 2rem;">Čo nové v komunite</h1>', unsafe_allow_html=True)
        st.write("##")

        # --- ZVYŠOK FEEDU ---
        st.markdown("""
        <div class="card">
            <p><b>Maroš Svetobežník</b> • Nové Zámky</p>
            <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=600" style="width:100%; border-radius:10px;">
            <p><br>Skvelý tip na kaviareň! Táto biela verzia appky bez emoji vyzerá neskutočne čisto a prémiovo.</p>
        </div>
        """, unsafe_allow_html=True)

    # --- B. OKRES A PAMIATKY ---
    elif stranka == "Okres a Pamiatky":
        st.title("Pamiatky v okolí")
        # Centrum NZ
        moje_lat, moje_lon = 47.985, 18.161
        dist = vypocitaj_vzdialenost(moje_lat, moje_lon, 47.981, 18.160)
        st.markdown(f'<div class="card"><h3>🏛️ Kalvária NZ</h3>Vzdialenosť: <b>{dist} km od teba</b></div>', unsafe_allow_html=True)

    # --- C. SKENER MENU ---
    elif stranka == "Skener Menu":
        st.title("Inteligentný Skener Menu")
        st.camera_input("Odfoťte menu pre preklad")
        st.info("Pripravené na skenovanie. AI analyzuje dokument.")

    # --- D. PROFIL ---
    elif stranka == "Profil":
        st.title("Profil Cestovateľa")
        st.markdown('<div class="card"><h3>Ocko Cestovateľ</h3>Body: 250 VP<br>Level: Zlatý prieskumník</div>', unsafe_allow_html=True)
        st.progress(25)
