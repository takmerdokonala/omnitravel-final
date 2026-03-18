import streamlit as st
import math

# --- KONFIGURÁCIA STRÁNKY ---
# 'collapsed' zabezpečí, že na začiatku uvidíš len tri čiarky (hamburger)
st.set_page_config(
    page_title="OmniTravel White Edition", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- SESSION STATE ---
if 'step' not in st.session_state: st.session_state.step = "login"

# --- FUNKCIA NA VÝPOČET VZDIALENOSTI ---
def vypocitaj_vzdialenost(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 2)

# =========================================================================
# ⚪️ PURE WHITE & CLEAN SIDEBAR STYLE (CSS)
# =========================================================================
WHITE_STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500;700&display=swap');

    .stApp { 
        background-color: #FFFFFF !important; 
        color: #000000 !important; 
        font-family: 'Quicksand', sans-serif !important; 
    }
    
    /* Úprava bočného panelu pre maximálnu čistotu */
    [data-testid="stSidebar"] { 
        background-color: #FFFFFF !important; 
        border-right: 1px solid #F0F0F0;
    }

    /* Skrytie predvolených ovládacích prvkov selectboxu, aby to vyzeralo ako čistý text */
    div[data-testid="stSidebar"] .stSelectbox {
        margin-top: 20px;
    }

    /* Nadpisy a karty */
    h1, h2, h3 { color: #8A2BE2; font-weight: 700; }
    
    .result-card, .feed-card {
        background: #FFFFFF;
        border: 1px solid #F0F0F0;
        padding: 20px; border-radius: 15px; margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }

    /* Štýl pre navigačné položky v menu */
    .nav-item {
        padding: 10px 0;
        border-bottom: 1px solid #F9F9F9;
        color: #555;
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
        st.write("Čistý dizajn pre vaše cesty.")
        if st.button("✨ Vstúpiť do aplikácie"): 
            st.session_state.step = "app"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 2. HLAVNÁ APLIKÁCIA (S HAMBURGER MENU)
# =========================================================================
elif st.session_state.step == "app":
    st.markdown(WHITE_STYLE, unsafe_allow_html=True)
    
    # --- BOČNÉ MENU (SIDEBAR) ---
    with st.sidebar:
        st.markdown('<h2 style="margin-bottom:0;">💜 OmniTravel</h2>', unsafe_allow_html=True)
        st.write("---")
        
        # Namiesto selectboxu použijeme radio button, ktorý vyzerá ako zoznam
        stranka = st.radio(
            "HLAVNÉ MENU",
            ["📸 Komunitný Feed", "🗺️ Mapa & Pamiatky", "🤖 AI Skener", "👤 Profil"],
            index=0
        )
        
        st.write("##")
        if st.button("Odhlásiť sa"):
            st.session_state.step = "login"
            st.rerun()

    # --- OBSAH STRÁNOK ---
    if stranka == "📸 Komunitný Feed":
        st.title("📸 Komunita")
        st.markdown("""
        <div class="feed-card">
            <p><b>Zuzka C.</b> • Nové Zámky</p>
            <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=600" style="width:100%; border-radius:10px;">
            <p><br>Skvelý tip na kaviareň v centre!</p>
        </div>
        """, unsafe_allow_html=True)

    elif stranka == "🗺️ Mapa & Pamiatky":
        st.title("🗺️ Okolie")
        # Súradnice (Nové Zámky)
        moje_lat, moje_lon = 47.985, 18.161
        pamiatky = [
            {"meno": "Kalvária NZ", "lat": 47.981, "lon": 18.160, "dist": 0},
            {"meno": "Lesopark Berek", "lat": 47.970, "lon": 18.145, "dist": 0}
        ]
        
        for p in pamiatky:
            d = vypocitaj_vzdialenost(moje_lat, moje_lon, p['lat'], p['lon'])
            st.markdown(f"""
            <div class="result-card">
                <h3>🏛️ {p['meno']}</h3>
                <p>Vzdialenosť: <b>{d} km</b></p>
            </div>
            """, unsafe_allow_html=True)

    elif stranka == "🤖 AI Skener":
        st.title("🤖 Skener")
        st.camera_input("Odfoť menu")
        st.success("AI pripravená na analýzu...")

    elif stranka == "👤 Profil":
        st.title("👤 Profil")
        st.write("Meno: Ocko Cestovateľ")
        st.progress(40)
