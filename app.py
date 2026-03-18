import streamlit as st

# --- 1. KONFIGURÁCIA ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# --- 2. PAMÄŤ ---
if 'is_registered' not in st.session_state: st.session_state.is_registered = False
if 'lang' not in st.session_state: st.session_state.lang = "Slovenčina"
if 'page' not in st.session_state: st.session_state.page = "home"
if 'user_data' not in st.session_state:
    st.session_state.user_data = {"name": "", "city": "", "wheelchair": False, "email": ""}

# --- 3. DIZAJN (Moderný & Sociálny) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }
    
    .stApp { background: #FFFFFF !important; }

    /* Centrujúca karta pre registráciu */
    .auth-card {
        background: white;
        padding: 40px;
        border-radius: 28px;
        box-shadow: 0 15px 50px rgba(0,0,0,0.05);
        border: 1px solid #F0F2F6;
        max-width: 450px;
        margin: auto;
    }

    /* Moderné tlačidlá */
    div.stButton > button {
        background: linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%) !important;
        color: white !important;
        border: none !important;
        padding: 14px !important;
        border-radius: 16px !important;
        font-weight: 600 !important;
        transition: 0.3s;
    }
    div.stButton > button:hover { transform: scale(1.02); opacity: 0.9; }
</style>
""", unsafe_allow_html=True)

# --- 4. LOGIKA REGISTRÁCIE ---
if not st.session_state.is_registered:
    st.markdown("<div style='height:80px'></div>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 2, 1])
    
    with col:
        st.markdown("<h1 style='text-align:center; color:#4F46E5; margin-bottom:10px;'>OmniTravel</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#6B7280; margin-bottom:30px;'>Zaregistrujte sa a objavujte svet bez hraníc</p>", unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="auth-card">', unsafe_allow_html=True)
            reg_email = st.text_input("E-mailová adresa", placeholder="meno@priklad.com")
            reg_password = st.text_input("Heslo", type="password")
            st.write("---")
            
            # Profilové údaje hneď pri registrácii
            reg_name = st.text_input("Vaše meno", placeholder="napr. Peter")
            reg_city = st.text_input("Domovské mesto", placeholder="napr. Košice")
            reg_wc = st.toggle("♿ Vyžadujem bezbariérový prístup")
            
            st.write("")
            if st.button("DOKONČIŤ REGISTRÁCIU"):
                if reg_email and reg_password and reg_name:
                    st.session_state.user_data.update({
                        "name": reg_name, "city": reg_city, 
                        "wheelchair": reg_wc, "email": reg_email
                    })
                    st.session_state.is_registered = True
                    st.balloons()
                    st.rerun()
                else:
                    st.error("Prosím, vyplňte meno a e-mail.")
            st.markdown('</div>', unsafe_allow_html=True)

# --- 5. HLAVNÁ APLIKÁCIA (Po registrácii) ---
else:
    # Sidebar menu
    with st.sidebar:
        st.markdown(f"<h3 style='color:#4F46E5;'>Ahoj, {st.session_state.user_data['name']}!</h3>", unsafe_allow_html=True)
        if st.button("🏠 Domov"): st.session_state.page = "home"
        if st.button("👤 Môj Profil"): st.session_state.page = "profile"
        if st.button("📸 Scanner"): st.session_state.page = "scanner"
        st.write("---")
        if st.button("Odhlásiť sa"):
            st.session_state.is_registered = False
            st.rerun()

    # Obsah stránky
    if st.session_state.page == "home":
        st.markdown(f"<h1 style='text-align:center; margin-top:50px;'>Vitajte v OmniTravel</h1>", unsafe_allow_html=True)
        st.info(f"Ste prihlásený ako: {st.session_state.user_data['email']}")
    
    elif st.session_state.page == "profile":
        _, col, _ = st.columns([1, 2, 1])
        with col:
            st.markdown(f"""
                <div style="background:white; padding:30px; border-radius:24px; box-shadow:0 10px 30px rgba(0,0,0,0.05); text-align:center; border: 1px solid #F0F2F6;">
                    <div style="width:80px; height:80px; background:#4F46E5; border-radius:50%; margin: 0 auto 15px; display:flex; align-items:center; justify-content:center; color:white; font-size:30px;">
                        {st.session_state.user_data['name'][0].upper()}
                    </div>
                    <h2>{st.session_state.user_data['name']}</h2>
                    <p>📍 {st.session_state.user_data['city']}</p>
                    {"<p>♿ Bezbariérový režim</p>" if st.session_state.user_data['wheelchair'] else ""}
                </div>
            """, unsafe_allow_html=True)
