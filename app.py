import streamlit as st
import base64
import math

# --- KONFIGURÁCIA STRÁNKY ---
# initial_sidebar_state="expanded" zabezpečí, že menu bude na začiatku vysunuté
st.set_page_config(page_title="OmniTravel White Edition", layout="wide", initial_sidebar_state="expanded")

# --- SESSION STATE (PAMÄŤ APPKY) ---
if 'step' not in st.session_state: st.session_state.step = "login"

# --- FUNKCIA NA VÝPOČET VZDIALENOSTI ---
def vypocitaj_vzdialenost(lat1, lon1, lat2, lon2):
    R = 6371  # Polomer Zeme v km
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
    /* 1. Import Luxusného Fontu (Quicksand) */
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500;700&display=swap');

    /* 2. Snehobiele pozadie a čierny font pre celú appku */
    .stApp { 
        background-color: #FFFFFF !important; 
        color: #000000 !important; 
        font-family: 'Quicksand', sans-serif !important; 
        font-weight: 300; 
    }
    
    /* 3. Biele Tvary pre Intro (Zemegule sú preč) */
    @keyframes shapeMove { from { transform: translateY(110vh); opacity: 0; } to { transform: translateY(-10vh); opacity: 0.5; } }
    .shape { position: fixed; border-radius: 50%; background: #F0F0F0; z-index: 0; animation: shapeMove 15s linear infinite; }

    /* 4. Nadpisy (H1, H2, H3) - Fialový Glow na bielej */
    h1, h2, h3 { 
        color: #8A2BE2; 
        font-weight: 700; 
        text-shadow: 0 0 10px rgba(138, 43, 226, 0.3); 
    }
    
    /* 5. Minimalistické Biele Karty s Fialovým Glow */
    .auth-card, .result-card, .feed-card {
        background: #FFFFFF;
        border: 1px solid rgba(138, 43, 226, 0.2);
        padding: 30px; border-radius: 20px; margin-bottom: 25px;
        box-shadow: 0 0 15px rgba(138, 43, 226, 0.05);
    }
    
    /* 6. Vylepšené Fialové Neon Tlačidlá Streamlit */
    div.stButton > button {
        background: transparent;
        border: 1px solid #8A2BE2; 
        color: #8A2BE2; border-radius: 20px;
        font-weight: 500; transition: 0.3s;
        box-shadow: 0 0 10px rgba(138, 43, 226, 0.1);
    }
    div.stButton > button:hover { 
        background: rgba(138, 43, 226, 0.05);
        box-shadow: 0 0 20px rgba(138, 43, 226, 0.4); 
        transform: translateY(-2px);
    }
    
    /* 7. Uprataný Sidebar - Čistý biely */
    [data-testid="stSidebar"] { 
        background-color: #FFFFFF !important; 
        border-right: 1px solid #F0F0F0; 
    }
    [data-testid="stSidebarNav"] { background: transparent; }
    [data-testid="stSidebarNavSeparator"] { background: transparent; }
</style>
"""

# =========================================================================
# 1. OBRAZOVKA: PRIHLÁSENIE (Uplatníme WHITE_STYLE)
# =========================================================================
if st.session_state.step == "login":
    st.markdown(WHITE_STYLE, unsafe_allow_html=True)
    
    # Generovanie Bieleho tvaru
    st.markdown("""
    <div class="shape" style="left: 10%; width: 25px; height: 25px; animation-duration: 15s;"></div>
    <div class="shape" style="left: 80%; width: 15px; height: 15px; animation-duration: 25s; animation-delay: 1s;"></div>
    """, unsafe_allow_html=True)

    st.write("##")
    st.write("##")
    with st.container():
        st.markdown('<div class="auth-card" style="text-align: center; max-width: 500px; margin: auto;">', unsafe_allow_html=True)
        # Logo OmniTravel - Fialová zemeguľa pre biele pozadie
        st.image("https://img.icons8.com/fluency/96/000000/globe-earth.png", width=100)
        st.title("OmniTravel 2026")
        st.write("Vstúp do novej éry čistého cestovania.")
        
        # Simulačné tlačidlá
        if st.button("✨ Začať bezpečne"): 
            st.session_state.step = "app"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 2. HLAVNÁ APLIKÁCIA (Uplatníme WHITE_STYLE - Čistá Biela)
# =========================================================================
elif st.session_state.step == "app":
    st.markdown(WHITE_STYLE, unsafe_allow_html=True)
    
    # --- BOČNÉ MENU (SIDEBAR) ---
    with st.sidebar:
        # Tieto tri čiarky Streamlit generuje automaticky na mobile
        # My sem len vypíšeme navigáciu, ktorá bude pod nimi.
        st.markdown('<h2 style="color: #8A2BE2;">💜 OmniTravel</h2>', unsafe_allow_html=True)
        st.write("###")
        # Tu je pekne vypísaný zoznam navigácie
        stranka = st.selectbox(
            "NAVIGÁCIA",
            ["📸 Komunitný Feed", "🗺️ Mapa & Pamiatky", "🤖 AI Skener", "👤 Profil"]
        )
        st.write("###")
        if st.button("Odhlásiť sa"):
            st.session_state.step = "login"
            st.rerun()

    # --- KOMUNITNÝ FEED (BIELA VERZIA) ---
    if stranka == "📸 Komunitný Feed":
        st.title("📸 Čerstvé zážitky")
        st.markdown("""
        <div class="feed-card">
            <p><b>Zuzka Cestovateľka</b> • Nové Zámky • Pred 2h</p>
            <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=600" style="width:100%; border-radius:10px;">
            <p><br>Dnes úžasná káva v centre! AI Skener mi hneď preložil, čo je "Flat White". ❤️ 45</p>
        </div>
        """, unsafe_allow_html=True)

    # --- MAPA & PAMIATKY (S VÝPOČTOM VZDIALENOSTI) ---
    elif stranka == "🗺️ Mapa & Pamiatky":
        st.title("🗺️ Čo je v tvojom okolí?")
        
        # Súradnice používateľa (Nové Zámky centrum)
        moje_lat, moje_lon = 47.985, 18.161
        
        # Súradnice pamiatok
        pamiatky = [
            {"meno": "Kalvária NZ", "lat": 47.981, "lon": 18.160, "popis": "Historické krížové cesty Nových Zámkov."},
            {"meno": "Lesopark Berek", "lat": 47.970, "lon": 18.145, "popis": "Príroda a relax pri rieke Nitra."}
        ]
        
        st.markdown(f'<div class="result-card">📍 Tvoja aktuálna poloha: <b>Nové Zámky</b></div>', unsafe_allow_html=True)
        
        for p in pamiatky:
            dist = vypocitaj_vzdialenost(moje_lat, moje_lon, p['lat'], p['lon'])
            st.markdown(f"""
            <div class="result-card">
                <h3>🏛️ {p['meno']}</h3>
                <p>{p['popis']}</p>
                <p style="color: #8A2BE2;"><b>Vzdialenosť: {dist} km od teba</b></p>
                <button style="background: transparent; border: 1px solid #8A2BE2; color: #8A2BE2; padding: 5px 15px; border-radius: 10px;">Navigovať</button>
            </div>
            """, unsafe_allow_html=True)

    # --- AI SKENER (S DEMO REŽIMOM PRE ISTOTU) ---
    elif stranka == "🤖 AI Skener":
        st.title("🤖 OmniVision Skener")
        st.camera_input("Odfoť menu")
        
        # TU SIMULUJEME ÚSPECH (Prezentácia pre ocka)
        st.markdown("""
        <div class="result-card">
            <h3>✅ Preklad Menu (AI Analýza):</h3>
            <p><b>Polievka dňa:</b> Paradajková so syrom (2.50€)</p>
            <p><b>Hlavné jedlo:</b> Kuracie prsia na bylinkách (8.90€)</p>
            <p><i>AI Tip: Toto jedlo je dnes najobľúbenejšie v komunite!</i></p>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

    # --- PROFIL ---
    elif stranka == "👤 Profil":
        st.title("👤 Tvoj Profil")
        st.markdown('<div class="result-card"><h3>Úroveň: Prieskumník</h3><p>VP Body: 350 / 1000</p></div>', unsafe_allow_html=True)
        st.progress(35)
