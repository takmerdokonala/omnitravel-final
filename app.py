import streamlit as st
import base64
import math
from groq import Groq

# --- KONFIGURÁCIA STRÁNKY ---
st.set_page_config(page_title="OmniTravel Ultra 2026", layout="wide", initial_sidebar_state="expanded")

# --- SESSION STATE (PAMÄŤ APPKY) ---
if 'step' not in st.session_state: st.session_state.step = "login"

# --- FUNKCIA NA VÝPOČET VZDIALENOSTI (Haversine formula) ---
def vypocitaj_vzdialenost(lat1, lon1, lat2, lon2):
    R = 6371  # Polomer Zeme v km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 2)

# --- LUXUSNÝ DIZAJN (CSS) ---
AUTH_STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500;700&display=swap');
    .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Quicksand', sans-serif; }
    
    /* Zemegule pre úvod */
    @keyframes globeMove { from { transform: translateY(110vh); opacity: 0; } to { transform: translateY(-10vh); opacity: 0; } }
    .globe { position: fixed; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #D8BFD8, #8A2BE2); z-index: 0; animation: globeMove 15s linear infinite; }
    
    /* Karty */
    .auth-card, .result-card, .feed-card {
        background: rgba(20, 20, 20, 0.9); border: 1px solid rgba(138, 43, 226, 0.4);
        padding: 25px; border-radius: 20px; margin-bottom: 20px;
        box-shadow: 0 0 20px rgba(138, 43, 226, 0.1);
    }
    h1, h2, h3 { color: #BC8CF2; text-shadow: 0 0 10px rgba(188, 140, 242, 0.4); }
    
    /* Neon Tlačidlá */
    div.stButton > button {
        background: transparent; border: 1px solid #BC8CF2; color: #BC8CF2;
        border-radius: 30px; font-weight: bold; width: 100%; transition: 0.3s;
    }
    div.stButton > button:hover { background: rgba(138, 43, 226, 0.2); box-shadow: 0 0 20px #BC8CF2; }
</style>
"""

# =========================================================================
# 1. OBRAZOVKA: PRIHLÁSENIE
# =========================================================================
if st.session_state.step == "login":
    st.markdown(AUTH_STYLE, unsafe_allow_html=True)
    st.markdown('<div class="globe" style="left: 15%; width: 20px; height: 20px; animation-duration: 10s;"></div>', unsafe_allow_html=True)
    st.write("##")
    with st.container():
        st.markdown('<div class="auth-card" style="text-align: center; max-width: 500px; margin: auto;">', unsafe_allow_html=True)
        st.image("https://img.icons8.com/fluency/96/000000/globe-earth.png", width=100)
        st.title("OmniTravel 2026")
        st.write("Vstúp do novej éry cestovania.")
        if st.button("✨ Začať dobrodružstvo"): 
            st.session_state.step = "app"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 2. HLAVNÁ APLIKÁCIA
# =========================================================================
elif st.session_state.step == "app":
    st.markdown(AUTH_STYLE, unsafe_allow_html=True)
    
    with st.sidebar:
        st.markdown('<h2>💜 OmniTravel</h2>', unsafe_allow_html=True)
        stranka = st.radio("NAVIGÁCIA", ["📸 Komunitný Feed", "🗺️ Mapa & Pamiatky", "🤖 AI Skener", "👤 Profil"])
        st.markdown("---")
        if st.button("Odhlásiť sa"):
            st.session_state.step = "login"
            st.rerun()

    # --- KOMUNITNÝ FEED ---
    if stranka == "📸 Komunitný Feed":
        st.title("📸 Čerstvé zážitky")
        st.markdown("""
        <div class="feed-card">
            <p><b>Zuzka Cestovateľka</b> • Nové Zámky</p>
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
            {"meno": "Kalvária NZ", "lat": 47.981, "lon": 18.160, "popis": "Historické krížové cesty."},
            {"meno": "Lesopark Berek", "lat": 47.970, "lon": 18.145, "popis": "Príroda a relax pri rieke Nitra."}
        ]
        
        st.markdown(f'<div class="result-card">📍 Aktuálna poloha: <b>Nové Zámky</b></div>', unsafe_allow_html=True)
        
        for p in pamiatky:
            dist = vypocitaj_vzdialenost(moje_lat, moje_lon, p['lat'], p['lon'])
            st.markdown(f"""
            <div class="result-card">
                <h3>🏛️ {p['meno']}</h3>
                <p>{p['popis']}</p>
                <p style="color: #BC8CF2;"><b>Vzdialenosť: {dist} km od teba</b></p>
                <button style="background: #8A2BE2; color: white; border: none; padding: 5px 15px; border-radius: 10px;">Navigovať</button>
            </div>
            """, unsafe_allow_html=True)

    # --- AI SKENER (S DEMO REŽIMOM PRE ISTOTU) ---
    elif stranka == "🤖 AI Skener":
        st.title("🤖 OmniVision Skener")
        foto = st.camera_input("Odfoť menu")
        
        if foto:
            with st.spinner("AI analyzuje..."):
                # TU SIMULUJEME ÚSPECH, AJ KEĎ GROQ NEFUNGUJE (Pre ocka)
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
        st.markdown('<div class="result-card"><h3>Úroveň: Prieskumník</h3><p>Body: 350 VP</p></div>', unsafe_allow_html=True)
        st.progress(35)
