import streamlit as st
import math
import base64
import os # Pre kontrolu súborov

# --- 1. KONFIGURÁCIA STRÁNKY ---
# layout="wide" je kľúčové pre full-width banner
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
# ⚪️ PURE WHITE & FULL-WIDTH STYLE (CSS)
# =========================================================================
WHITE_STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500;700&display=swap');

    .stApp { 
        background-color: #FFFFFF !important; 
        color: #1A1A1A !important; 
        font-family: 'Quicksand', sans-serif !important; 
        font-weight: 300; 
    }
    
    /* FIX: Bočné menu */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #F0F0F0;
    }
    
    /* FIX: Tmavofialová pre texty v menu */
    [data-testid="stSidebarNav"] * {
        color: #4B0082 !important;
        font-weight: 600 !important;
    }

    /* Nadpisy a karty (H2, H3) - Odteraz ČIERNE */
    h2, h3 { 
        color: #1A1A1A !important; /* Čierna namiesto fialovej */
        font-weight: 700; 
    }
    
    .omni-card, .feed-card {
        background: #FFFFFF;
        border: 1px solid #F0F0F0;
        padding: 20px; border-radius: 15px; margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    }
    
    /* Špeciálny štýl pre banner bez bielych okrajov */
    .banner-container {
        width: 100vw; /* 100% šírky obrazovky */
        margin-left: -1rem; /* Kompenzácia predvoleného paddingu Streamlitu */
        margin-right: -1rem;
        margin-top: -1rem;
        overflow: hidden;
    }
    .omni-banner {
        width: 100%;
        object-fit: cover;
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
    st.write("Vstúp do novej éry čistého cestovania.")
    if st.button("✨ Vstúpiť"): 
        set_step_app()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 2. HLAVNÁ APLIKÁCIA (S HAMBURGER MENU)
# =========================================================================
elif st.session_state.step == "app":
    st.markdown(WHITE_STYLE, unsafe_allow_html=True)
    
    # --- BOČNÉ MENU (SIDEBAR) ---
    with st.sidebar:
        st.markdown('<h2>💜 OmniTravel</h2>', unsafe_allow_html=True)
        st.write("---")
        
        # Pekne vypísaný zoznam navigácie (radio button)
        stranka = st.radio(
            "NAVIGÁCIA",
            ["Komunitný Feed", "Mapa Okolia", "AI Skener Menu", "Profil"],
            index=0 # Predvolená Komunita
        )
        st.write("##")
        if st.button("Odhlásiť sa"):
            set_step_login()
            st.rerun()

    # --- OBSAH STRÁNOK ---

    # --- A. KOMUNITNÝ FEED (S BANNEROM OD OKRAJA PO OKRAJ) ---
    if stranka == "Komunitný Feed":
        
        # 🚨 🚨 🚨 KĽÚČOVÁ ČASŤ: FULL-WIDTH BANNER 🚨 🚨 🚨
        
        # Kontrola, či si nahrala súbor 'header.png' na GitHub
        if os.path.exists("header.png"):
            # Otvoríme a preložíme obrázok do base64 (HTML reč)
            with open("header.png", "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
            
            # Vložíme obrázok v full-width kontajneri s ELEGANTNÝM TIEŇOM pre oddelenie
            st.markdown(f"""
            <div class="banner-container" style="box-shadow: 0 10px 30px rgba(138, 43, 226, 0.15); border-bottom: 2px solid rgba(138, 43, 226, 0.1);">
                <img src="data:image/png;base64,{encoded_string}" class="omni-banner">
            </div>
            """, unsafe_allow_html=True)
        else:
            # Ak zabudneš nahrať header.png na GitHub
            st.error("🚨 Chyba: Zabudla si nahrať 'header.png' na GitHub! Appka spadla. Nahraj ho prosím.")
            st.markdown('<h1>OmniTravel Prototyp</h1>', unsafe_allow_html=True)

        # --- NOVÝ ČIERNY NADPIS (A ELEGANNTÉ ODDIELENIE) ---
        st.write("###")
        # Tu prefarbíme na čiernu
        st.markdown('<h1 style="color: #1A1A1A; font-family: Quicksand, sans-serif; font-weight: 300; text-align: center; font-size: 2rem; margin-top: 15px;">Čo nové v komunite</h1>', unsafe_allow_html=True)
        st.write("##")

        # --- ZVYŠOK FEEDU ---
        st.markdown("""
        <div class="feed-card">
            <p><b>Maroš Svetobežník</b> • Nové Zámky</p>
            <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=600" style="width:100%; border-radius:10px;">
            <p><br>Skvelý tip na kaviareň! Táto biela verzia appky vyzerá neskutočne čisto a prémiovo. ❤️ 45</p>
        </div>
        """, unsafe_allow_html=True)

    # --- B. MAPA OKOLIA ---
    elif stranka == "Mapa Okolia":
        st.title("🗺️ Pamiatky v okolí")
        # Centrum NZ
        moje_lat, moje_lon = 47.985, 18.161
        dist = vypocitaj_vzdialenost(moje_lat, moje_lon, 47.981, 18.160)
        st.markdown(f'<div class="omni-card"><h3>🏛️ Kalvária NZ</h3>Vzdialenosť: <b>{dist} km</b></div>', unsafe_allow_html=True)

    # --- C. AI SKENER ---
    elif stranka == "AI Skener Menu":
        st.title("🤖 AI Skener")
        st.camera_input("Odfoťte dokument")
        st.info("Pripravené na skenovanie.")

    # --- D. PROFIL ---
    elif stranka == "Profil":
        st.title("👤 Profil")
        st.markdown('<div class="omni-card"><h3>Body: 250 VP</h3>Level: 1</div>', unsafe_allow_html=True)
        st.progress(25)
