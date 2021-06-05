# sample01.py
import streamlit as st
import pandas as pd

df = pd.DataFrame([["UEC","電気通信大学"], ["MIT", "マサチューセッツ工科大学"]])
st.table(df)
