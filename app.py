import streamlit as st
import os

# --- 1. KONFIGURÁCIA (Musí byť úplne hore!) ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# --- 2. PAMÄŤ A STAV ---
if 'is_registered' not in st.session_state: st.session_state.is_registered = False
if 'auth_mode' not in st.session_state: st.session_state.auth_mode = "welcome" # welcome / login / register
if 'lang' not in st.session_state: st.session_state.lang = "Slovenčina"
if 'user_data' not in st.session_state:
    st.session_state.user_data = {"name": "", "city": "", "wheelchair": False, "email": ""}

# --- 3. SLOVNÍK PREKLADOV ---
translations = {
    "Slovenčina": {
        "explore": "Zaregistrujte sa a objavujte svet bez hraníc",
        "reg": "REGISTRÁCIA", "log": "PRIHLÁSENIE", "back": "← Späť",
        "email_p": "meno@priklad.com", "pass_p": "Zadajte silné heslo",
        "name_p": "napr. Peter", "wc": "♿ Vyžadujem bezbariérový prístup", "submit_reg": "DOKONČIŤ REGISTRÁCIU"
    }
}
T = translations["Slovenčina"]

# --- 4. CSS DIZAJN (Čistý, Biely, Vycentrovaný) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }
    .stApp { background-color: #FFFFFF !important; }

    /* Hlavný kontajner na vycentrovanie všetkého */
    .main-center-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        min-height: 80vh; /* Zabezpečí stred na výšku */
        width: 100%;
    }

    /* Karta registrácie / prihlásenia (Biely iOS štýl, vycentrovaná) */
    .auth-card {
        background: white;
        padding: 50px 40px;
        border-radius: 32px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.05);
        border: 1px solid #F0F2F6;
        max-width: 450px;
        margin: auto; /* Vycentrovanie v stĺpci */
    }

    /* Vstupné polia */
    div[data-baseweb="input"] {
        border-radius: 14px !important;
        background-color: #F4F7FB !important;
        border: 1px solid transparent !important;
    }
    div[data-baseweb="input"]:focus-within {
        border-color: #4F46E5 !important;
        background-color: white !important;
    }

    /* BIELE BUBLINOVÉ TLAČIDLÁ (Úvodná obrazovka) */
    /* Zacieľujeme na tlačidlá, ktoré NIE SÚ vo formulári */
    div.stButton:not([data-testid="stForm"]) > button {
        width: 100% !important;
        max-width: 320px !important;
        background-color: #FFFFFF !important;
        color: #1E293B !important;
        padding: 18px !important;
        border-radius: 50px !important; /* Maximálne zaoblenie - bublina */
        font-weight: 600 !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
        transition: 0.3s all;
        display: block;
        margin: 10px auto !important; /* Vycentrovanie a odstup pod sebou */
    }
    div.stButton:not([data-testid="stForm"]) > button:hover {
        border-color: #4F46E5 !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.06) !important;
    }

    /* TLAČIDLÁ VO FORMULÁRI (Fialové pre akciu) */
    div[data-testid="stForm"] div.stButton > button {
        background: linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%) !important;
        color: white !important;
        border-radius: 16px !important;
        margin-top: 20px;
    }

    /* Schovanie Streamlit dekorácií */
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
</style>
""", unsafe_allow_html=True)

# --- 5. LOGIKA STRÁNOK S LOGOM KOMPASU ---
if not st.session_state.is_registered:
    # Hlavný flex kontajner pre stred
    st.markdown('<div class="main-center-container">', unsafe_allow_html=True)
    
    # --- ÚVODNÁ OBRAZOVKA (Welcome) ---
    if st.session_state.auth_mode == "welcome":
        
        # 1. Pôvodné SVG LOGO KOMPAS (Z image_6.png, vycentrované)
        # Odstránená hviezda, vrátený kompas
        st.markdown("""
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" style="width: 120px; height: 120px; display: block; margin: 0 auto 30px;">
                <defs>
                    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#4F46E5;stop-opacity:1" />
                        <stop offset="100%" style="stop-color:#7C3AED;stop-opacity:1" />
                    </linearGradient>
                </defs>
                <circle cx="50" cy="50" r="45" stroke-width="1.5" stroke="#E5E7EB" fill="white" />
                <path d="M50 15 L56 38 H80 L62 52 L68 75 L50 61 L32 75 L38 52 L20 38 H44 Z" fill="url(#grad)" />
                <text x="50" y="93" text-anchor="middle" font-size="12" font-weight="700" fill="#111827">OMNITRAVEL</text>
            </svg>
        """, unsafe_allow_html=True)
        
        # 2. Text (vycentrovaný cez CSS)
        st.markdown(f"<p style='color:#6B7280; margin-bottom:45px; max-width:300px; margin-left:auto; margin-right:auto;'>{T['explore']}</p>", unsafe_allow_html=True)
        
        # 3. BIELE BUBLINOVÉ TLAČIDLÁ (Vycentrované a pod sebou cez CSS)
        if st.button(T["log"], key="main_log"):
            st.session_state.auth_mode = "login"
            st.rerun()
            
        if st.button(T["reg"], key="main_reg"):
            st.session_state.auth_mode = "register"
            st.rerun()
            
    # --- FORMULÁRE (Login / Register v bielej karte) ---
    else:
        # Použijeme stĺpec pre kartu, aby bola v strede
        _, col, _ = st.columns([1, 2, 1])
        with col:
            with st.container():
                st.markdown('<div class="auth-card">', unsafe_allow_html=True)
                
                # Tlačidlo späť
                if st.button(T["back"], key="back_btn"):
                    st.session_state.auth_mode = "welcome"
                    st.rerun()
                st.write("---")

                if st.session_state.auth_mode == "register":
                    st.markdown(f"<h3 style='text-align:center;'>{T['reg']}</h3>", unsafe_allow_html=True)
                    # --- FORMULÁR REGISTRÁCIE ---
                    with st.form("complete_registration", clear_on_submit=False):
                        reg_email = st.text_input("E-mailová adresa", placeholder=T["email_p"])
                        reg_password = st.text_input("Heslo", type="password", placeholder=T["pass_p"])
                        st.write("---")
                        reg_name = st.text_input("Vaše meno", placeholder=T["name_p"])
                        st.write("")
                        reg_wc = st.toggle(T["wc"], value=st.session_state.user_data["wheelchair"])
                        submit = st.form_submit_button(T["submit_reg"])
                        if submit and reg_email and reg_password and reg_name:
                            st.session_state.user_data.update({"name": reg_name, "wheelchair": reg_wc, "email": reg_email})
                            st.session_state.is_registered = True
                            st.balloons()
                            st.rerun()
                        elif submit: st.error("Prosím, vyplňte meno, e-mail a heslo.")
                else:
                    # --- FORMULÁR PRIHLÁSENIA ---
                    st.markdown(f"<h3 style='text-align:center;'>{T['log']}</h3>", unsafe_allow_html=True)
                    with st.form("simple_login", clear_on_submit=False):
                        login_email = st.text_input("E-mailová adresa", placeholder=T["email_p"])
                        login_pwd = st.text_input("Heslo", type="password", placeholder=T["pass_p"])
                        if st.form_submit_button(T["log"]):
                            if login_email and login_pwd and st.session_state.user_data["name"] != "":
                                st.session_state.is_registered = True
                                st.rerun()
                            else: st.error("Profil neexistuje alebo zlé údaje.")
                
                st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True) # Koniec main-center-container

# --- 7. HLAVNÁ APLIKÁCIA (Ponechaná) ---
else:
    st.markdown(f"<h1 style='text-align:center; margin-top:50px;'>Vitajte v OmniTravel, {st.session_state.user_data['name']}!</h1>", unsafe_allow_html=True)
    if st.button("🚪 Odhlásiť sa"):
        st.session_state.is_registered = False
        st.session_state.auth_mode = "welcome"
        st.rerun()
