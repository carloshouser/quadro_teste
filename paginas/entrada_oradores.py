import streamlit as st
import base64
from pathlib import Path
from acessos import quadros


def render_entrada_oradores():        

    # 🔧 ESPAÇO DE SEGURANÇA NO TOPO (antes de tudo)
    st.markdown("<div style='height:60px'></div>", unsafe_allow_html=True)

    # 🔙 Botão Voltar
    if st.button("⬅ Voltar para a página principal", key = 'entrada_oradores_voltar', width='stretch'):
        st.session_state["pagina"] = "home"
        st.rerun()

    st.markdown("---")
    st.title('🔧' + quadros["entrada_oradores"]["titulo"])

    entrada_oradores_path = (
        Path(__file__).parent.parent
        / "assets"
        / quadros["entrada_oradores"]["arquivo"]
    )
    

    with open(entrada_oradores_path, "rb") as file:
        if entrada_oradores_path.exists():
            pdf_base64 = base64.b64encode(file.read()).decode("utf-8")
            st.markdown(
                f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="100%" height="1000px"></iframe>',
                unsafe_allow_html=True,
            )
        else:
            st.error("Lista de entrada de oradores não encontrada.")