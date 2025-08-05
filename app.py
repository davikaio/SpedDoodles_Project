import streamlit as st
from core import gerar_duas_palavras
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="SpedDoodles", page_icon="🎨")
st.title("🎨 SpedDoodles, Gerador de Ideias para Desenhos")

dificuldade = st.selectbox("Escolha a dificuldade:", ["Iniciante 😇", "Intermediário 😠", "Experiente 😈"])

if 'palavras' not in st.session_state:
        st.session_state.palavras = None


if st.button("Gerar Ideia"):
    st.session_state.palavras = gerar_duas_palavras(dificuldade)
    palavras = gerar_duas_palavras(dificuldade)
    st.subheader("Sua combinação criativa:")
    st.markdown(f"- **{palavras[0]}**")
    st.markdown(f"- **{palavras[1]}**")
    

    st.subheader("Desenhe aqui:")
    st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)", 
        stroke_width=2,
        stroke_color="#000000",
        background_color="#FFFFFF",
        height=600,
        width=800,
        drawing_mode="freedraw",
        key="canvas",
        update_streamlit=True,
        display_toolbar=True,
        initial_drawing=None,
            )