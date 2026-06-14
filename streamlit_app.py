import streamlit as st

# 1. Konfiguracja strony (musi być jako pierwsza funkcja Streamlit w kodzie)
st.set_page_config(
    page_title="Moja Czysta Aplikacja",
    page_icon="📄",
    layout="wide", # Opcje: "centered" (wyśrodkowany) lub "wide" (szeroki)
    initial_sidebar_state="collapsed" # Opcje: "auto", "expanded", "collapsed"
)

# 2. Ukrywanie domyślnych elementów Streamlit (Menu, Stopka, Header)
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    #stDecoration {display:none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- TUTAJ ZACZYNA SIĘ TWOJA CZYSTA STRONA ---

st.title("Czysta strona startowa")
st.write("Twoja aplikacja jest gotowa do rozbudowy. Zacznij dodawać komponenty poniżej.")

# Przykład dodania elementów w kolumnach dla testu:
col1, col2 = st.columns(2)
with col1:
    st.subheader("Kolumna A")
    # Twój kod...

with col2:
    st.subheader("Kolumna B")
    # Twój kod...