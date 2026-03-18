import streamlit as st
import math
from PIL import Image # Pre manipuláciu s fotkou

# --- 1. KONFIGURÁCIA STRÁNKY ---
st.set_page_config(
    page_title="OmniTravel - Profil Cestovateľa", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. SESSION STATE (PAMÄŤ APPKY) ---
if 'step' not in st.session_state: st.session_state.step = "login"
if 'user_name' not in st.session_state: st.session_state.user_name = "Ocko Cestovateľ"
if 'user_bio' not in st.session_state: st.session_state.user_bio = "Cestujem. Objavujem. Skenujem. AI je môj kompas. 🌍🤖☕"
# Predvolená fotka, ak ocko nahrá vlastnú, prepíše sa
if 'profile_photo' not in st.session_state: st.session_state.profile_photo = None 

# Štatistiky
if 'scans_count' not in st.session_state: st.session_state.scans_count = 12
if 'posts_count' not in st.session_state: st.session_state.posts_count = 3

# --- 3. DIZAJN (CSS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;500;700&display=swap');
    .stApp { background-color: #FFFFFF !important; color: #1A1A1A !important; font-family: 'Quicksand', sans-serif !important; }
    
    /* Menu Fix */
    [data-testid="stSidebar"] { background-color: #FFFFFF !important; border-right: 1px solid #F0F0F0; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label {
        color: #4B0082 !important; font-weight: 600 !important;
    }

    h1, h2, h3 { color: #8A2BE2 !important; font-weight: 700; }
    .omni-card {
        background: #FFFFFF; border: 1px solid #F0F0F0; padding: 25px; 
        border-radius: 20px; margin-bottom: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.04);
    }
    .stat-box { text-align: center; padding: 10px; border-right: 1px solid #F0F0F0; }
    .stat-box:last-child { border-right: none; }
    
    /* Okrúhla profilovka */
    .profile-pic {
        width: 100px; height: 100px; border-radius: 50%; object-fit: cover;
        border: 3px solid #8A2BE2;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================================
# 4. LOGIKA STRÁNOK
# =========================================================================

if st.session_state.step == "login":
    st.write("##")
    st.markdown('<div style="text-align: center; padding-top: 50px;">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/fluency/96/000000/globe-earth.png", width=100)
    st.title("OmniTravel Community 2026")
    if st.button("✨ Vstúpiť do profilu"): 
        st.session_state.step = "app"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == "app":
    with st.sidebar:
        st.markdown('<h2>💜 OmniTravel</h2>', unsafe_allow_html=True)
        st.write("---")
        stranka = st.radio("NAVIGÁCIA", ["📸 Komunita", "🗺️ Mapa", "🤖 AI Skener", "👤 Môj Profil"])
        if st.button("Odhlásiť sa"):
            st.session_state.step = "login"
            st.rerun()

    # --- A. KOMUNITA (Prepojenie s profilom) ---
    if stranka == "📸 Komunita":
        st.title("📸 Čo nové vo svete?")
        
        # Simulujeme profil ocka v komunite
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.session_state.profile_photo:
                st.image(st.session_state.profile_photo, width=60) # Okrúhla fotka
            else:
                st.markdown('<div style="width: 60px; height: 60px; background: #F0F0FF; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 30px;">👨‍✈️</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="omni-card"><b>{st.session_state.user_name}</b> (Ty)<br><small>{st.session_state.user_bio[:30]}...</small><br><br>Testujem môj nový profil! ✨🚀</div>', unsafe_allow_html=True)

    # --- B. MAPA ---
    elif stranka == "🗺️ Mapa":
        st.title("🗺️ Pamiatky v okolí")
        # Centrum NZ
        moje_lat, moje_lon = 47.985, 18.161
        st.markdown(f'<div class="omni-card"><h3>🏛️ Kalvária NZ</h3>Súradnice: <b>47.981, 18.160</b></div>', unsafe_allow_html=True)

    # --- C. AI SKENER ---
    elif stranka == "🤖 AI Skener":
        st.title("🤖 Inteligentný Skener")
        foto = st.camera_input("Odfoťte dokument alebo menu")
        if foto:
            st.session_state.scans_count += 1
            st.success("Menu úspešne pridané do tvojich štatistík!")

    # --- D. MÔJ PROFIL (S FOTKOU A BIO EDITOROM) ---
    elif stranka == "👤 Môj Profil":
        st.title("👤 Tvoj Cestovateľský Profil")
        
        # --- HLAVNÁ KARTA PROFILU (Vizualizácia) ---
        col_img, col_info = st.columns([1, 3])
        with col_img:
            if st.session_state.profile_photo:
                # Používame PIL na zabezpečenie štvorcového výrezu a okrúhlosti cez CSS
                img = Image.open(st.session_state.profile_photo)
                # Tu by išla pokročilejšia Pillow mágia na orezanie, pre MVP stačí CSS
                st.image(img, width=100)
                # Na mobiloch Streamlit niekedy ignoruje CSS na zaoblenie pri st.image,
                # preto v reálnej appke používame Pillow na orezanie fotky do kruhu.
                # Pre prototyp to necháme takto, ocko pochopí, že to bude kruh.
            else:
                # Predvolený avatar
                st.markdown('<div style="width: 100px; height: 100px; background: #F0F0FF; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 50px; border: 3px solid #8A2BE2;">👨‍✈️</div>', unsafe_allow_html=True)
        
        with col_info:
            st.markdown(f"""
            <div class="omni-card" style="box-shadow: none; border: none; padding: 0;">
                <h2 style="margin:0;">{st.session_state.user_name}</h2>
                <p style="color: #666; margin:0;">{st.session_state.user_bio}</p>
            </div>
            """, unsafe_allow_html=True)

        # --- ŠTATISTIKY PROFILU ---
        st.markdown(f"""
        <div class="omni-card">
            <div style="display: flex; justify-content: space-around;">
                <div class="stat-box"><b>{st.session_state.scans_count}</b><br><small>Skeny</small></div>
                <div class="stat-box"><b>{st.session_state.posts_count}</b><br><small>Príspevky</small></div>
                <div class="stat-box"><b>Level 4</b><br><small>Prieskumník</small></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # --- UPRAVIŤ PROFIL (Editor) ---
        with st.expander("⚙️ Upraviť profil (Foto, Meno, Bio)"):
            st.write("###")
            
            # 1. Nahrávanie Profilovej Fotky
            nová_fotka = st.file_uploader("Nahrať profilovú fotku (PNG, JPG)", type=['png', 'jpg', 'jpeg'])
            
            # 2. Meno a Bio
            novy_nick = st.text_input("Meno / Prezývka", st.session_state.user_name)
            nove_bio = st.text_area("O mne / Bio (Tvoje motto)", st.session_state.user_bio, height=100, max_chars=150)
            
            if st.button("Uložiť zmeny"):
                # Ak nahral novú fotku, prepíšeme predvolenú
                if nová_fotka:
                    st.session_state.profile_photo = nová_fotka
                    st.success("Fotka bola nahraná!")
                
                # Uložíme meno a bio
                st.session_state.user_name = novy_nick
                st.session_state.user_bio = nove_bio
                st.success("Profil úspešne aktualizovaný!")
                st.rerun()

        # DOSIAHNUTÉ ODZNAKY
        st.write("### 🏅 Tvoje Odznaky")
        col_o1, col_o2, col_o3 = st.columns(3)
        with col_o1: st.markdown('<div class="omni-card" style="text-align:center;">📸<br><small>Prvá fotka</small></div>', unsafe_allow_html=True)
        with col_o2: st.markdown('<div class="omni-card" style="text-align:center;">🌍<br><small>Svetobežník</small></div>', unsafe_allow_html=True)
        with col_o3: st.markdown('<div class="omni-card" style="text-align:center; opacity:0.3;">✨<br><small>AI Legenda</small></div>', unsafe_allow_html=True)
