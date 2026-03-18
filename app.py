import streamlit as st
import base64
import os

# --- 1. KONFIGURÁCIA ---
st.set_page_config(
    page_title="OmniTravel", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. PAMÄŤ ---
if 'step' not in st.session_state: st.session_state.step = "app" # Pre testovanie rovno do app

# =========================================================================
# ⚪️ ULTRA ELEGANT SIDEBAR (TOPS STYLE)
# =========================================================================
STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&display=swap');

    .stApp { 
        background-color: #FFFFFF !important; 
        font-family: 'Inter', sans-serif !important; 
    }

    /* Schovanie pôvodných Streamlit prvkov pre čistý look */
    [data-testid="stHeader"] { background-color: white !important; border-bottom: 1px solid #F0F0F0; }
    .block-container { padding: 0rem !important; }

    /* SIDEBAR DEFINÍCIA */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E0E0E0;
        width: 320px !important;
    }
    
    /* Odstránenie paddingu v sidebare */
    [data-testid="stSidebarUserContent"] {
        padding-top: 0rem !important;
    }

    /* Horná časť menu (Login / Register) */
    .nav-top-auth {
        display: flex;
        background-color: #333333;
        color: white;
        text-align: center;
    }
    .nav-auth-item {
        flex: 1;
        padding: 15px 0;
        font-size: 0.9rem;
        font-weight: 500;
        border-right: 1px solid #444444;
        cursor: pointer;
    }

    /* Prepínač jazykov */
    .nav-lang-bar {
        display: flex;
        background-color: #F9F9F9;
        border-bottom: 1px solid #EEEEEE;
    }
    .nav-lang-item {
        flex: 1;
        padding: 10px 0;
        text-align: center;
        font-size: 0.85rem;
        color: #666666;
        border-right: 1px solid #EEEEEE;
    }
    .nav-lang-active {
        color: #000000;
        font-weight: 600;
    }

    /* Štýlovanie Radio Menu aby vyzeralo ako zoznam */
    .stRadio > div { gap: 0px !important; }
    .stRadio label {
        padding: 18px 25px !important;
        border-bottom: 1px solid #F5F5F5 !important;
        width: 100% !important;
        margin: 0 !important;
        font-size: 1rem !important;
        color: #333333 !important;
        transition: 0.2s;
    }
    .stRadio label:hover {
        background-color: #FBFBFB !important;
    }
    
    /* Skrytie radio krúžkov */
    [data-testid="stWidgetLabel"] { display: none; }
    div[data-testid="stMarkdownContainer"] p { margin-bottom: 0; }

    /* Banner */
    .banner-box { width: 100%; line-height: 0; }
    .omni-banner { width: 100%; display: block; }

</style>
"""

st.markdown(STYLE, unsafe_allow_html=True)

# =========================================================================
# 📱 BOČNÉ MENU (SIDEBAR)
# =========================================================================
with st.sidebar:
    # 1. Login / Register sekcia
    st.markdown('''
        <div class="nav-top-auth">
            <div class="nav-auth-item">Login</div>
            <div class="nav-auth-item" style="border-right:none;">Register</div>
        </div>
    ''', unsafe_allow_html=True)

    # 2. Jazykový pásik
    st.markdown('''
        <div class="nav-lang-bar">
            <div class="nav-lang-item nav-lang-active">SK</div>
            <div class="nav-lang-item" style="border-right:none;">EN</div>
        </div>
    ''', unsafe_allow_html=True)

    # 3. Samotná navigácia
    # Používame ikony a názvy presne podľa zadania
    stranka = st.radio(
        "Navigácia",
        [
            "🏠 Domovská stránka", 
            "👤 Môj Profil", 
            "🤖 AI Menu", 
            "📸 Scanner", 
            "📍 Mapa okolia / Kam vyraziť", 
            "👥 Komunita"
        ],
        label_visibility="collapsed"
    )

    st.markdown('<div style="padding: 20px; color: #999; font-size: 0.8rem;">OmniTravel v1.0</div>', unsafe_allow_html=True)

# =========================================================================
# 🖼️ OBSAH STRÁNKY
# =========================================================================

# Zobrazenie banneru iba na domovskej obrazovke a komunite
if "Domovská" in stranka or "Komunita" in stranka:
    if os.path.exists("header.png"):
        with open("header.png", "rb") as f:
            data = base64.b64encode(f.read()).decode()
        st.markdown(f'<div class="banner-box"><img src="data:image/png;base64,{data}" class="omni-banner"></div>', unsafe_allow_html=True)

# Dynamický nadpis podľa výberu v menu
st.markdown(f'<h1 style="text-align: center; margin-top: 40px; font-weight: 300;">{stranka}</h1>', unsafe_allow_html=True)

if "Domovská" in stranka:
    st.markdown("""
    <div style="max-width: 600px; margin: 0 auto; padding: 20px; text-align: center;">
        <p style="color: #666;">Vitajte späť! Objavte nové miesta alebo využite náš AI skener pre preklad jedálnych lístkov.</p>
    </div>
    """, unsafe_allow_html=True)

elif "Scanner" in stranka:
    st.camera_input("Odfoťte menu pre AI analýzu")

elif "Komunita" in stranka:
    st.markdown("""
    <div style="max-width: 500px; margin: 20px auto; border: 1px solid #EEE; padding: 15px;">
        <p><b>Maroš Svetobežník</b> • Práve teraz</p>
        <div style="height: 200px; background: #F5F5F5; margin: 10px 0;"></div>
        <p>Nové menu v OmniTravel vyzerá svetovo!</p>
    </div>
    """, unsafe_allow_html=True)
