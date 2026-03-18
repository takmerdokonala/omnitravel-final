import streamlit as st
import base64
import math
import os # Pre kontrolu súborov

# --- 1. KONFIGURÁCIA STRÁNKY ---
st.set_page_config(
    page_title="OmniTravel White", 
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
# ⚪️ PURE WHITE & LUXURY NEON STYLE (CSS)
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
    
    /* Menu Fix (Tri čiarky) */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #F0F0F0;
    }
    
    /* Vynútenie tmavej farby pre texty v menu */
    [data-testid="stSidebarNav"] * {
        color: #4B0082 !important;
        font-weight: 600 !important;
    }

    /* Nadpisy a karty */
    h1, h2, h3 { color: #8A2BE2 !important; font-weight: 700; }
    
    .card {
        background: #FFFFFF;
        border: 1px solid #F0F0F0;
        padding: 20px; border-radius: 15px; margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
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
    
    # SIDEBAR
    with st.sidebar:
        st.markdown('<h2>💜 OmniTravel</h2>', unsafe_allow_html=True)
        st.write("---")
        stranka = st.radio(
            "HLAVNÉ MENU",
            ["📸 Komunitný Feed", "🗺️ Mapa & Pamiatky", "🤖 AI Skener", "👤 Profil"]
        )
        st.write("##")
        if st.button("Odhlásiť sa"):
            set_step_login()
            st.rerun()

    # --- OBSAH STRÁNOK ---

    # --- A. KOMUNITNÝ FEED (BIELA VERZIA S VLOŽENÝM BANNEROM) ---
    if stranka == "📸 Komunitný Feed":
        
        # 🚨 🚨 🚨 KĽÚČOVÁ ČASŤ: VLOŽENIE OBRÁZKA DO ČELA 🚨 🚨 🚨
        
        # Kontrola, či si nahrala súbor 'header.png' na GitHub
        if os.path.exists("header.png"):
            # Otvoríme a preložíme obrázok do base64 (reč pre HTML)
            with open("header.png", "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
            
            # Vložíme obrázok ako banner s fialovým glow tieňom
            st.markdown(f"""
            <div style="width: 100%; border-radius: 20px; overflow: hidden; box-shadow: 0 0 25px rgba(138, 43, 226, 0.3); border: 2px solid rgba(138, 43, 226, 0.2); margin-bottom: 20px;">
                <img src="data:image/png;base64,{encoded_string}" style="width: 100%; object-fit: cover;">
            </div>
            """, unsafe_allow_html=True)
        else:
            # Ak si ho zabudla nahrať, ukážeme záchranný nápis
            st.error("🚨 Chyba: Zabudla si nahrať 'header.png' na GitHub! Appka padla. Nahraj ho prosím.")
            st.markdown("""
            <div class="card" style="background-color: red; color: white;">
                <h1>OmniTravel - AI sprievodca cestovaním</h1>
            </div>
            """, unsafe_allow_html=True)
        
        # --- ZVYŠOK FEEDU ---
        st.title("📸 Čo nové v komunite?")
        
        st.markdown("""
        <div class="card">
            <p><b>Maroš Svetobežník</b> • Nové Zámky</p>
            <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=600" style="width:100%; border-radius:10px;">
            <p><br>Skvelý tip na kaviareň! Táto biela verzia appky vyzerá neskutočne čisto. ❤️ 45</p>
        </div>
        """, unsafe_allow_html=True)

    # --- B. MAPA & PAMIATKY ---
    elif stranka == "🗺️ Mapa & Pamiatky":
        st.title("🗺️ Okolie")
        # Centrum NZ
        moje_lat, moje_lon = 47.985, 18.161
        dist = vypocitaj_vzdialenost(moje_lat, moje_lon, 47.981, 18.160)
        st.markdown(f'<div class="card"><h3>🏛️ Kalvária NZ</h3>Vzdialenosť: <b>{dist} km</b></div>', unsafe_allow_html=True)

    # --- C. AI SKENER ---
    elif stranka == "🤖 AI Skener":
        st.title("🤖 AI Skener")
        st.camera_input("Odfoť menu")
        st.info("AI pripravená na analýzu.")

    # --- D. PROFIL ---
    elif stranka == "👤 Profil":
        st.title("👤 Profil")
        st.markdown('<div class="card"><h3>Body: 250 VP</h3>Level: 1</div>', unsafe_allow_html=True)
        st.progress(25)
