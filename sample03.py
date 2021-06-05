# sample03.py

import streamlit as st

option = st.selectbox("select your university", ["UEC", "電気通信大学", "多摩のMIT"])

st.write(f"You selected: {option}")
