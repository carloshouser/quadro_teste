import streamlit as st
import base64
from pathlib import Path
from acessos import quadros

def render_agenda_oradores():

    # 🔧 ESPAÇO DE SEGURANÇA NO TOPO (antes de tudo)
    st.markdown("<div style='height:60px'></div>", unsafe_allow_html=True)

    # 🔙 Botão Voltar
    if st.button("⬅ Voltar para a página principal", key = 'agenda_oradores_voltar', width='stretch'):
        st.session_state["pagina"] = "home"
        st.rerun()

    st.markdown("---")
    st.title(quadros["agenda_oradores"]["titulo"])

    agenda_oradores_path = (
        Path(__file__).parent.parent
        / "assets"
        / quadros["agenda_oradores"]["arquivo"]
    )
    
    with open(agenda_oradores_path, "rb") as file:        
        if agenda_oradores_path.exists():
            pdf_base64 = base64.b64encode(file.read()).decode("utf-8")
            st.markdown(
                f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="100%" height="1000px"></iframe>',
                unsafe_allow_html=True,
            )
        else:
            st.error("Agenda de Oradores não encontrada.")