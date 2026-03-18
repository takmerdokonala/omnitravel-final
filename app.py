import streamlit as st
import math
import base64
import os

# --- 1. KONFIGURÁCIA ---
st.set_page_config(
    page_title="OmniTravel", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. PAMÄŤ ---
if 'step' not in st.session_state: st.session_state.step = "login"

# =========================================================================
# ⚪️ TOPS STYLE ELEGANT DESIGN (CSS)
# =========================================================================
STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap');

    .stApp { 
        background-color: #FFFFFF !important; 
        font-family: 'Roboto', sans-serif !important; 
    }

    /* FIX HLAVIČKY */
    [data-testid="stHeader"] {
        background-color: white !important;
        border-bottom: 1px solid #EEEEEE;
    }
    
    .block-container {
        padding: 0rem !important;
    }

    /* ČIERNE PÍSMO */
    h1, h2, h3, p, span, label {
        color: #000000 !important;
        font-weight: 400 !important;
    }

    /* ELEGANTNÝ SIDEBAR PODĽA VZORU */
    [data-testid="stSidebar"] {
        background-color: #F9F9F9 !important;
        border-right: 1px solid #EEEEEE;
        width: 300px !important;
    }
    
    /* Štýlovanie položiek v menu */
    .stRadio > div {
        gap: 0px !important;
    }
    
    .stRadio label {
        padding: 15px 20px !important;
        border-bottom: 1px solid #F0F0F0 !important;
        width: 100% !important;
        margin: 0 !important;
        transition: 0.2s;
    }
    
    .stRadio label:hover {
        background-color: #F0F0F0 !important;
    }

    /* BANNER HRANATÝ */
    .banner-container {
        width: 100%;
        margin: 0;
        line-height: 0;
    }
    .omni-banner {
        width: 100%;
        display: block;
    }
</style>
"""

# =========================================================================
# 1. LOGIN
# =========================================================================
if st.session_state.step == "login":
    st.markdown(STYLE, unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; padding-top: 150px;">', unsafe_allow_html=True)
    st.title("OmniTravel")
    if st.button("Vstúpiť"): 
        st.session_state.step = "app"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 2. APP
# =========================================================================
elif st.session_state.step == "app":
    st.markdown(STYLE, unsafe_allow_html=True)
    
    with st.sidebar:
        st.markdown('<div style="padding: 20px;"><h2>Menu</h2></div>', unsafe_allow_html=True)
        
        # Menu s ikonkami (používame textové ikony pre stabilitu)
        stranka = st.radio(
            "",
            ["🏠 Domov / Komunita", "🗺️ Mapa okolia", "📷 AI Skener", "👤 Môj Profil"],
            label_visibility="collapsed"
        )
        
        st.write("##")
        if st.button("Odhlásiť sa"):
            st.session_state.step = "login"
            st.rerun()

    # --- OBSAH ---
    if "Domov" in stranka:
        if os.path.exists("header.png"):
            with open("header.png", "rb") as f:
                data = base64.b64encode(f.read()).decode()
            st.markdown(f'<div class="banner-container"><img src="data:image/png;base64,{data}" class="omni-banner"></div>', unsafe_allow_html=True)
        
        st.markdown('<h1 style="text-align: center; margin-top: 40px;">Čo nové v komunite</h1>', unsafe_allow_html=True)

        st.markdown("""
        <div style="max-width: 600px; margin: 20px auto; padding: 0 20px;">
            <p><b>Maroš Svetobežník</b> • Nové Zámky</p>
            <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=600" style="width:100%; border-radius: 0px;">
            <p><br>Dizajn menu je teraz presne podľa vzoru. Čisté línie a funkčnosť.</p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown(f'<div style="padding: 40px;"><h1>{stranka}</h1><p>Sekcia je pripravená.</p></div>', unsafe_allow_html=True)
