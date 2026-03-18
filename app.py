import streamlit as st
import base64
from groq import Groq

# --- KONFIGURÁCIA STRÁNKY ---
st.set_page_config(page_title="OmniTravel Ultra", layout="wide", initial_sidebar_state="expanded")

# --- MAGICKÉ POZADIE (ČIERNE S FIALOVÝMI TVARMI) ---
st.markdown("""
<style>
    /* Hlavné pozadie */
    .stApp {
        background: black;
    }
    
    /* Animované tvary na pozadí */
    @keyframes move {
        from { transform: translateY(0px) translateX(0px) rotate(0deg); }
        to { transform: translateY(-1000px) translateX(100px) rotate(360deg); }
    }
    
    .shape {
        position: fixed;
        width: 10px;
        height: 10px;
        background: rgba(138, 43, 226, 0.4);
        border-radius: 50%;
        z-index: -1;
        animation: move 20s linear infinite;
    }

    /* Štýl pre výsledky a karty */
    .result-card {
        background: rgba(30, 30, 30, 0.8);
        border: 1px solid #8A2BE2;
        padding: 20px;
        border-radius: 15px;
        color: white;
        margin: 10px 0;
    }

    /* Štýl pre tlačidlá prihlásenia */
    .login-btn {
        display: block;
        width: 100%;
        padding: 10px;
        margin: 5px 0;
        text-align: center;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
    }
    .google-btn { background: #fff; color: #000; }
    .apple-btn { background: #333; color: #fff; }
</style>

<div class="shape" style="left: 10%; bottom: 0; animation-duration: 25s;"></div>
<div class="shape" style="left: 30%; bottom: 0; animation-duration: 18s; width: 15px; background: #9400D3;"></div>
<div class="shape" style="left: 60%; bottom: 0; animation-duration: 30s;"></div>
<div class="shape" style="left: 85%; bottom: 0; animation-duration: 22s; height: 12px;"></div>
""", unsafe_allow_html=True)

# --- BOČNÉ MENU (SIDEBAR) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/globe-earth.png", width=80) # Alebo tvoje fialové logo
    st.title("OmniTravel Pro")
    
    st.markdown("---")
    # ROZBAĽOVACIE MENU (Navigácia)
    stranka = st.selectbox(
        "Kam sa chystáš?",
        ["🗺️ Pamiatky a Okolie", "📸 OmniVision Skener", "👤 Môj Profil", "💎 Nastavenia Pro"]
    )
    
    st.markdown("---")
    st.subheader("Prihlásenie")
    st.markdown('<a href="#" class="login-btn google-btn">Sign in with Google</a>', unsafe_allow_html=True)
    st.markdown('<a href="#" class="login-btn apple-btn">Sign in with Apple</a>', unsafe_allow_html=True)
    email = st.text_input("E-mail")
    if st.button("Prihlásiť e-mailom"):
        st.success("Overovací link odoslaný!")

    st.markdown("---")
    st.subheader("Zdieľaj appku")
    col1, col2, col3 = st.columns(3)
    with col1: st.button("📸 IG")
    with col2: st.button("🐦 X")
    with col3: st.button("📘 FB")

# --- HLAVNÝ OBSAH PODĽA VÝBERU ---

if stranka == "🗺️ Pamiatky a Okolie":
    st.title("🗺️ Čo je v okolí?")
    # Tu nechaj svoj kód pre GPS a Tavily (Tab 1)
    st.info("Klikni na tlačidlo v tvojom pôvodnom kóde pre hľadanie pamiatok.")

elif stranka == "📸 OmniVision Skener":
    st.title("📸 OmniVision Skener")
    # Tu vlož ten náš "nezničiteľný" kód pre analýzu fotiek (Tab 2)
    st.write("Nahraj fotku menu a AI ju spracuje.")

elif stranka == "👤 Môj Profil":
    st.title("👤 Tvoj Profil")
    st.write("Tu uvidíš históriu svojich ciest a naskenovaných menu.")
    st.progress(45, text="Vernostné body: 450/1000")

elif stranka == "💎 Nastavenia Pro":
    st.title("💎 OmniTravel Pro")
    st.checkbox("Aktivovať prémiové mapy")
    st.checkbox("Offline režim")
