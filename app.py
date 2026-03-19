import streamlit as st

# --- 1. ZÁKLADNÉ NASTAVENIA ---
st.set_page_config(page_title="OmniTravel", layout="wide", initial_sidebar_state="collapsed")

# Načítanie údajov zo Secrets
CLIENT_ID = st.secrets.get("google_client_id", "")
REDIRECT_URI = st.secrets.get("redirect_uri", "")

# --- 2. ŠTÝLOVANIE (CSS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] { 
        font-family: 'Plus Jakarta Sans', sans-serif !important; 
        background-color: #FFFFFF !important; 
    }
    
    .main-container { 
        display: flex; flex-direction: column; align-items: center; justify-content: center; 
        text-align: center; min-height: 80vh; margin: auto; max-width: 500px; 
    }
    
    /* Karty pre menu */
    .menu-card {
        background: #FFFFFF; padding: 20px; border-radius: 20px; 
        border: 1px solid #F1F5F9; box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 15px; text-align: left; transition: 0.3s;
    }
    .menu-card:hover { transform: translateY(-3px); border-color: #4F46E5; }

    .brand-title { font-weight: 700; font-size: 2.2rem; color: #1E293B; margin-top: 10px; }
    
    /* Elegantné tlačidlá */
    div.stButton > button {
        width: 100% !important; background-color: #FFFFFF !important; border-radius: 50px !important; 
        padding: 12px !important; border: 1px solid #E2E8F0 !important; font-weight: 600 !important;
        transition: 0.3s;
    }
    div.stButton > button:hover { border-color: #4F46E5 !important; color: #4F46E5 !important; }

    .google-btn {
        display: inline-block; width: 100%; padding: 14px; background-color: #FFFFFF; color: #1E293B;
        border-radius: 50px; border: 1px solid #E2E8F0; font-weight: 600; text-decoration: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }
</style>
""", unsafe_allow_html=True)

def render_logo():
    st.markdown('<div style="text-align:center;"><svg width="70" height="70" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" stroke="#1E293B" stroke-width="2" fill="none"/><path d="M50 20L60 50L50 45L40 50L50 20Z" fill="#4F46E5"/><path d="M50 80L40 50L50 55L60 50L50 80Z" fill="#94A3B8"/></svg></div>', unsafe_allow_html=True)

# --- 3. LOGIKA APLIKÁCIE ---

# Kontrola, či je používateľ "prihlásený" (máme token v URL)
query_params = st.query_params

if "access_token" in query_params:
    # === OBRAZOVKA PO PRIHLÁSENÍ ===
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    render_logo()
    st.markdown('<h1 class="brand-title">Moje cesty</h1>', unsafe_allow_html=True)
    
    # Ukážka menu kariet
    st.markdown("""
    <div class="menu-card">
        <h4 style="margin:0; color:#1E293B;">🌍 Naplánovať nový výlet</h4>
        <p style="color:#94A3B8; font-size:0.9rem; margin:5px 0 0 0;">Vytvorte si itinerár pomocou AI.</p>
    </div>
    <div class="menu-card">
        <h4 style="margin:0; color:#1E293B;">📸 Moje spomienky</h4>
        <p style="color:#94A3B8; font-size:0.9rem; margin:5px 0 0 0;">Prezrite si fotky z minulých ciest.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("") # Medzera
    
    if st.button("ODHLÁSIŤ SA"):
        st.query_params.clear()
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # === ÚVODNÁ OBRAZOVKA (LOGIN) ===
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    render_logo()
    st.markdown('<h1 class="brand-title">OMNITRAVEL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#94A3B8; margin-bottom:30px;">Vaše dobrodružstvo začína tu.</p>', unsafe_allow_html=True)
    
    # Google link
    login_url = f"https://accounts.google.com/o/oauth2/v2/auth?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=token&scope=openid%20email%20profile"
    
    st.markdown(f'<a href="{login_url}" class="google-btn">Sign in with Google</a>', unsafe_allow_html=True)
    
    st.markdown('<p style="color:#CBD5E1; font-size:0.8rem; margin:20px 0;">ALEBO</p>', unsafe_allow_html=True)
    
    if st.button("POUŽIŤ EMAIL"):
        st.info("E-mailové prihlásenie pripravujeme.")
        
    st.markdown('</div>', unsafe_allow_html=True)
