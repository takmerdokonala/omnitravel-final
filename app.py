import streamlit as st
import base64
import requests
from groq import Groq

# --- KONFIGURÁCIA STRÁNKY ---
st.set_page_config(page_title="OmniTravel Ultra", layout="wide")

# Inicializácia klientov
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]

# --- MAGICKÉ ČIERNE POZADIE S POHYBLIVÝMI TVARMI ---
st.markdown("""
<style>
    .stApp { background: black; color: white; }
    
    @keyframes move {
        from { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        to { transform: translateY(-10vh) rotate(360deg); opacity: 0.8; }
    }
    
    .shape {
        position: fixed;
        background: rgba(138, 43, 226, 0.4);
        border-radius: 3px;
        z-index: -1;
        animation: move linear infinite;
    }

    .result-card {
        background: rgba(25, 25, 25, 0.9);
        border: 1px solid #8A2BE2;
        padding: 15px;
        border-radius: 12px;
        margin: 10px 0;
    }
    
    .login-btn { 
        display: block; width: 100%; padding: 10px; margin: 8px 0; 
        text-align: center; border-radius: 8px; text-decoration: none; 
        font-weight: bold; font-size: 14px; 
    }
    .google-btn { background: white; color: black; }
    .apple-btn { background: #333; color: white; }
</style>

<div class="shape" style="left:10%; width:10px; height:10px; animation-duration:15s; animation-delay:0s;"></div>
<div class="shape" style="left:35%; width:15px; height:15px; animation-duration:20s; animation-delay:5s;"></div>
<div class="shape" style="left:60%; width:8px; height:8px; animation-duration:12s; animation-delay:2s;"></div>
<div class="shape" style="left:85%; width:12px; height:12px; animation-duration:18s; animation-delay:8s;"></div>
""", unsafe_allow_html=True)

# --- BOČNÉ MENU (SIDEBAR) ---
with st.sidebar:
    st.title("💜 OmniTravel Pro")
    stranka = st.selectbox("Kam ideme?", ["🗺️ Pamiatky v okolí", "📸 Skener Menu", "👤 Prihlásenie", "📤 Zdieľať"])
    
    st.markdown("---")
    st.subheader("Sociálne siete")
    col1, col2 = st.columns(2)
    with col1: st.button("📸 IG")
    with col2: st.button("📘 FB")

# --- 🗺️ SEKCIA PAMIATKY ---
if stranka == "🗺️ Pamiatky v okolí":
    st.title("🗺️ Objavuj okolie")
    if st.button("📍 Zistiť moju polohu"):
        with st.spinner("Hľadám pamiatky..."):
            try:
                url = "https://api.tavily.com/search"
                payload = {
                    "api_key": TAVILY_API_KEY,
                    "query": "najzaujímavejšie pamiatky Nové Zámky a okolie",
                    "search_depth": "advanced"
                }
                response = requests.post(url, json=payload)
                vysledky = response.json().get("results", [])
                
                for r in vysledky:
                    st.markdown(f'<div class="result-card"><h4>📍 {r["title"]}</h4><p>{r["content"]}</p><a href="{r["url"]}" target="_blank" style="color:#8A2BE2;">Viac info →</a></div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Chyba pri hľadaní: {e}")

# --- 📸 SEKCIA SKENER MENU ---
elif stranka == "📸 Skener Menu":
    st.title("📸 OmniVision Skener")
    foto = st.file_uploader("Nahraj fotku menu", type=["jpg", "png", "jpeg"])
    
    if foto:
        with st.spinner("AI číta menu..."):
            try:
                base64_image = base64.b64encode(foto.getvalue()).decode('utf-8')
                res = client.chat.completions.create(
                    model="llama-3.2-11b-vision-preview",
                    messages=[{"role": "user", "content": [{"type": "text", "text": "Prelož toto menu do slovenčiny."}, {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}]}]
                )
                st.markdown(f'<div class="result-card">{res.choices[0].message.content}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"AI momentálne neodpovedá: {e}")

# --- 👤 SEKCIA PRIHLÁSENIE ---
elif stranka == "👤 Prihlásenie":
    st.title("👤 Prihlásenie")
    st.markdown('<a href="#" class="login-btn google-btn">Sign in with Google</a>', unsafe_allow_html=True)
    st.markdown('<a href="#" class="login-btn apple-btn">Sign in with Apple</a>', unsafe_allow_html=True)
    st.markdown("---")
    email = st.text_input("E-mail")
    if st.button("Poslať overovací kód"):
        st.success("Link na prihlásenie bol odoslaný!")

# --- 📤 SEKCIA ZDIEĽAŤ ---
elif stranka == "📤 Zdieľať":
    st.title("📤 Povedz o nás svetu")
    st.write("Zdieľaj svoju polohu s priateľmi.")
    st.button("Zdieľať na Instagram")
