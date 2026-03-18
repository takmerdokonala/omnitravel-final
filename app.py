import streamlit as st

# --- 1. KONFIGURÁCIA ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CSS DIZAJN (Presná kópia z 1000116064.jpg) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700&display=swap');
    
    html, body, [class*="css"] { 
        font-family: 'Plus Jakarta Sans', sans-serif !important; 
        background-color: #FFFFFF !important;
    }

    /* Vycentrovanie celého obsahu na stred */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        height: 90vh;
        width: 100%;
    }

    /* Štýl nápisu OMNITRAVEL */
    .brand-title {
        font-weight: 700;
        font-size: 2.8rem;
        color: #1E293B;
        margin-top: 20px;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }

    /* Sivý podnadpis */
    .brand-subtitle {
        color: #94A3B8;
        font-size: 1.1rem;
        margin-bottom: 50px;
    }

    /* Fialové pilulkové tlačidlá */
    div.stButton > button {
        width: 320px !important;
        background: linear-gradient(90deg, #9491FF 0%, #7366FF 100%) !important;
        color: white !important;
        padding: 18px !important;
        border-radius: 50px !important; /* Pilulkový tvar */
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        border: none !important;
        margin: 10px auto !important;
        display: block;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(115, 102, 255, 0.2);
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(115, 102, 255, 0.4);
        opacity: 0.9;
    }

    /* Odstránenie Streamlit lišty hore */
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
</style>
""", unsafe_allow_html=True)

# --- 3. OBSAH (Logo, Text a Tlačidlá) ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# LOGO (Modrá hviezda v kruhu - presne podľa 1000116064.jpg)
st.markdown("""
    <svg width="130" height="130" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-bottom: 10px;">
        <circle cx="50" cy="50" r="48" stroke="#1E293B" stroke-width="1.5"/>
        <circle cx="50" cy="50" r="43" stroke="#1E293B" stroke-width="1"/>
        <path d="M50 20L56 44L80 50L56 56L50 80L44 56L20 50L44 44L50 20Z" fill="#5F52FF"/>
        <circle cx="50" cy="50" r="5" fill="#1E293B"/>
        <circle cx="50" cy="50" r="2" fill="white"/>
    </svg>
""", unsafe_allow_html=True)

st.markdown('<h1 class="brand-title">OMNITRAVEL</h1>', unsafe_allow_html=True)
st.markdown('<p class="brand-subtitle">Zaregistrujte sa a objavujte svet bez hraníc</p>', unsafe_allow_html=True)

# TLAČIDLÁ (Fialové pilulky pod sebou)
if st.button("PRIHLÁSIŤ"):
    st.switch_page("pages/login.py") # Príklad navigácie

if st.button("REGISTROVAŤ"):
    st.switch_page("pages/register.py")

st.markdown('</div>', unsafe_allow_html=True)
