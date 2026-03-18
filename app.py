import streamlit as st
import base64
import time
import pandas as pd # Pre simuláciu dát

# --- KONFIGURÁCIA STRÁNKY ---
st.set_page_config(page_title="OmniTravel Community", layout="wide", initial_sidebar_state="expanded")

# --- SESSION STATE (PAMÄŤ) ---
if 'step' not in st.session_state: st.session_state.step = "login"
if 'user_posts' not in st.session_state: st.session_state.user_posts = [] # Tu budeme ukladať (dočasne) ockove príspevky

# =========================================================================
# 🌑 STYLE 1: ÚVOD (GLOBES) - Ponechané
# =========================================================================
AUTH_STYLE = """
<style>
    .stApp { background-color: #000000; color: #FFFFFF; font-family: sans-serif; }
    @keyframes globeMove { from { transform: translateY(110vh); opacity: 0; } to { transform: translateY(-10vh); opacity: 0; } }
    .globe { position: fixed; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #D8BFD8, #8A2BE2); z-index: 0; animation: globeMove 15s linear infinite; }
    .auth-card { background: rgba(10, 10, 10, 0.85); border: 1px solid #BC8CF2; padding: 50px; border-radius: 30px; text-align: center; max-width: 500px; margin: auto; position: relative; z-index: 10; }
    div.stButton > button { background: linear-gradient(45deg, #8A2BE2, #9400D3); color: white; border-radius: 30px; font-weight: bold; width: 100%; transition: 0.3s; }
</style>
"""

