# --- 2. ROZŠÍRENÝ SLOVNÍK (Pridané preklady pre bezbariérovosť) ---
# Doplň toto do svojho existujúceho slovníka translations pre každý jazyk
translations = {
    "Slovenčina": {
        # ... predošlé preklady ...
        "wheelchair": "BEZBARIÉROVÝ PRÍSTUP",
        "save": "ULOŽIŤ PROFIL",
        "edit": "UPRAVIŤ PROFIL"
    },
    "English": {
        # ... predošlé preklady ...
        "wheelchair": "WHEELCHAIR ACCESSIBILITY",
        "save": "SAVE PROFILE",
        "edit": "EDIT PROFILE"
    }
    # Podobne doplň pre ostatné jazyky...
}

# --- 3. PAMÄŤ (Pridaný stav pre bezbariérovosť) ---
if 'user_data' not in st.session_state:
    st.session_state.user_data = {
        "name": "",
        "bio": "",
        "city": "",
        "interests": [],
        "wheelchair": False  # Nové pole
    }

# ... (ponechaj predošlé CSS a SIDEBAR) ...

# --- 7. OBSAH (Sekcia PROFIL) ---
if page == "profile":
    T = translations[st.session_state.lang]
    
    if st.session_state.user_data["name"] == "":
        st.subheader("Vytvorte si svoj profil")
        
        with st.form("profile_form"):
            new_name = st.text_input("Meno")
            new_city = st.text_input("Mesto")
            
            # Pridanie prepínača pre bezbariérový prístup
            st.write("---")
            is_wheelchair = st.toggle(T["wheelchair"], value=st.session_state.user_data["wheelchair"])
            st.write("---")
            
            new_interests = st.multiselect("Záujmy", options=["Gastro", "Príroda", "Kultúra"])
            
            submit = st.form_submit_button(T["save"])
            
            if submit and new_name:
                st.session_state.user_data.update({
                    "name": new_name,
                    "city": new_city,
                    "wheelchair": is_wheelchair,
                    "interests": new_interests
                })
                st.rerun()
    else:
        # Zobrazenie profilu s ikonkou bezbariérovosti
        col1, col2 = st.columns([1, 2])
        with col2:
            st.markdown(f"## {st.session_state.user_data['name']}")
            
            # Ak je zapnutý bezbariérový prístup, zobrazíme to viditeľne
            if st.session_state.user_data["wheelchair"]:
                st.markdown("♿ **Bezbariérové trasy zapnuté**")
            
            st.markdown(f"📍 {st.session_state.user_data['city']}")
            
            if st.button(T["edit"]):
                st.session_state.user_data["name"] = ""
                st.rerun()
