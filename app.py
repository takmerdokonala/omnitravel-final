import streamlit as st
import base64
from groq import Groq
from tavily import TavilyClient
from streamlit_js_eval import streamlit_js_eval, get_geolocation

# --- BEZPEČNÁ KONFIGURÁCIA (Secrets) ---
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]
except KeyError:
    st.error("Chýbajú API kľúče v Secrets! Aplikácia nemôže fungovať.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)
tavily = TavilyClient(api_key=TAVILY_API_KEY)

# --- FIALOVÝGlassmorphism DIZAJN (CSS) ---
FIALOVA = "#9333ea" # Krásna neónová fialová
POZADIE = "#110022" # Temná fialová (temné pozadie)

st.set_page_config(page_title="OmniTravel Pro", page_icon="📍", layout="wide")

st.markdown(f"""
    <style>
    /* Základné nastavenia */
    .stApp {{ background: {POZADIE}; color: white; }}
    .stApp > header {{ background: transparent; }}
    
    /* Nadpisy a text */
    h1, h2, h3, p {{ color: white !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
    .pro-title {{ color: {FIALOVA}; font-weight: bold; font-size: 2em; }}
    
    /* Tlačidlá a Vstupy */
    .stButton > button {{ 
        background-color: {FIALOVA} !important; border-radius: 20px; border: none; 
        color: white !important; padding: 10px 20px; transition: 0.3s;
    }}
    .stButton > button:hover {{ background-color: white !important; color: {FIALOVA} !important; }}
    .stTextInput > div > div > input {{ background-color: rgba(255,255,255,0.05) !important; color: white !important; border: 1px solid {FIALOVA} !important; border-radius: 10px; }}

    /* Karta výsledkov */
    .result-card {{ 
        background: rgba(255, 255, 255, 0.05); padding: 25px; 
        border-radius: 20px; border-left: 6px solid {FIALOVA}; 
        box-shadow: 0 4px 15px rgba(147, 51, 234, 0.3);
    }}
    
    /* Pro zámok (Zlaté tlačidlo) */
    .pro-lock {{ background: linear-gradient(45deg, #FFD700, #FFA500) !important; color: black !important; font-weight: bold; }}
    </style>
    """, unsafe_allow_html=True)

# Logo a Názov
st.image("image_0.png", width=120) # Tu bude tvoje logo
st.markdown('<div class="pro-title">OmniTravel AI <span style="font-size: 0.5em; color: #aaa;">PRO</span></div>', unsafe_allow_html=True)

# Bočný panel - Nastavenia
with st.sidebar:
    st.subheader("🔑 Profil a Platba")
    user_pro = st.toggle("Aktivovať Pro verziu (Test)", value=False)
    
    if user_pro:
        st.success("Máš aktivovanú Pro verziu! 💎")
    else:
        st.warning("Používaš Free verziu.")
        if st.button("🔥 Prejsť na PRO", help="Odomkni Audio a Offline"):
            st.toast("Presmerovávam na platobnú bránu (Test)...")

# --- FUNKCIE APPKY ---

tab1, tab2, tab3 = st.tabs(["🗺️ Pamiatky", "📸 Skener Menu", "💎 Pro Funkcie"])

# --- TAB 1: PAMIATKY & GPS ---
with tab1:
    st.subheader("Zisti, čo je v okolí")
    
    # 📍 GPS POLOHA (Pomocou streamlit_js_eval)
    gps_check = st.checkbox("Použiť moju polohu (📍 GPS)")
    loc = None
    if gps_check:
        with st.spinner("Získavam polohu z GPS..."):
            loc = get_geolocation()
            if loc:
                lat = loc['coords']['latitude']
                lon = loc['coords']['longitude']
                st.write(f"Získaná poloha: {lat:.4f}, {lon:.4f}")
                # AI search na základe GPS
                query = f"top sights near latitude {lat} longitude {lon} 2026 prices"
            else:
                st.error("Nepodarilo sa získať polohu. Skontroluj povolenia prehliadača.")
                gps_check = False # Reset checku
    
    mesto = st.text_input("Zadaj mesto (ak nemáš GPS):", "Nové Zámky", disabled=gps_check)
    
    if not gps_check and not mesto:
        st.stop()
    
    # AI Vyhľadávanie
    if st.button("Hľadať info na webe"):
        with st.spinner("Hľadám..."):
            res = tavily.search(query=query if gps_check else f"top sights in {mesto} 2026 prices")
            st.info("AI vygeneruje podrobný prehľad...")
            st.markdown(f'<div class="result-card">{res}</div>', unsafe_allow_html=True)

# --- TAB 2: SKENER MENU (AI VISION) ---
with tab2:
    st.subheader("📸 Inteligentný skener menu OmniVision")
    st.write("Analyzuj jedálny lístok naživo alebo z uloženej fotky.")
    
    # --- VÝBER ZDROJA OBRÁZKA ---
    # Použijeme radio button, aby si používateľ vybral
    zdroj_foto = st.radio(
        "Vyber zdroj obrázka:",
        ("Nová fotka (Fotoaparát)", "Nahrať z galérie (Uložená fotka)"),
        horizontal=True
    )
    
    # Premenná pre obrázok
    image_to_process = None
    
    if zdroj_foto == "Nová fotka (Fotoaparát)":
        # Pôvodný camera input
        foto_live = st.camera_input("Odfoť menu", key="camera_pro")
        if foto_live:
            image_to_process = foto_live
            
    else:
        # 📂 NOVÉ: File Uploader pre galériu
        foto_upload = st.file_uploader(
            "Vyber fotku menu z galérie",
            type=["jpg", "jpeg", "png"],
            key="gallery_pro",
            help="Podporujeme formáty JPG, JPEG a PNG."
        )
        if foto_upload:
            image_to_process = foto_upload
            # Voliteľne: Zobrazíme náhľad nahranej fotky
            st.image(image_to_process, caption="Nahrátý obrázok", width=300)

    # --- SPRACOVANIE AI VISION (Spoločné pre oba zdroje) ---
    if image_to_process:
        with st.spinner("OmniVision číta a analyzuje menu..."):
            
            # 1. Príprava obrázka (Získanie Base64)
            bytes_data = image_to_process.getvalue()
            base64_image = base64.b64encode(bytes_data).decode('utf-8')
            
            # 2. Volanie Vision Modelu (Llama 3.2 Vision)
            try:
                response = client.chat.completions.create(
                    model="llava-v1.5-7b-4096-preview",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "Analyzuj toto menu. Prelož názvy jedál a nápojov do slovenčiny. Vypíš prehľadne ceny. Upozorni na zaujímavé jedlá, alergény alebo nezvyčajne vysoké ceny. Ak je to možné, odporuč jedlo pre dieťa."
                                },
                                {
                                    "type": "image_url",
                                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                                }
                            ]
                        }
                    ],
                    temperature=0.4,
                    max_tokens=1024
                )
                
                # 3. Zobrazenie výsledku
                st.markdown(
                    f'<div class="result-card"><h3>📝 Rozbor menu OmniVision:</h3>{response.choices[0].message.content}</div>',
                    unsafe_allow_html=True
                )
                
            except Exception as e:
                st.error(f"Chyba pri analýze: {e}")
# --- TAB 3: PRO FUNKCIE (Hlas & Offline) ---
with tab3:
    st.subheader("💎 Exkluzívne Pro funkcie")
    
    # AUDIO SPRIEVODCA (Odomknutý len v Pro verzii)
    st.write("📖 Audio Sprievodca pre pamiatky")
    if user_pro:
        # Použijeme gTTS pre hlas
        st.info("Tu si vypočuješ Audio")
    else:
        st.button("🔒 Audio Sprievodca (Len PRO)", key="audio_lock")
    
    st.write("---")
    
    st.write("☁️ Offline prístup (Uloženie skenov)")
    if user_pro:
        st.info("Skeny sú uložené offline")
    else:
        st.button("🔒 Offline Ukladanie (Len PRO)", key="offline_lock")
