import streamlit as st
import base64
import requests
from groq import Groq

# --- KONFIGURÁCIA ---
st.set_page_config(page_title="OmniTravel Ultra", layout="wide")

# Inicializácia klientov (vytiahne si kľúče zo Secrets)
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]

# --- MAGICKÉ POZADIE A ŠTÝL ---
st.markdown("""
<style>
    .stApp { background: black; color: white; }
    @keyframes move { from { transform: translateY(0px); } to { transform: translateY(-1000px); } }
    .shape {
        position: fixed; width: 8px; height: 8px; background: rgba(138, 43, 226, 0.5);
        border-radius: 50%; z-index: -1; animation: move 20s linear infinite;
    }
    .result-card {
        background: rgba(30, 30, 30, 0.9); border: 1px solid #8A2BE2;
        padding: 15px; border-radius: 12px; margin: 10px 0;
    }
    .login-btn { display: block; width: 100%; padding: 8px; margin: 5px 0; text-align: center; border-radius: 5px; text-decoration: none; font-weight: bold; font-size: 14px; }
    .google-btn { background: white; color: black; }
    .apple-btn { background: #333; color: white; }
</style>
<div class="shape" style="left:10%; bottom:0; animation-duration:25s;"></div>
<div class="shape" style="left:50%; bottom:0; animation-duration:15s;"></div>
<div class="shape" style="left:80%; bottom:0; animation-duration:30s;"></div>
""", unsafe_allow_html=True)

# --- BOČNÉ MENU ---
with st.sidebar:
    st.title("💜 OmniTravel")
    stranka = st.selectbox("Menu:", ["🗺️ Pamiatky", "📸 Skener Menu", "👤 Profil & Login"])
    
    st.markdown("---")
    st.subheader("Sociálne siete")
    col1, col2 = st.columns(2)
    with col1: st.button("📸 IG")
    with col2: st.button("📘 FB")

# --- 🗺️ SEKCIA PAMIATKY (Tvoj pôvodný kód) ---
if stranka == "🗺️ Pamiatky":
    st.title("🗺️ Čo je v tvojom okolí?")
    
    if st.button("📍 Zistiť moju polohu (GPS)"):
        st.info("Hľadám pamiatky v Nových Zámkoch a okolí...")
        try:
            url = "https://api.tavily.com/search"
            payload = {
                "api_key": TAVILY_API_KEY,
                "query": "najzaujímavejšie pamiatky a atrakcie Nové Zámky a okolie",
                "search_depth": "advanced"
            }
            response = requests.post(url, json=payload)