# =========================================================================
# 💎 STYLE 2: HLAVNÁ APPKA (PURE BLACK, LUXURY FONT, SOCIAL FEED)
# =========================================================================
MAIN_STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500;700&display=swap');
    .stApp, [data-testid="stSidebar"] { background-color: #000000 !important; color: #FFFFFF !important; font-family: 'Quicksand', sans-serif !important; font-weight: 300; }
    h1, h2, h3 { color: #BC8CF2; font-weight: 700; text-shadow: 0 0 15px rgba(188, 140, 242, 0.4); }
    
    /* 📸 SOCIAL FEED CARD (Instagram Style) */
    .feed-card {
        background: rgba(20, 20, 20, 0.9);
        border: 1px solid rgba(138, 43, 226, 0.3);
        border-radius: 15px; margin-bottom: 25px; overflow: hidden;
        transition: 0.3s;
    }
    .feed-card:hover { border-color: #BC8CF2; box-shadow: 0 0 15px rgba(138, 43, 226, 0.3); }
    .feed-header { padding: 15px; display: flex; align-items: center; border-bottom: 1px solid #222; }
    .feed-avatar { width: 40px; height: 40px; border-radius: 50%; background: #333; margin-right: 12px; border: 2px solid #8A2BE2; }
    .feed-image { width: 100%; height: 300px; object-fit: cover; }
    .feed-content { padding: 15px; }
    .feed-actions { padding: 10px 15px; border-top: 1px solid #222; color: #8A2BE2; font-size: 1.2em; }

    /* Neon Tlačidlá */
    div.stButton > button { background: transparent; border: 1px solid #BC8CF2; color: #BC8CF2; border-radius: 20px; transition: 0.3s; }
    div.stButton > button:hover { background: rgba(138, 43, 226, 0.1); box-shadow: 0 0 15px #BC8CF2; }
</style>
"""

# =========================================================================
# FUNKCIE PRE PRECHOD
# =========================================================================
def go_to_promo(): st.session_state.step = "promo"
def go_to_app(): st.session_state.step = "app"

# =========================================================================
# 1 & 2: ONBOARDING (LOGIN & PROMO) - Ponechané
# =========================================================================
if st.session_state.step == "login":
    st.markdown(AUTH_STYLE, unsafe_allow_html=True)
    st.markdown('<div class="globe" style="left: 10%; width: 15px; height: 15px; animation-duration: 20s;"></div>', unsafe_allow_html=True)
    st.write("##")
    with st.container():
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.image("https://img.icons8.com/fluency/96/000000/globe-earth.png", width=100)
        st.title("OmniTravel Community")
        st.write("Cestuj. Foť. Zdieľaj s AI sprievodcom.")
        st.button("✨ Vstúpiť do komunity", on_click=go_to_promo)
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == "promo":
    st.markdown(AUTH_STYLE, unsafe_allow_html=True)
    st.write("##")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown('<div class="auth-card" style="background: linear-gradient(135deg, #101010 0%, #3a0066 100%);">', unsafe_allow_html=True)
        st.title("💎 OmniTravel PRO")
        st.write("Aktivuj plný potenciál")
        st.markdown("✅ Neobmedzený OmniVision<br>✅ Offline Google Mapy<br>✅ Komunitné Eventy", unsafe_allow_html=True)
        st.button("🚀 AKTIVOVAŤ PRO (0€)", on_click=go_to_app)
        if st.button("Možno neskôr"): go_to_app()
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 3. HLAVNÁ APLIKÁCIA (OminTravel Community Edition)
# =========================================================================
elif st.session_state.step == "app":
    st.markdown(MAIN_STYLE, unsafe_allow_html=True)
    
    with st.sidebar:
        st.markdown('<h2>💜 OmniTravel</h2>', unsafe_allow_html=True)
        # NOVÁ NAVIGÁCIA
        stranka = st.radio("NAVIGÁCIA", ["📸 Komunitný Feed", "🗺️ Mapa a Pamiatky", "🤖 AI Skener Menu", "👤 Môj Profil"])
        st.markdown("---")
        if st.button("Odhlásiť sa"):
            st.session_state.step = "login"
            st.rerun()

    # --- A. KOMUNITNÝ FEED (SOCIÁLNA SIEŤ) ---
    if stranka == "📸 Komunitný Feed":
        st.title("📸 Objavuj svet očami iných")
        
        # Sekcia na pridanie príspevku
        with st.expander("➕ Pridať nový zážitok"):
            col_add1, col_add2 = st.columns([1, 2])
            with col_add1:
                st.camera_input("Odfoť", key="new_post_photo")
            with col_add2:
                st.text_area("Popis", placeholder="Kde si a čo odporúčaš?")
                st.slider("Hodnotenie", 1, 5, 5)
                if st.button("Uverejniť"):
                    st.success("Príspevok bol pridaný do tvojho profilu! (Simulácia)")
        
        st.write("---")
        
        # SIMULÁCIA FEEDU (Zobrazíme 2 príspevky)
        col_feed1, col_feed2, col_feed3 = st.columns([1,2,1]) # Vycentrujeme feed
        with col_feed2:
            # PRÍSPEVOK 1 (Reštaurácia)
            st.markdown(f"""
            <div class="feed-card">
                <div class="feed-header">
                    <div class="feed-avatar"></div>
                    <div><b>Zuzka Cestovateľka</b><br><small>Nové Zámky • Pred 2h</small></div>
                </div>
                <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=600" class="feed-image">
                <div class="feed-content">
                    <h4>Najlepšia káva v NZ! ☕️</h4>
                    <p>AI Skener mi super preložil menu. Odporúčam ich cappuccino. ⭐⭐⭐⭐⭐</p>
                </div>
                <div class="feed-actions">❤️ 45  💬 3  🗺️ Ukázať na mape</div>
            </div>
            """, unsafe_allow_html=True)
            
            # PRÍSPEVOK 2 (Pamiatka)
            st.markdown(f"""
            <div class="feed-card">
                <div class="feed-header">
                    <div class="feed-avatar" style="background: #555;"></div>
                    <div><b>Maroš Svetobežník</b><br><small>Kalvária NZ • Včera</small></div>
                </div>
                <img src="https://images.unsplash.com/photo-1541963463532-d68292c34b19?q=80&w=600" class="feed-image">
                <div class="feed-content">
                    <h4>Krásna prechádzka na Kalváriu 🏰</h4>
                    <p>Super výhľad na mesto. Appka mi našla túto pamiatku cez GPS.</p>
                </div>
                <div class="feed-actions">❤️ 120  💬 15  🗺️ Ukázať na mape</div>
            </div>
            """, unsafe_allow_html=True)

    # --- B. MAPA A PAMIATKY (GOOGLE MAPS PROTOTYP) ---
    elif stranka == "🗺️ Mapa a Pamiatky":
        st.title("🗺️ Mapa a Pamiatky v okolí")
        st.markdown('<div class="result-card"><h3>📍 Tvoja Poloha: Nové Zámky</h3></div>', unsafe_allow_html=True)
        
        # SIMULÁCIA GOOGLE MAPY
        # V roku 2026 namiesto interaktívnej mapy vložíme STATICKÝ OBRÁZOK mapy, aby sme ušetrili API náklady.
        st.markdown(f"""
        <div class="result-card">
            <h3>Google Maps Prototyp</h3>
            <p>Hľadám trasu k najbližšej pamiatke...</p>
            <img src="https://maps.googleapis.com/maps/api/staticmap?center=Nove+Zamky,Slovakia&zoom=14&size=800x400&markers=color:purple|label:P|47.985,18.161&key=YOUR_API_KEY" style="width: 100%; border-radius: 10px; border: 1px solid #BC8CF2;">
            <p><br>🏰 <b>Kalvária NZ</b> je vzdialená 800m (cca 10 minút pešo).</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.button("📍 Zistiť presnú GPS polohu (Simulácia)")

    # --- C. AI SKENER MENU (Ponechané) ---
    elif stranka == "🤖 AI Skener Menu":
        st.title("🤖 AI Skener Menu")
        st.info("Hľadám voľný AI model...")
        col_scan1, col_scan2 = st.columns(2)
        with col_scan1: st.button("📷 Fotoaparát", use_container_width=True)
        with col_scan2: st.button("📂 Galéria", use_container_width=True)
        st.markdown('<div class="result-card"><h3>Výsledok Analýzy</h3><p>Tu sa zobrazí preklad a rozbor menu.</p></div>', unsafe_allow_html=True)

    # --- D. MÔJ PROFIL (SOCIÁLNY PROFIL) ---
    elif stranka == "👤 Môj Profil":
        st.title("👤 Môj Cestovateľský Profil")
        col_prof1, col_prof2, col_prof3 = st.columns([1,2,1])
        with col_prof2:
            st.markdown(f"""
            <div class="feed-card">
                <div class="feed-header">
                    <div class="feed-avatar"></div>
                    <div><b>Môj Ocko - Cestovateľ</b><br><small>Nové Zámky • Úroveň 1</small></div>
                </div>
                <div class="feed-content">
                    <p>VP Body: 250 / 1000</p>
                    <p>Príspevky: 0 | Naskenované Menu: 5 | Pamiatky: 2</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.progress(25)
            st.button("💎 Upgrade na PRO pre neobmedzené funkcie")
