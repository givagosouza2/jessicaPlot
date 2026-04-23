import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")

st.title("Vídeo + Cinemática específica")

video_url = "https://youtu.be/KrsJxEfyyVM"
st.video(video_url)

# Importando apenas colunas específicas
df = pd.read_csv("cinematica.csv", usecols=[0, 9, 10, 11])

df.columns = ["tempo", "x", "y", "z"]
z = df["z"]
t = df["tempo"]
peak_z = np.max(z)
for index,valor in z:
    if valor == peak_z:
        tempo = t - t[index]
        break
# Plot apenas do eixo Z
fig = px.line(
    df,
    x=tempo,
    y=z,
    labels={"tempo": "Tempo (s)", "z": "Amplitude"},
    title="Cinemática - eixo Z"
)

st.plotly_chart(fig, use_container_width=True)
