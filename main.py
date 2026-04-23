import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Vídeo + Cinemática", layout="centered")

st.title("Vídeo e cinemática do movimento")

# URL do vídeo
video_url = "https://youtu.be/KrsJxEfyyVM"
st.video(video_url)

st.subheader("Gráfico da cinemática do movimento")

# Arquivo CSV com os dados cinemáticos
df = pd.read_csv("cinematica.csv")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df["tempo"], df["x"], label="X")
ax.plot(df["tempo"], df["y"], label="Y")
ax.plot(df["tempo"], df["z"], label="Z")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Amplitude")
ax.set_title("Séries temporais da cinemática")
ax.legend()
ax.grid(True)

st.pyplot(fig)
