import streamlit as st
import os

# --- 1. KONFIGURÁCIA ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# --- 2. PAMÄŤ A STAV ---
if 'is_registered' not in st.session_state: st.session_state.is_registered = False
if 'auth_mode' not in st.session_state: st.session_state.auth_mode = "welcome" # welcome / login / register
if 'lang' not in st.session_state: st.session_state.lang = "Slovenčina"
if 'page' not in st.session_state: st.session_state.page = "home"
if 'user_data' not in st.session_state:
    st.session_state.user_data = {"name": "", "city": "", "wheelchair": False, "email": ""}

# --- 3. SLOVNÍK PREKLADOV (SK/EN) ---
translations = {
    "Slovenčina": {
        "welcome": "Vitajte", "reg_desc": "Zaregistrujte sa a objavujte svet",
        "email_p": "meno@priklad.com", "pass_p": "Zadajte silné heslo",
        "name_p": "napr. Peter", "city_p": "napr. Košice",
        "wc": "♿ Vyžadujem bezbariérový prístup", "submit_reg": "DOKONČIŤ REGISTRÁCIU",
        "reg": "REGISTRÁCIA", "log": "PRIHLÁSENIE", "logout": "Odhlásiť sa",
        "home": "Domov", "profile": "Môj Profil"
    },
    "English": {
        "welcome": "Welcome", "reg_desc": "Sign up and explore the world",
        "email_p": "name@example.com", "pass_p": "Enter strong password",
        "name_p": "e.g., Peter", "city_p": "e.g., Kosice",
        "wc": "♿ Wheelchair access needed", "submit_reg": "COMPLETE REGISTRATION",
        "reg": "REGISTRATION", "log": "LOGIN", "logout": "Logout",
        "home": "Home", "profile": "My Profile"
    }
}
T = translations[st.session_state.lang]

# --- 4. CSS DIZAJN (Moderný, Sociálny, Zaoblený) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }
    .stApp { background-color: #FFFFFF !important; }

    /* Centrujúci kontajner (Pre úvod aj formuláre) */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin-top: 80px;
    }

    /* Karta registrácie / prihlásenia (Biely iOS štýl) */
    .auth-card {
        background: white;
        padding: 50px 40px;
        border-radius: 32px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.05);
        border: 1px solid #F0F2F6;
        max-width: 480px;
        margin: auto;
    }

    /* Moderné vstupné polia (iOS/iPhone dizajn) */
    div[data-baseweb="input"] {
        border-radius: 14px !important;
        background-color: #F4F7FB !important;
        border: 1px solid transparent !important;
        padding: 4px !important;
    }
    div[data-baseweb="input"]:focus-within {
        border-color: #4F46E5 !important;
        background-color: white !important;
    }

    /* Moderné tlačidlá (Fialový gradient s tieňom a zaoblením) */
    div.stButton > button {
        width: 100% !important;
        max-width: 300px !important;
        background: linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%) !important;
        color: white !important;
        border: none !important;
        padding: 14px !important;
        border-radius: 16px !important;
        font-weight: 600 !important;
        transition: 0.3s all;
        margin-bottom: 15px !important;
        display: block;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3);
    }
    div.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(79, 70, 229, 0.4); }

    /* Schovanie Streamlit dekorácií */
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
</style>
""", unsafe_allow_html=True)

# --- 5. LOGIKA STRÁNOK ---
# Táto funkcia zobrazuje úvodnú obrazovku, ktorú si schválila
def show_welcome():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # SVG LOGO KOMPAS (Z image_6.png)
    st.markdown("""
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" style="width: 100px; height: 100px; display: block; margin: 0 auto 30px;">
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
    
    st.markdown(f"<p style='color:#6B7280; margin-bottom:35px;'>{T['reg_desc']}</p>", unsafe_allow_html=True)
    
    # BIELE BUBLINY (PRIHLÁSENIE / REGISTRÁCIA pod sebou)
    if st.button(T["log"], key="main_log"):
        st.session_state.auth_mode = "login"
        st.rerun()
        
    if st.button(T["reg"], key="main_reg"):
        st.session_state.auth_mode = "register"
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)

