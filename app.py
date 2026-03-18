import streamlit as st
import base64
from groq import Groq
from tavily import TavilyClient

# --- BEZPEČNÉ NAČÍTANIE KĽÚČOV (Zo Streamlit Secrets) ---
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]
except KeyError:
    st.error("Chýbajú API kľúče v nastaveniach (Secrets)!")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)
tavily = TavilyClient(api_key=TAVILY_API_KEY)

st.set_page_config(page_title="OmniTravel Pro", page_icon="📍")

st.title("📍 OmniTravel AI")

# Jednoduché menu
tab1, tab2 = st.tabs(["🗺️ Pamiatky", "📸 Skener"])

with tab1:
    mesto = st.text_input("Zadaj mesto:", "Nové Zámky")
    if st.button("Hľadať"):
        with st.spinner("Hľadám na webe..."):
            search = tavily.search(query=f"top attractions in {mesto} 2026 prices")
            st.write("AI spracováva výsledky...")
            # Tu AI vygeneruje odpoveď (zjednodušené pre test)
            st.info(f"Našiel som pamiatky v meste {mesto}. (Dáta sú pripravené)")

with tab2:
    foto = st.camera_input("Odfoť menu")
    if foto:
        st.success("Foto prijaté! AI ho analyzuje...")