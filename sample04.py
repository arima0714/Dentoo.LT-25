# sample04.py
import streamlit as st

check1 = st.checkbox("選択肢1")
check2 = st.checkbox("選択肢2")
check3 = st.checkbox("選択肢3")

if check1:
    st.write("you checked 1")
if check2:
    st.write("you checked 2")
if check3:
    st.write("you checked 3")
