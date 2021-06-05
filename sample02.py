# sample02.py
import streamlit as st
import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot([1,2,3,4],[8,6,7,5])
st.pyplot(fig)
