import streamlit as st
import base64
import requests
from groq import Groq

# --- KONFIGURÁCIA ---
st.set_page_config(page_title="OmniTravel Ultra", layout="wide")

# Inicializácia klientov
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]

# --- MAGICKÉ ČIERNE POZADIE S POHYBLIVÝMI TVARMI ---
st.markdown("""
<style>
    .stApp { background: black; color: white; }
    
    /* Animácia stúpajúcich fialových častíc */
    @keyframes move {
        from { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        to { transform: translateY(-10vh) rotate(360deg); opacity: 0.8; }
    }
    
    .shape {
        position: fixed;
        background: rgba(138, 43, 226, 0.4);
        border-radius: 3px; /* Malé fialové štvorčeky/tvary */
        z-index: -1;
        animation: move linear infinite;
    }

    .result-card {
        background: rgba(25, 25, 25, 0.9);
        border: 1px solid #8A2BE2;
        padding: 15px;
        border-radius: 12px;
        margin: 10px 0;
    }
    
    .login-btn { 
        display: block; width: 100%; padding: 10px; margin: 8px 0; 
        text-align: center; border-radius: 8px; text-decoration: none; 
        font-weight: bold; font-size: 14px; 
    }
    .google-btn { background: white; color: black; }
    .apple-btn { background: #333; color: white; }
</style>

<div class="shape" style="left:10%; width:10px; height:10px; animation-duration:15s; animation-delay:0s;"></div>
<div class="shape" style="
