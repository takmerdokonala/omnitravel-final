import streamlit as st

# --- 1. KONFIGURÁCIA ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# --- 2. PAMÄŤ ---
if 'is_registered' not in st.session_state: st.session_state.is_registered = False
if 'user_data' not in st.session_state:
    st.session_state.user_data = {"name": "", "city": "", "wheelchair": False}

# --- 3. LOGO (SVG GRAFIKA - Kompas z tvojho návrhu) ---
logo_html = """
<div style="text-align: center; margin-bottom: 20px;">
    <svg width="120" height="120" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="48" stroke="#1E293B" stroke-width="2"/>
        <circle cx="50" cy="50" r="40" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="4 2"/>
        <path d="M50 15L58 45L50 40L42 45L50 15Z" fill="#4F46E5"/>
        <path d="M50 85L42 55L50 60L58 55L50 85Z" fill="#94A3B8"/>
        <circle cx="50" cy="50" r="4" fill="#1E293B"/>
        <path d="M20 50H30M70 50H80M50 20V30M50 70V80" stroke="#1E293B" stroke-width="2" stroke-linecap="round"/>
    </svg>
    <h1 style="font-family: 'Plus Jakarta Sans', sans-serif; color: #1E293B; letter-spacing: 2px; margin-top: 10px;">
        OMNI<span style="font-weight: 300; color: #64748B;">TRAVEL</span>
    </h1>
    <p style="color: #94A3B8; font-size: 0.9rem; margin-top: -10px;">Vaše dobrodružstvo začína.</p>
</div>
"""

# --- 4. DIZAJN (CSS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }
    
    .stApp { background: white !important; }

    /* Karta registrácie */
    .auth-card {
        background: #FFFFFF;
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 15px 50px rgba(0,0,0,0.06);
        border: 1px solid #F1F5F9;
        text-align: center;
    }

    /* Vstupné polia */
    div[data-baseweb="input"] {
        border-radius: 15px !important;
        background-color: #F8FAFC !important;
        border: 1px solid #E2E8F0 !important;
    }

    /* Tlačidlo */
    div.stButton > button {
        width: 100%;
        background: #1E293B !important;
        color: white !important;
        padding: 15px !important;
        border-radius: 15px !important;
        font-weight: 600 !important;
        border: none !important;
        transition: 0.3s;
    }
    div.stButton > button:hover { background: #334155 !important; transform: translateY(-2px); }
</style>
""", unsafe_allow_html=True)

# --- 5. OBSAH ---
if not st.session_state.is_registered:
    st.markdown("<div style='height:50px'></div>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.5, 1])
    
    with col:
        # Zobrazenie LOGA
        st.markdown(logo_html, unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="auth-card">', unsafe_allow_html=True)
            name = st.text_input("Meno", placeholder="napr. Alex")
            email = st.text_input("E-mail", placeholder="alex@priklad.sk")
            pwd = st.text_input("Heslo", type="password")
            
            st.write("")
            if st.button("ZAREGISTROVAŤ SA"):
                if name and email and pwd:
                    st.session_state.user_data["name"] = name
                    st.session_state.is_registered = True
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
else:
    # Hlavná obrazovka po prihlásení
    st.sidebar.markdown(logo_html.replace('120', '50'), unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center; margin-top:50px;'>Vitaj, {st.session_state.user_data['name']}! 🌍</h2>", unsafe_allow_html=True)
    if st.button("Odhlásiť sa"):
        st.session_state.is_registered = False
        st.rerun()
