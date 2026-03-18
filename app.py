import streamlit as st
import math

# --- 1. KONFIGURÁCIA STRÁNKY ---
st.set_page_config(
    page_title="OmniTravel White", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. SESSION STATE (PAMÄŤ) ---
if 'step' not in st.session_state: 
    st.session_state.step = "login"

# --- 3. FUNKCIA NA VÝPOČET VZDIALENOSTI ---
def vypocitaj_vzdialenost(lat1, lon1, lat2, lon2):
    R = 6371 
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 2)

# --- 4. ČISTÝ BIELY ŠTÝL (CSS) ---
# Tu som opravil tú chybu, ktorá spôsobovala pád
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500;700&display=swap');

    .stApp { 
        background-color: #FFFFFF !important; 
        color: #1A1A1A !important; 
        font-family: 'Quicksand', sans-serif !important; 
    }
    
    /* OPRAVA VIDITEĽNOSTI MENU */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #F0F0F0;
    }
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: #4B0082 !important;
        font-weight: 600 !important;
    }

    /* Nadpisy a karty */
    h1, h2, h3 { color: #8A2BE2 !important; font-weight: 700; }
    
    .omni-card {
        background: #FFFFFF;
        border: 1px solid #F0F0F0;
        padding: 20px; 
        border-radius: 15px; 
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    }

    /* Tlačidlá */
    div.stButton > button {
        background-color: #FFFFFF;
        border: 1px solid #8A2BE2;
        color: #8A2BE2;
        border-radius: 20px;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================================
# 5. LOGIKA STRÁNOK
# =========================================================================

# --- A. LOGIN ---
if st.session_state.step == "login":
    st.write("##")
    st.markdown('<div style="text-align: center; padding-top: 50px;">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/fluency/96/000000/globe-earth.png", width=100)
    st.title("OmniTravel 2026")
    st.write("Váš inteligentný sprievodca.")
    if st.button("✨ Vstúpiť"): 
        st.session_state.step = "app"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- B. HLAVNÁ APPKA ---
elif st.session_state.step == "app":
    # SIDEBAR
    with st.sidebar:
        st.markdown('<h2>💜 OmniTravel</h2>', unsafe_allow_html=True)
        st.write("---")
        stranka = st.radio(
            "NAVIGÁCIA",
            ["📸 Komunitný Feed", "🗺️ Mapa & Pamiatky", "🤖 AI Skener", "👤 Profil"]
        )
        st.write("##")
        if st.button("Odhlásiť sa"):
            st.session_state.step = "login"
            st.rerun()

    # --- OBSAH ---
    if stranka == "📸 Komunitný Feed":
        st.title("📸 Komunita")
        st.markdown('<div class="omni-card"><b>Maroš Svetobežník</b> • Nové Zámky<br><br><img src="https://images.unsplash.com/photo-1555392859-d6e23a7f48b3?q=80&w=600" style="width:100%; border-radius:10px;"><br><br>Dnes testujeme biely dizajn!</div>', unsafe_allow_html=True)

    elif stranka == "🗺️ Mapa & Pamiatky":
        st.title("🗺️ Okolie")
        moje_lat, moje_lon = 47.985, 18.161
        pamiatky = [
            {"meno": "Kalvária NZ", "lat": 47.981, "lon": 18.160},
            {"meno": "Lesopark Berek", "lat": 47.970, "lon": 18.145}
        ]
        for p in pamiatky:
            d = vypocitaj_vzdialenost(moje_lat, moje_lon, p['lat'], p['lon'])
            st.markdown(f'<div class="omni-card"><h3>🏛️ {p['meno']}</h3>Vzdialenosť: <b>{d} km</b></div>', unsafe_allow_html=True)

    elif stranka == "🤖 AI Skener":
        st.title("🤖 AI Skener")
        st.camera_input("Odfoťte menu")
        st.info("AI analýza je pripravená.")

    elif stranka == "👤 Profil":
        st.title("👤 Profil")
        st.markdown('<div class="omni-card"><h3>Ocko Cestovateľ</h3>Level: Zlatý prieskumník</div>', unsafe_allow_html=True)
