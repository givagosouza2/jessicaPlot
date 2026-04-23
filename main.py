import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")

st.title("Análise de movimento por participante")

# 🔹 Dicionário com dados de cada pessoa
dados = {
    "Aristacho": {
        "video": "https://youtu.be/KrsJxEfyyVM",
        "csv": "aristacho.csv"
    },
    "Carmem": {
        "video": "https://youtu.be/0VMtsdwf8ns",
        "csv": "carmem.csv"
    },
    "Isabel": {
        "video": "https://youtu.be/hODABKKUWq0",
        "csv": "isabel.csv"
    },
    "Orlando": {
        "video": "https://youtu.be/V-j6muEi6lg",
        "csv": "orlando.csv"
    },
    "Therezinha": {
        "video": "https://youtu.be/Jutzpg-CssQ",
        "csv": "therezinha.csv"
    }
}

# 🔽 Lista de seleção
nome = st.selectbox("Selecione o participante:", list(dados.keys()))

# 🔹 Recupera dados selecionados
video_url = dados[nome]["video"]
csv_path = dados[nome]["csv"]

# Layout em colunas
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader(f"Vídeo - {nome}")
    st.video(video_url)

with col2:
    st.subheader("Cinemática (eixo Z)")

    df = pd.read_csv(csv_path, usecols=[0, 9, 10, 11])
    df.columns = ["tempo", "x", "y", "z"]
    z = df["z"]
    t = df["tempo"]
    peak_z = np.max(z)
    for index,valor in enumerate(z):
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







