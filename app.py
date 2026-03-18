import streamlit as st
import math

# --- 1. KONFIGURÁCIA STRÁNKY ---
st.set_page_config(
    page_title="OmniTravel White Edition", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. SESSION STATE (PAMÄŤ) ---
if 'step' not in st.session_state: st.session_state.step = "login"

# --- 3. FUNKCIA NA VÝPOČET VZDIALENOSTI ---
def vypocitaj_vzdialenost(lat1, lon1, lat2, lon2):
    R = 6371 # Polomer Zeme v km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 2)

# --- 4. ULTRA CLEAN WHITE STYLE (CSS) ---
STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500;700&display=swap');

    /* Globálne nastavenia */
    .stApp { 
        background-color: #FFFFFF !important; 
        color: #1A1A1A !important; 
        font-family: 'Quicksand', sans-serif !important; 
    }
    
    /* FIX: Viditeľnosť textu v bočnom menu */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #F0F0F0;
    }
    [data-testid="stSidebar"] .st-emotion-cache-1647spv, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: #4B0082 !important; /* Tmavofialová pre kontrast */
        font-weight: 600 !important;
        font-size: 1.05rem !important;
    }

    /* Nadpisy a karty */
    h1, h2, h3 { color: #8A2BE2 !important; font-weight: 700; }
    
    .card {
        background: #FFFFFF;
        border: 1px solid #F0F0F0;
        padding: 20px; border-radius: 15px; margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    }

    /* Tlačidlá */
    div.stButton > button {
        background-color: #FFFFFF;
        border: 1px solid #8A2BE2;
        color: #8A2BE2;
        border-radius: 20px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #F8F0FF;
        box-shadow: 0 0 10px rgba(138, 43, 226, 0.2);
    }
</style>
"""

# =========================================================================
# 5. LOGIKA STRÁNOK
# =========================================================================

# --- A. LOGIN ---
if st.session_state.step == "login":
    st.markdown(STYLE, unsafe_allow_html=True)
    st.write("##")
    st.markdown('<div style="text-align: center; padding-top: 50px;">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/fluency/96/000000/globe-earth.png", width=100)
    st.title("OmniTravel 2026")
    st.write("Váš inteligentný sprievodca v čistom dizajne.")
    if st.button("✨ Vstúpiť"): 
        st.session_state.step = "app"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- B. HLAVNÁ APPKA ---
elif st.session_state.step == "app":
    st.markdown(STYLE, unsafe_allow_html=True)
    
    # SIDEBAR S HAMBURGER MENU
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
        st.markdown("""
        <div class="card">
            <p><b>Maroš Svetobežník</b> • Nové Zámky</p>
            <img src="https://images.unsplash.com/photo-1555392859-d6e23a7f48b3?q=80&w=600" style="width:100%; border-radius:10px;">
            <p><br>Dnes som vyskúšal ten nový AI skener v reštaurácii. Funguje to parádne! 👏</p>
        </div>
        """, unsafe_allow_html=True)

    elif stranka == "🗺️ Mapa & Pamiatky":
        st.title("🗺️ Okolie")
        # Centrum NZ
        moje_lat, moje_lon = 47.985, 18.161
        pamiatky = [
            {"meno": "Kalvária NZ", "lat": 47.981, "lon": 18.160},
            {"meno": "Lesopark Berek", "lat": 47.970, "lon": 18.145},
            {"meno": "Termálne kúpalisko", "lat": 47.992, "lon": 18.175}
        ]
        
        for p in pamiatky:
            d = vypocitaj_vzdialenost(moje_lat, moje_lon, p['lat'], p['lon'])
            st.markdown(f"""
            <div class="card">
                <h3>🏛️ {p['meno']}</h3>
                <p>Vzdialenosť: <b>{d} km od teba</b></p>
            </div>
            """, unsafe_allow_html=True)

    elif stranka == "🤖 AI Skener":
        st.title("🤖 AI Skener")
        st.camera_input("Odfoťte dokument alebo menu")
        # Simulácia pre ocka
        st.info("Pripravené na skenovanie...")

    elif stranka == "👤 Profil":
        st.title("👤 Profil")
        st.markdown(f"""
        <div class="card">
            <h3>Ocko Cestovateľ</h3>
            <p>Úroveň: <b>Zlatý prieskumník</b></p>
            <p>Počet odfotených menu: 12</p>
        </div>
        """, unsafe_allow_html=True)
    /* Nadpisy */
    h1, h2, h3 { color: #8A2BE2 !important; font-weight: 700; }
    
    .result-card, .feed-card {
        background: #FFFFFF;
        border: 1px solid #EEEEEE;
        padding: 20px; border-radius: 15px; margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        color: #1A1A1A !important;
    }

    /* Tlačidlo Odhlásiť */
    div.stButton > button {
        background-color: #F8F0FF;
        border: 1px solid #8A2BE2;
        color: #8A2BE2;
        border-radius: 12px;
    }
</style>
"""

# =========================================================================
# 1. OBRAZOVKA: PRIHLÁSENIE
# =========================================================================
if st.session_state.step == "login":
    st.markdown(WHITE_STYLE, unsafe_allow_html=True)
    st.write("##")
    with st.container():
        st.markdown('<div style="text-align: center; padding: 50px;">', unsafe_allow_html=True)
        st.image("https://img.icons8.com/fluency/96/000000/globe-earth.png", width=100)
        st.title("OmniTravel 2026")
        st.write("Čistý, moderný dizajn pre ocka.")
        if st.button("✨ Vstúpiť do aplikácie"): 
            st.session_state.step = "app"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 2. HLAVNÁ APLIKÁCIA
# =========================================================================
elif st.session_state.step == "app":
    st.markdown(WHITE_STYLE, unsafe_allow_html=True)
    
    # --- BOČNÉ MENU (SIDEBAR) ---
    with st.sidebar:
        st.markdown('<h2>💜 OmniTravel</h2>', unsafe_allow_html=True)
        st.write("---")
        
        # HLAVNÉ MENU - Teraz by malo byť krásne vidieť text
        stranka = st.radio(
            "NAVIGÁCIA",
            ["📸 Komunitný Feed", "🗺️ Mapa & Pamiatky", "🤖 AI Skener", "👤 Profil"],
            index=0
        )
        
        st.write("##")
        if st.button("Odhlásiť sa"):
            st.session_state.step = "login"
            st.rerun()

    # --- OBSAH ---
    if stranka == "📸 Komunitný Feed":
        st.title("📸 Komunita")
        st.markdown("""
        <div class="feed-card">
            <p><b>Zuzka Cestovateľka</b> • Nové Zámky</p>
            <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=600" style="width:100%; border-radius:10px;">
            <p><br>Skúšam nový biely dizajn! Text je konečne vidieť. ✨</p>
        </div>
        """, unsafe_allow_html=True)

    elif stranka == "🗺️ Mapa & Pamiatky":
        st.title("🗺️ Okolie")
        moje_lat, moje_lon = 47.985, 18.161
        pamiatky = [
            {"meno": "Kalvária NZ", "lat": 47.981, "lon": 18.160},
            {"meno": "Lesopark Berek", "lat": 47.970, "lon": 18.145}
        ]
        
        for p in pamiatky:
            d = vypocitaj_vzdialenost(moje_lat, moje_lon, p['lat'], p['lon'])
            st.markdown(f"""
            <div class="result-card">
                <h3>🏛️ {p['meno']}</h3>
                <p>Vzdialenosť: <b>{d} km od teba</b></p>
            </div>
            """, unsafe_allow_html=True)

    elif stranka == "🤖 AI Skener":
        st.title("🤖 Skener")
        st.camera_input("Odfoť menu")
        st.markdown('<div class="result-card">Pripravený na fotenie.</div>', unsafe_allow_html=True)

    elif stranka == "👤 Profil":
        st.title("👤 Profil")
        st.markdown('<div class="result-card"><b>Meno:</b> Ocko Cestovateľ<br><b>Level:</b> 1</div>', unsafe_allow_html=True)
