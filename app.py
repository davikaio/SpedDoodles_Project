import streamlit as st
from core import gerar_duas_palavras

st.set_page_config(page_title="SpedDoodles", page_icon="🎨")
st.title("🎨 SpedDoodles, Gerador de Ideias para Desenhos")

dificuldade = st.selectbox("Escolha a dificuldade:", ["Iniciante", "Intermediário", "Experiente"])

if st.button("Gerar Ideia"):
    palavras = gerar_duas_palavras(dificuldade)
    st.subheader("Sua combinação criativa:")
    st.markdown(f"- **{palavras[0]}**")
    st.markdown(f"- **{palavras[1]}**")