# --- 6. AUTENTIFIKÁCIA A FORMULÁRE ---
if not st.session_state.is_registered:
    # --- ÚVODNÁ OBRAZOVKA (Welcome) ---
    if st.session_state.auth_mode == "welcome":
        show_welcome()
    
    # --- FORMULÁRE (Login / Register) ---
    else:
        st.markdown("<div style='height:80px'></div>", unsafe_allow_html=True)
        _, col, _ = st.columns([1, 2, 1])
        
        with col:
            with st.container():
                st.markdown('<div class="auth-card">', unsafe_allow_html=True)
                
                # Zobrazenie prekladu pod logom
                if st.session_state.auth_mode == "register":
                    st.markdown(f"<p style='color:#6B7280; margin-bottom:30px;'>{T['reg_desc']}</p>", unsafe_allow_html=True)
                    # --- FORMULÁR REGISTRÁCIE (S Bezbariérovosťou) ---
                    with st.form("complete_registration", clear_on_submit=False):
                        reg_email = st.text_input("E-mailová adresa", placeholder=T["email_p"])
                        reg_password = st.text_input("Heslo", type="password", placeholder=T["pass_p"])
                        st.write("---")
                        reg_name = st.text_input("Vaše meno", placeholder=T["name_p"])
                        reg_city = st.text_input("Domovské mesto", placeholder=T["city_p"])
                        st.write("")
                        reg_wc = st.toggle(T["wc"], value=st.session_state.user_data["wheelchair"])
                        submit = st.form_submit_button(T["submit_reg"])
                        if submit and reg_email and reg_password and reg_name:
                            st.session_state.user_data.update({"name": reg_name, "city": reg_city, "wheelchair": reg_wc, "email": reg_email})
                            st.session_state.is_registered = True
                            st.rerun()
                else:
                    # --- FORMULÁR PRIHLÁSENIA ---
                    st.markdown(f"<p style='color:#6B7280; margin-bottom:30px;'>{translations[st.session_state.lang]['log']}</p>", unsafe_allow_html=True)
                    with st.form("simple_login", clear_on_submit=False):
                        login_email = st.text_input("E-mailová adresa", placeholder=T["email_p"])
                        login_pwd = st.text_input("Heslo", type="password", placeholder=T["pass_p"])
                        if st.form_submit_button(translations[st.session_state.lang]['log']):
                            if login_email and login_pwd and st.session_state.user_data["name"] != "":
                                st.session_state.is_registered = True
                                st.rerun()
                
                # Tlačidlo späť na úvod
                if st.button("← Späť", key="back_btn"):
                    st.session_state.auth_mode = "welcome"
                    st.rerun()
                
                st.markdown('</div>', unsafe_allow_html=True)

# --- 7. HLAVNÁ APLIKÁCIA (Po autentifikácii) ---
else:
    # Sidebar menu s logom
    with st.sidebar:
        # Mini logo do sidebaru
        st.markdown('<div style="display:flex; align-items:center; gap:10px; margin-bottom:20px;"><div style="width:30px; height:30px; background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%); border-radius:8px; display:flex; align-items:center; justify-content:center; color:white; font-size:15px; font-weight:700;">OT</div><span style="font-size:18px; font-weight:700; color:#111827;">OmniTravel</span></div>', unsafe_allow_html=True)
        st.write(f"### Ahoj, {st.session_state.user_data['name']}!")
        if st.button(f"🏠 {T['home']}"): st.session_state.page = "home"
        if st.button(f"👤 {T['profile']}"): st.session_state.page = "profile"
        st.write("---")
        if st.button(f"🚪 {T['logout']}"):
            st.session_state.is_registered = False
            st.session_state.auth_mode = "welcome" # Vrátime na úvod
            st.rerun()

    # Obsah
    if st.session_state.page == "home":
        st.markdown(f"<h1 style='text-align:center; margin-top:50px; color:#111827;'>{T['home']}</h1>", unsafe_allow_html=True)
        st.write(f"<p style='text-align:center; color:#6B7280;'>Pripravujeme pre vás niečo úžasné, {st.session_state.user_data['name']}!</p>", unsafe_allow_html=True)
