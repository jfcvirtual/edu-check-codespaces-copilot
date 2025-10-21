"""
App mínima para verificar Codespaces + Python + Streamlit.
Muestra info del entorno y ejecuta un cálculo simple.
"""
import platform
import sys
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="USCO • Verificación", layout="centered")
st.title("✅ Verificación: Codespaces + Python + Streamlit")

# 1) Entorno
st.subheader("Entorno")
st.write({
    "python": sys.version.split()[0],
    "platform": platform.platform(),
    "processor": platform.processor() or "N/D"
})

# 2) Cálculo rápido
st.subheader("Cálculo NumPy")
x = np.linspace(0, 2*np.pi, 50)
st.line_chart(np.sin(x))

# 3) DataFrame demo
st.subheader("Pandas")
df = pd.DataFrame({"x": x, "sin(x)": np.sin(x)})
st.dataframe(df.head())

st.success("Si ve esta página, Codespaces y Streamlit funcionan.")
