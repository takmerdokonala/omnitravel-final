import streamlit as st
import base64
import time

# --- KONFIGURÁCIA STRÁNKY ---
st.set_page_config(page_title="OmniTravel Ultra 2026", layout="wide", initial_sidebar_state="collapsed")

# --- INICIALIZÁCIA STAVU (SESSION STATE) ---
if 'step' not in st.session_state:
    st.session_state.step = "login" # Kroky: login -> promo -> app

# =========================================================================
# 🌑 STYLE 1: ÚVOD (DEEP BLACK & GLOSSY PURPLE GLOBES)
# =========================================================================
AUTH_STYLE = """
<style>
    .stApp { background-color: #000000; color: #FFFFFF; font-family: sans-serif; }
    
    @keyframes globeMove {
        from { transform: translateY(110vh) translateX(0) rotate(0deg) scale(0.8); opacity: 0; }
        10% { opacity: 0.7; } 50% { opacity: 1; } 90% { opacity: 0.7; }
        to { transform: translateY(-10vh) translateX(20px) rotate(360deg) scale(1.2); opacity: 0; }
    }
    .globe {
        position: fixed; border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, #D8BFD8, #8A2BE2, #4B0082);
        box-shadow: 0 0 20px #9400D3, inset 0 0 10px rgba(255, 255, 255, 0.4);
        z-index: 0; animation: globeMove 15s linear infinite;
    }
    .auth-card {
        background: rgba(10, 10, 10, 0.85); backdrop-filter: blur(5px);
        border: 1px solid #BC8CF2; padding: 50px; border-radius: 30px;
        text-align: center; max-width: 500px; margin: auto;
        box-shadow: 0 0 30px rgba(138, 43, 226, 0.3); position: relative; z-index: 10;
    }
    div.stButton > button {
        background: linear-gradient(45deg, #8A2BE2, #9400D3);
        color: white; border: none; border-radius: 30px;
        font-weight: bold; width: 100%; transition: 0.3s;
        box-shadow: 0 0 15px rgba(138, 43, 226, 0.5);
    }
    div.stButton > button:hover { transform: scale(1.03); box-shadow: 0 0 25px #8A2BE2; }
    div.stTextInput input {
        background-color: rgba(30, 30, 30, 0.8); border: 1px solid #BC8CF2;
        color: white; border-radius: 8px;
    }
</style>
"""

# =========================================================================
# 💎 STYLE 2: HLAVNÁ APPKA (PURE BLACK & LUXURY NEON)
# =========================================================================
MAIN_STYLE = """
<style>
    /* 1. Import Luxusného Fontu (Quicksand) */
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500;700&display=swap');

    /* 2. Čisto čierne pozadie a luxusný font pre celú appku */
    .stApp, [data-testid="stSidebar"] { 
        background-color: #000000 !important; 
        color: #FFFFFF !important; 
        font-family: 'Quicksand', sans-serif !important; 
        font-weight: 300; 
    }
    
    /* 3. Vylepšené nápisy (H1, H2, H3) - Fialový Glow */
    h1, h2, h3 { 
        color: #BC8CF2; 
        font-weight: 700; 
        text-shadow: 0 0 15px rgba(188, 140, 242, 0.6); 
    }
    
    /* 4. Glassmorphism Neon Karty pre výsledky */
    .result-card {
        background: rgba(25, 25, 25, 0.8);
        border: 1px solid rgba(138, 43, 226, 0.4);
        padding: 25px; border-radius: 15px; margin: 15px 0;
        box-shadow: 0 0 20px rgba(138, 43, 226, 0.2);
    }
    
    /* 5. Vylepšené Neon Tlačidlá Streamlit */
    div.stButton > button {
        background: transparent;
        border: 1px solid #BC8CF2; 
        color: #BC8CF2; border-radius: 20px;
        font-weight: 500; transition: 0.3s;
        box-shadow: 0 0 10px rgba(138, 43, 226, 0.2);
    }
    div.stButton > button:hover { 
        background: rgba(138, 43, 226, 0.1);
        box-shadow: 0 0 20px rgba(138, 43, 226, 0.5); 
        transform: translateY(-2px);
    }
    
    /* 6. Uprataný Sidebar bez pozadia */
    [data-testid="stSidebarNav"] { background: transparent; }
    [data-testid="stSidebarNavSeparator"] { background: transparent; }
</style>
"""

# =========================================================================
# FUNKCIE PRE PRECHOD
# =========================================================================
def go_to_promo(): st.session_state.step = "promo"
def go_to_app(): st.session_state.step = "app"

