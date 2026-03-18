import streamlit as st
import base64

# --- 1. KONFIGURÁCIA (Musí byť úplne hore!) ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# --- 2. PAMÄŤ A STAV (Ukladanie relácie) ---
if 'lang' not in st.session_state: st.session_state.lang = "Slovenčina"
if 'is_registered' not in st.session_state: st.session_state.is_registered = False

# --- 3. DIZAJN A ŠTÝL (CSS pre presný vzhľad z image_9.png) ---
st.markdown("""
<style>
    /* Import moderného písma */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background-color: #FFFFFF !important;
    }

    /* Hlavný kontajner na vycentrovanie všetkého */
    .main-center-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        min-height: 80vh; /* Zabezpečí stred na výšku stránky */
        width: 100%;
        max-width: 600px; /* Obmedzíme šírku na webe pre lepší vzhľad */
        margin: auto;
    }

    /* Nadpis OMNITRAVEL (Celoštátny) */
    .brand-header {
        font-weight: 700;
        font-size: 2.5rem;
        color: #111827;
        letter-spacing: -1px;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    /* Podnadpis (Sivý text) */
    .brand-sub {
        color: #6B7280;
        font-size: 1rem;
        margin-bottom: 40px;
        font-weight: 300;
    }

    /* --- ŠTÝL TLAČIDIEL (Indigo modrá, Plne zaoblená z image_9.png) --- */
    div.stButton > button {
        width: 100% !important;
        max-width: 320px !important; /* Presná šírka pre biele bubliny */
        background: linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%) !important;
        color: white !important;
        border: none !important;
        padding: 16px !important;
        border-radius: 50px !important; /* Maximálne zaoblenie z image_9.png */
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: 0.3s all;
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 15px !important; /* Odstup pod sebou */
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3);
    }
    div.stButton > button:hover {
        opacity: 0.9;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(79, 70, 229, 0.4);
    }

    /* Schovanie dekorácií Streamlit */
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
</style>
""", unsafe_allow_html=True)

# --- 4. FUNKCIA PRE ZOBRAZENIE LOGA ---
def render_logo():
    # Použijeme SVG pre perfektnú ostrosť loga (kompas z image_9.png)
    logo_svg = """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" style="width: 120px; height: 120px; display: block; margin: 0 auto;">
            <circle cx="50" cy="50" r="45" stroke="#E5E7EB" stroke-width="1.5" fill="white" />
            <path d="M50 15 L56 38 H80 L62 52 L68 75 L50 61 L32 75 L38 52 L20 38 H44 Z" fill="#4F46E5" />
            <circle cx="50" cy="50" r="3" fill="#111827" />
        </svg>
    """
    st.markdown(logo_svg, unsafe_allow_html=True)

# --- 5. OBSAH STRÁNKY (VYCENTROVANÝ) ---
# Hlavný kontajner pre stred
st.markdown('<div class="main-center-container">', unsafe_allow_html=True)

# Zobrazenie LOGA (Vycentrované)
render_logo()

# Zobrazenie NÁZVU A TEXTU (Vycentrované)
st.markdown('<div class="brand-header">OMNITRAVEL</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-sub">Zaregistrujte sa a objavujte svet bez hraníc</div>', unsafe_allow_html=True)

# Zobrazenie TLAČIDIEL (Pod sebou, Indigo modrá, Plne zaoblené)
# Použil som text z tvojho obrázka
if st.button("PRIHLÁSIŤ"):
    st.info("Sekcia PRIHLÁSIŤ sa pripravuje.")
    
if st.button("REGISTROVAŤ"):
    st.info("Sekcia REGISTROVAŤ sa pripravuje.")

# Koniec kontajnera
st.markdown('</div>', unsafe_allow_html=True)
