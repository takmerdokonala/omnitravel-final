import streamlit as st
import os

# --- 1. KONFIGURÁCIA (Musí byť úplne hore!) ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# --- 2. PAMÄŤ A STAV (Trvalé úložisko pre reláciu) ---
if 'is_registered' not in st.session_state: st.session_state.is_registered = False
if 'auth_mode' not in st.session_state: st.session_state.auth_mode = "register" # register / login
if 'lang' not in st.session_state: st.session_state.lang = "Slovenčina"
if 'page' not in st.session_state: st.session_state.page = "home"
if 'user_data' not in st.session_state:
    st.session_state.user_data = {"name": "", "city": "", "wheelchair": False, "email": ""}

# --- 3. SLOVNÍK PREKLADOV (Aby to fungovalo aj po slovensky) ---
translations = {
    "Slovenčina": {
        "reg": "Registrácia", "log": "Prihlásenie", "submit_reg": "DOKONČIŤ REGISTRÁCIU", "submit_log": "PRIHLÁSIŤ SA",
        "email_p": "meno@priklad.com", "pass_p": "Zadajte silné heslo",
        "name_p": "napr. Peter", "city_p": "napr. Košice",
        "wc": "♿ Vyžadujem bezbariérový prístup", "welcome": "Vitajte späť!", "explore": "Zaregistrujte sa a objavujte svet bez hraníc"
    }
}
T = translations["Slovenčina"]

