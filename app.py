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
if 'step' not in st.session_state: st.session_state.step = "app"

# =========================================================================
# ⚪️ PURE MINIMALIST DESIGN (OPRAVA ZOBRAZENIA TEXTU)
# =========================================================================
STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

    .stApp { 
        background-color: #FFFFFF !important; 
        font-family: 'Inter', sans-serif !important; 
    }

    [data-testid="stHeader"] { background-color: white !important; }
    .block-container { padding: 0rem !important; }

    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E0E0E0;
        width: 320px !important;
    }
    [data-testid="stSidebarUserContent"] { padding-top: 0rem !important; }

    /* Horná Auth sekcia */
    .nav-top-auth {
        display: flex;
        background-color: #333333;
        color: white;
        text-align: center;
    }
    .nav-auth-item {
        flex: 1;
        padding: 18px 0;
        font-size: 0.85rem;
        font-weight: 500;
        border-right: 1px solid #444444;
        letter-spacing: 1px;
    }

    /* Jazykový pásik */
    .nav-lang-bar {
        display: flex;
        background-color: #F9F9F9;
        border-bottom: 1px solid #EEEEEE;
    }
    .nav-lang-item {
        flex: 1;
        padding: 12px 0;
        text-align: center;
        font-size: 0.85rem;
        color: #999999;
        border-right: 1px solid #EEEEEE;
    }
    .nav-lang-active { color: #000000; font-weight: 600; }

    /* MENU - OPRAVA VIDITEĽNOSTI TEXTU */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label {
        padding: 22px 25px !important;
        border-bottom: 1px solid #F5F5F5 !important;
        margin: 0 !important;
        width: 100%;
        display: flex;
    }
    
    /* Úplné schovanie krúžkov a medzier po nich */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label [data-testid="stWidgetLabel"],
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label div:first-child {
        display: none !important;
    }

    /* VYKRESLENIE TEXTU - ČIERNA A DOSTREDU */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label div[data-testid="stMarkdownContainer"] p {
        color: #000000 !important;
        font-size: 1rem !important;
        font-weight: 400 !important;
        margin-left: 0px !important; /* Reset posunu */
        text-align: left !important;
        width: 100%;
    }

    /* Efekt pri vybraní (jemné zvýraznenie) */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label[data-filled="true"] {
        background-color: #FBFBFB !important;
    }

    /* Obsah */
    .banner-box { width: 100%; line-height: 0; }
    .omni-banner { width: 100%; display: block; }
    h1 { color: #000000 !important; font-weight: 300 !important; text-align: center; }

</style>
"""

st.markdown(STYLE, unsafe_allow_html=True)

# =========================================================================
# 📱 BOČNÉ MENU
# =========================================================================
with st.sidebar:
    # 1. Login / Register
    st.markdown('<div class="nav-top-auth"><div class="nav-auth-item">LOGIN</div><div class="nav-auth-item" style="border-right:none;">REGISTER</div></div>', unsafe_allow_html=True)

    # 2. Jazyky
    st.markdown('<div class="nav-lang-bar"><div class="nav-lang-item nav-lang-active">SK</div><div class="nav-lang-item" style="border-right:none;">EN</div></div>', unsafe_allow_html=True)

    # 3. Zoznam stránok (ČISTÝ TEXT)
    stranka = st.radio(
        "Navigácia",
        [
            "Domovská stránka", 
            "Môj Profil", 
            "AI Menu", 
            "Scanner", 
            "Mapa okolia", 
            "Komunita"
        ],
        label_visibility="collapsed"
    )

    st.markdown('<div style="padding: 40px 20px; color: #CCC; font-size: 0.7rem; text-align: center; letter-spacing: 2px;">OMNITRAVEL v1.0</div>', unsafe_allow_html=True)

# =========================================================================
# 🖼️ OBSAH
# =========================================================================
if "Domovská" in stranka or "Komunita" in stranka:
    if os.path.exists("header.png"):
        with open("header.png", "rb") as f:
            data = base64.b64encode(f.read()).decode()
        st.markdown(f'<div class="banner-box"><img src="data:image/png;base64,{data}" class="omni-banner"></div>', unsafe_allow_html=True)

st.markdown(f'<h1 style="margin-top: 50px; text-transform: uppercase; letter-spacing: 2px;">{stranka}</h1>', unsafe_allow_html=True)

if "Domovská" in stranka:
    st.markdown('<div style="max-width: 600px; margin: 0 auto; padding: 20px; text-align: center; color: #888; font-weight: 300; line-height: 1.6;">Vitajte v minimalistickom rozhraní OmniTravel. Vaše cesty začínajú tu.</div>', unsafe_allow_html=True)
