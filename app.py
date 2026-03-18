import streamlit as st
import math
import base64
import os

# --- 1. KONFIGURÁCIA STRÁNKY ---
st.set_page_config(
    page_title="OmniTravel", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. SESSION STATE ---
if 'step' not in st.session_state: st.session_state.step = "login"
if 'page' not in st.session_state: st.session_state.page = "Komunita"

# --- 3. FUNKCIA NA VÝPOČET VZDIALENOSTI ---
def vypocitaj_vzdialenost(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 2)

# =========================================================================
# ⚪️ ELEGANT BLACK & WHITE NAVIGATION STYLE (CSS)
# =========================================================================
STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;600&display=swap');

    /* Odstránenie Streamlit prvkov a bielych okrajov */
    [data-testid="stHeader"] { display: none !important; }
    .block-container { padding: 0rem !important; }
    
    .stApp { 
        background-color: #FFFFFF !important; 
        color: #000000 !important; 
        font-family: 'Quicksand', sans-serif !important; 
    }

    /* Full-width Banner */
    .banner-container {
        width: 100%;
        margin: 0;
        padding: 0;
        line-height: 0;
    }
    .omni-banner {
        width: 100%;
        display: block;
    }

    /* Vlastné elegantné menu */
    .nav-bar {
        display: flex;
        justify-content: center;
        gap: 30px;
        padding: 20px 0;
        border-bottom: 1px solid #EEEEEE;
        background: #FFFFFF;
    }
    
    .nav-item {
        color: #000000 !important;
        text-decoration: none !important;
        font-size: 1.2rem;
        font-weight: 400;
        cursor: pointer;
        transition: 0.3s;
    }
    .nav-item:hover {
        font-weight: 600;
    }

    /* Čierne nadpisy */
    h1, h2, h3 {
        color: #000000 !important;
        font-weight: 400 !important;
        text-align: center;
    }

    /* Karta feedu */
    .feed-card {
        max-width: 600px;
        margin: 30px auto;
        padding: 20px;
        background: #FFFFFF;
        border: 1px solid #F5F5F5;
        box-shadow: 0 2px 15px rgba(0,0,0,0.02);
    }
    
    /* Skrytie sidebar tlačidla */
    [data-testid="collapsedControl"] { display: none !important; }
</style>
"""

# =========================================================================
# 1. PRIHLÁSENIE
# =========================================================================
if st.session_state.step == "login":
    st.markdown(STYLE, unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; padding-top: 150px;">', unsafe_allow_html=True)
    st.title("OmniTravel")
    if st.button("Vstúpiť"): 
        st.session_state.step = "app"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 2. HLAVNÁ APLIKÁCIA
# =========================================================================
elif st.session_state.step == "app":
    st.markdown(STYLE, unsafe_allow_html=True)
    
    # 🚨 BANNER ÚPLNE HORE
    if os.path.exists("header.png"):
        with open("header.png", "rb") as f:
            data = base64.b64encode(f.read()).decode()
        st.markdown(f'<div class="banner-container"><img src="data:image/png;base64,{data}" class="omni-banner"></div>', unsafe_allow_html=True)

    # 🚨 ELEGANTNÁ NAVIGÁCIA (NAMIESTO SIDEBARU)
    col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
    with col2:
        if st.button("Komunita"): st.session_state.page = "Komunita"
    with col3:
        if st.button("Mapa"): st.session_state.page = "Mapa"
    with col4:
        if st.button("Skener"): st.session_state.page = "Skener"
    with col5:
        if st.button("Profil"): st.session_state.page = "Profil"
    
    st.markdown('<div style="height: 1px; background: #EEEEEE; width: 100%; margin-bottom: 20px;"></div>', unsafe_allow_html=True)

    # --- OBSAH ---
    if st.session_state.page == "Komunita":
        st.markdown('<h1 style="font-size: 2.2rem; margin-top: 20px;">Čo nové v komunite</h1>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feed-card">
            <p style="font-size: 1.1rem;"><b>Maroš Svetobežník</b> • Nové Zámky</p>
            <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=600" style="width:100%; margin: 15px 0;">
            <p>Skvelý tip na kaviareň. Tento čistý dizajn s pevnou navigáciou a čiernym písmom pôsobí veľmi elegantne.</p>
        </div>
        """, unsafe_allow_html=True)

    elif st.session_state.page == "Mapa":
        st.markdown('<h1>Mapa okolia</h1>', unsafe_allow_html=True)
        # Príklad pamiatky
        st.markdown('<div class="feed-card"><h3>Kalvária Nové Zámky</h3><p>Vzdialenosť: 1.2 km</p></div>', unsafe_allow_html=True)

    elif st.session_state.page == "Skener":
        st.markdown('<h1>Skener menu</h1>', unsafe_allow_html=True)
        st.camera_input("Odfoťte menu")

    elif st.session_state.page == "Profil":
        st.markdown('<h1>Môj profil</h1>', unsafe_allow_html=True)
        if st.button("Odhlásiť sa"):
            st.session_state.step = "login"
            st.rerun()
