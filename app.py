import streamlit as st
import base64
import requests
from groq import Groq

# --- INICIALIZÁCIA KLIENTA ---
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# --- KONFIGURÁCIA STRÁNKY ---
st.set_page_config(page_title="OmniTravel Ultra", layout="wide", initial_sidebar_state="expanded")

# --- MAGICKÉ ČIERNE POZADIE S FIALOVÝMI TVARMI ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: white; }
    
    /* Animované tvary */
    @keyframes move {
        from { transform: translateY(100vh) translateX(0); opacity: 0.5; }
        to { transform: translateY(-10vh) translateX(20px); opacity: 0; }
    }
    .shape {
        position: fixed; background: #8A2BE2; border-radius: 50%;
        z-index: 0; animation: move 10s linear infinite;
    }
    
    /* Štýl pre bočné menu */
    [data-testid="stSidebar"] { background-color: #111111; border-right: 1px solid #8A2BE2; }
    
    /* Štýl pre boxy */
    .result-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid #8A2BE2;
        padding: 15px; border-radius: 10px; margin: 10px 0;
    }
</style>
<div class="shape" style="left: 10%; width: 10px; height: 10px; animation-duration: 15s;"></div>
<div class="shape" style="left: 40%; width: 20px; height: 20px; animation-duration: 20s; background: #9400D3;"></div>
<div class="shape" style="left: 80%; width: 15px; height: 15px; animation-duration: 12s;"></div>
""", unsafe_allow_html=True)

# --- BOČNÉ MENU ---
with st.sidebar:
    st.title("💜 OmniTravel")
    stranka = st.selectbox(
        "MENU",
        ["🗺️ Pamiatky", "📸 Skener Menu", "👤 Profil"]
    )
    st.markdown("---")
    st.write("🔒 **Prihlásenie**")
    st.button("Google Login", use_container_width=True)
    st.button("Apple Login", use_container_width=True)
    st.markdown("---")
    st.write("🌐 **Zdieľať**")
    st.write("📸 Instagram | 📘 Facebook")

# --- HLAVNÝ OBSAH ---

if stranka == "🗺️ Pamiatky":
    st.title("🗺️ Objavuj okolie")
    if st.button("📍 Zistiť moju polohu"):
        # SEM VLOŽÍME TVOJ TAVILY KÓD (zjednodušený pre test)
        st.success("Hľadám pamiatky v Nových Zámkoch...")
        st.markdown('<div class="result-card">🏰 <b>Kalvária NZ</b><br>Historické miesto s výhľadom.</div>', unsafe_allow_html=True)
        st.markdown('<div class="result-card">🌳 <b>Berek</b><br>Krásny lesopark na prechádzku.</div>', unsafe_allow_html=True)

elif stranka == "📸 Skener Menu":
    st.title("📸 OmniVision Skener")
    zdroj = st.radio("Zdroj:", ["Fotoaparát", "Galéria"], horizontal=True)
    foto = st.camera_input("Odfoť") if zdroj == "Fotoaparát" else st.file_uploader("Nahraj")
    
    if foto:
        with st.spinner("Analyzujem..."):
            # Náš smart kód s viacerými modelmi
            base64_image = base64.b64encode(foto.getvalue()).decode('utf-8')
            try:
                resp = client.chat.completions.create(
                    model="llama-3.2-11b-vision-preview",
                    messages=[{"role": "user", "content": [{"type": "text", "text": "Prelož toto menu."}, {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}]}]
                )
                st.markdown(f'<div class="result-card">{resp.choices[0].message.content}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.warning("Model je preťažený, skús o minútu.")

elif stranka == "👤 Profil":
    st.title("👤 Tvoj profil")
    st.write("Tu bude história tvojich skenov.")
    st.progress(20, text="Body za cestovanie: 200")
