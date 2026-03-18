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

# --- 3. FUNKCIA NA VÝPOČET VZDIALENOSTI ---
def vypocitaj_vzdialenost(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 2)

# =========================================================================
# ⚪️ ULTRA CLEAN & NO-MARGIN STYLE (CSS)
# =========================================================================
STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500;700&display=swap');

    /* ODSTRÁNENIE HORNÉHO BIELO PRIESTORU */
    [data-testid="stHeader"] {
        display: none !important;
    }
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
    }
    #root > div:nth-child(1) > div > div > div > div > section > div {
        padding-top: 0rem !important;
    }

    .stApp { 
        background-color: #FFFFFF !important; 
        color: #000000 !important; 
        font-family: 'Quicksand', sans-serif !important; 
    }
    
    /* Čierne nadpisy */
    h1, h2, h3, p, span, li {
        color: #000000 !important;
        font-family: 'Quicksand', sans-serif !important;
    }

    /* Bočné menu - čisto biele s čiernym textom */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #EEEEEE;
    }
    [data-testid="stSidebarNav"] * {
        color: #000000 !important;
        font-weight: 500 !important;
    }

    /* Banner bez okrajov */
    .banner-wrapper {
        width: 100%;
        margin: 0 !important;
        padding: 0 !important;
        line-height: 0;
    }
    .omni-banner {
        width: 100%;
        display: block;
        margin: 0;
    }

    /* Oddelenie banneru od obsahu */
    .separator {
        height: 2px;
        background: rgba(0,0,0,0.05);
        width: 100%;
        margin-bottom: 20px;
    }

    /* Karty feedu */
    .feed-card {
        background: #FFFFFF;
        border: 1px solid #F5F5F5;
        padding: 20px;
        border-radius: 0px; /* Hranatý štýl */
        margin: 10px 15px 20px 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.02);
    }
</style>
"""

# =========================================================================
# 1. PRIHLÁSENIE
# =========================================================================
if st.session_state.step == "login":
    st.markdown(STYLE, unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; padding-top: 100px;">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/fluency-systems-filled/96/000000/globe.png", width=80)
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
    
    with st.sidebar:
        st.markdown('<h2 style="margin-top:0;">OmniTravel</h2>', unsafe_allow_html=True)
        stranka = st.radio("Menu", ["Komunitný Feed", "Mapa", "Skener", "Profil"])
        if st.button("Odhlásiť"):
            st.session_state.step = "login"
            st.rerun()

    if stranka == "Komunitný Feed":
        # Banner úplne hore
        if os.path.exists("header.png"):
            with open("header.png", "rb") as f:
                data = base64.b64encode(f.read()).decode()
            st.markdown(f"""
                <div class="banner-wrapper">
                    <img src="data:image/png;base64,{data}" class="omni-banner">
                </div>
                <div class="separator"></div>
            """, unsafe_allow_html=True)
        
        # Elegantný čierny nadpis
        st.markdown('<h1 style="text-align: center; font-weight: 300; font-size: 1.8rem; margin-top: 10px;">Čo nové v komunite</h1>', unsafe_allow_html=True)

        # Feed bez emoji
        st.markdown("""
        <div class="feed-card">
            <p><b>Maroš Svetobežník</b> • Nové Zámky</p>
            <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=600" style="width:100%;">
            <p><br>Skvelý tip na kaviareň. Tento čistý dizajn bez zbytočných prvkov pôsobí veľmi profesionálne.</p>
        </div>
        """, unsafe_allow_html=True)

    elif stranka == "Mapa":
        st.markdown('<div style="padding: 20px;"><h1>Mapa okolia</h1></div>', unsafe_allow_html=True)
    elif stranka == "Skener":
        st.markdown('<div style="padding: 20px;"><h1>Skener menu</h1></div>', unsafe_allow_html=True)
    elif stranka == "Profil":
        st.markdown('<div style="padding: 20px;"><h1>Profil</h1></div>', unsafe_allow_html=True)