# --- 4. DIZAJN (CSS pre moderný a sociálny vibe) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }
    .stApp { background-color: #FFFFFF !important; }

    /* Centrujúca karta pre autentifikáciu (Login/Register) */
    .auth-card {
        background: white;
        padding: 50px 40px;
        border-radius: 32px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.05);
        border: 1px solid #F0F2F6;
        max-width: 480px;
        margin: auto;
        text-align: center;
    }

    /* Moderné vstupné polia (Ako iOS) */
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

    /* Moderné tlačidlá (Fialový gradient s tieňom) */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%) !important;
        color: white !important;
        border: none !important;
        padding: 14px !important;
        border-radius: 16px !important;
        font-weight: 600 !important;
        transition: 0.3s all;
        margin-top: 10px;
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3);
    }
    div.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(79, 70, 229, 0.4); }

    /* Prepínač medzi Loginom a Registráciou (Ako sociálne siete) */
    .auth-tabs {
        display: flex; gap: 10px; justify-content: center; margin-bottom: 25px;
        background: #F4F7FB; padding: 6px; border-radius: 15px;
    }
    .auth-tab {
        flex: 1; padding: 10px; border-radius: 12px; font-weight: 600; color: #6B7280;
        transition: 0.2s;
    }
    .auth-tab:hover { background: #E0E7FF; color: #4F46E5; }
</style>
""", unsafe_allow_html=True)

# =========================================================================
# 5. LOGIKA AUTENTIFIKÁCIE S LOGOM
# =========================================================================
if not st.session_state.is_registered:
    # --- LOGO (SVG ktoré som vytvoril) ---
    st.markdown("<div style='height:80px'></div>", unsafe_allow_html=True)
    logo_svg = """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" style="width: 120px; height: 120px; display: block; margin: 0 auto 30px;">
            <defs>
                <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:#4F46E5;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:#7C3AED;stop-opacity:1" />
                </linearGradient>
            </defs>
            <circle cx="50" cy="50" r="45" stroke-width="1.5" stroke="#E5E7EB" fill="white" />
            <circle cx="50" cy="50" r="42" stroke-width="1" stroke="#F0F2F6" fill="white" />
            <path d="M50 15 L56 38 H80 L62 52 L68 75 L50 61 L32 75 L38 52 L20 38 H44 Z" fill="url(#grad)" />
            <text x="50" y="93" text-anchor="middle" font-size="12" font-weight="700" fill="#111827">OMNITRAVEL</text>
        </svg>
    """
    st.markdown(logo_svg, unsafe_allow_html=True)
    
    # --- Centrujúci stĺpec pre kartu ---
    _, col, _ = st.columns([1, 2, 1])
    
    with col:
        with st.container():
            st.markdown('<div class="auth-card">', unsafe_allow_html=True)
            
            # --- PREPÍNAČ MODULOV (Registrácia / Prihlásenie) ---
            st.markdown('<div class="auth-tabs">', unsafe_allow_html=True)
            r_col, l_col = st.columns(2)
            with r_col:
                if st.button(T["reg"], key="reg_btn", help="Prepnúť na registráciu"):
                    st.session_state.auth_mode = "register"
            with l_col:
                if st.button(T["log"], key="log_btn", help="Prepnúť na prihlásenie"):
                    st.session_state.auth_mode = "login"
            st.markdown('</div>', unsafe_allow_html=True)

            # --- SAMOTNÉ FORMULÁRE (Preklad pod logom) ---
            if st.session_state.auth_mode == "register":
                st.markdown(f"<p style='color:#6B7280; margin-bottom:30px;'>{T['explore']}</p>", unsafe_allow_html=True)
                with st.form("complete_registration", clear_on_submit=False):
                    email = st.text_input("E-mailová adresa", placeholder=T["email_p"])
                    pwd = st.text_input("Heslo", type="password", placeholder=T["pass_p"])
                    st.write("---")
                    name = st.text_input("Meno", placeholder=T["name_p"])
                    city = st.text_input("Mesto", placeholder=T["city_p"])
                    wc = st.toggle(T["wc"])
                    if st.form_submit_button(T["submit_reg"]):
                        if email and pwd and name:
                            st.session_state.user_data.update({"name": name, "city": city, "wheelchair": wc, "email": email})
                            st.session_state.is_registered = True
                            st.balloons()
                            st.rerun()
                        else: st.error("Prosím, vyplňte meno, e-mail a heslo.")
            else:
                st.markdown(f"<p style='color:#6B7280; margin-bottom:30px;'>{T['welcome']}</p>", unsafe_allow_html=True)
                with st.form("simple_login", clear_on_submit=False):
                    email_login = st.text_input("E-mailová adresa", placeholder=T["email_p"])
                    pass_login = st.text_input("Heslo", type="password", placeholder=T["pass_p"])
                    if st.form_submit_button(T["submit_log"]):
                        # Jednoduchá kontrola pre demo (Ak má meno, pustíme ho)
                        if email_login and pass_login and st.session_state.user_data["name"] != "":
                            st.session_state.is_registered = True
                            st.rerun()
                        else: st.error("Nesprávne údaje alebo profil neexistuje.")
            st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# 6. HLAVNÁ APLIKÁCIA (Po autentifikácii)
# =========================================================================
else:
    # Sidebar menu s logom
    with st.sidebar:
        st.markdown('<div style="display:flex; align-items:center; gap:10px; margin-bottom:20px;">' + logo_svg.replace('width: 120px; height: 120px;', 'width: 40px; height: 40px;').replace('font-size: 12', 'font-size: 10').replace('display: block; margin: 0 auto 30px;', 'margin: 0;') + '</div>', unsafe_allow_html=True)
        st.write(f"### Ahoj, {st.session_state.user_data['name']}!")
        st.write("---")
        if st.button("🚪 Odhlásiť sa"):
            st.session_state.is_registered = False
            st.session_state.auth_mode = "register" # Vrátime na registráciu
            st.rerun()

    # Obsah
    st.markdown(f"<h1 style='text-align:center; margin-top:50px;'>Vitajte v OmniTravel</h1>", unsafe_allow_html=True)
    st.write(f"<p style='text-align:center; color:#6B7280;'>Váš účet: {st.session_state.user_data['email']}</p>", unsafe_allow_html=True)