# =========================================================================
# 1. OBRAZOVKA: PRIHLÁSENIE (Uplatníme AUTH_STYLE)
# =========================================================================
if st.session_state.step == "login":
    st.markdown(AUTH_STYLE, unsafe_allow_html=True)
    
    # Generovanie Zemegúľ
    st.markdown("""
    <div class="globe" style="left: 10%; width: 15px; height: 15px; animation-duration: 20s;"></div>
    <div class="globe" style="left: 30%; width: 25px; height: 25px; animation-duration: 12s; animation-delay: 5s;"></div>
    <div class="globe" style="left: 60%; width: 20px; height: 20px; animation-duration: 18s;"></div>
    <div class="globe" style="left: 85%; width: 12px; height: 12px; animation-duration: 25s; animation-delay: 1s;"></div>
    """, unsafe_allow_html=True)

    st.write("##")
    st.write("##")
    with st.container():
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.image("https://img.icons8.com/fluency/96/000000/globe-earth.png", width=100)
        st.title("OmniTravel 2026")
        st.write("Tvoj globálny AI sprievodca. Cestuj s OmniVision.")
        
        st.button("✨ Pokračovať s Google", on_click=go_to_promo)
        st.button(" Pokračovať s Apple", on_click=go_to_promo)
        
        st.write("--- alebo ---")
        st.text_input("E-mail", placeholder="tvoj@email.com")
        st.button("Vytvoriť účet", on_click=go_to_promo)
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 2. OBRAZOVKA: PROMO REKLAMA (Stále AUTH_STYLE pre plynulosť)
# =========================================================================
elif st.session_state.step == "promo":
    st.markdown(AUTH_STYLE, unsafe_allow_html=True)
    st.write("##")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown('<div class="promo-card" style="background: linear-gradient(135deg, #101010 0%, #3a0066 100%); border: 2px solid #BC8CF2; box-shadow: 0 0 30px rgba(138, 43, 226, 0.6); padding: 40px; border-radius: 20px; text-align: center;">', unsafe_allow_html=True)
        st.title("💎 OmniTravel PRO")
        st.write("Získaj maximum zo svojich ciest")
        st.markdown("""
        ✅ **Neobmedzený OmniVision** (Skenuj menu bez limitov)<br>
        ✅ **Offline Mapy** (Pamiatky aj bez signálu)<br>
        ✅ **Prioritná Podpora** (AI odpovedá bleskovo)
        """, unsafe_allow_html=True)
        st.write("### 0,00€ / mesiac")
        st.write("*(Limitovaná ponuka pre testerov)*")
        
        st.button("🚀 AKTIVOVAŤ PRO VERZIU", on_click=go_to_app)
        if st.button("Možno neskôr"): 
            st.session_state.step = "app"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 3. HLAVNÁ APLIKÁCIA (Uplatníme MAIN_STYLE - Čistá čierna & Luxusný font)
# =========================================================================
elif st.session_state.step == "app":
    st.markdown(MAIN_STYLE, unsafe_allow_html=True)
    
    with st.sidebar:
        st.markdown('<h2 style="color: #BC8CF2; text-shadow: 0 0 10px rgba(188,140,242,0.4);">💜 OmniTravel</h2>', unsafe_allow_html=True)
        stranka = st.selectbox("MENU", ["🗺️ Pamiatky", "📸 Skener", "👤 Profil"])
        if st.button("Odhlásiť sa"):
            st.session_state.step = "login"
            st.rerun()

    if stranka == "🗺️ Pamiatky":
        st.title("🗺️ Objavuj okolie")
        st.markdown('<div class="result-card"><h3>📍 Zistiť moju polohu</h3><p>Tento box sa zmení na GPS panel.</p></div>', unsafe_allow_html=True)
        if st.button("Hľadať v okolí (NZ)"):
            st.success("Hľadám pamiatky...")
            st.markdown('<div class="result-card"><h3>🏛️ Kalvária</h3><p>Historická pamiatka Nových Zámkov.</p></div>', unsafe_allow_html=True)

    elif stranka == "📸 Skener":
        st.title("📸 OmniVision Skener")
        st.write("Hľadám voľný AI model...")
        col1, col2 = st.columns(2)
        with col1: st.button("📷 Fotoaparát", use_container_width=True)
        with col2: st.button("📂 Galéria", use_container_width=True)
        st.markdown('<div class="result-card"><h3>Výsledok Analýzy</h3><p>Tu sa zobrazí preklad a rozbor menu.</p></div>', unsafe_allow_html=True)

    elif stranka == "👤 Profil":
        st.title("👤 Profil Cestovateľa")
        col1, col2 = st.columns(2)
        with col1: st.markdown('<div class="result-card"><h3>Úroveň 1</h3><p>Cestovateľ</p></div>', unsafe_allow_html=True)
        with col2: st.markdown('<div class="result-card"><h3>Body</h3><p>250 VP</p></div>', unsafe_allow_html=True)
        st.progress(25)
