# Importações
import streamlit as st
import json
import base64
from constantes import usuarios, estilo, quadros

# Funções Auxiliares


def add_css():
    """
    Adiciona o CSS para personalizar o layout do aplicativo.
    """
    st.markdown(estilo, unsafe_allow_html=True)


def load_json(file_path):
    """
    Carrega dados de um arquivo JSON.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def render_header():
    """
    Renderiza o cabeçalho do aplicativo com uma imagem.
    """
    st.image("Salao.png", use_container_width=True)


def autenticar_usuario(usuario, senha):
    """
    Verifica se o usuário e a senha são válidos.
    """
    return usuario in usuarios and usuarios[usuario]["senha"] == senha


def reset_sessao():
    """
    Reseta a sessão do Streamlit.
    """
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# Renderizações


def render_login():
    """
    Renderiza a tela de login.
    """
    st.title("Flamboyant - Quadro de Anúncios")
    usuario = st.text_input("Usuário").strip()
    senha = st.text_input("Senha", type="password").strip()

    if st.button("Entrar"):
        if autenticar_usuario(usuario, senha):
            st.session_state.update({
                "logado": True,
                "usuario": usuario,
                "pagina": "home"
            })
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")


def render_home():
    """
    Renderiza a página principal com os quadros de anúncios.
    """
    st.title("Flamboyant - Quadro de Anúncios")
    usuario = st.session_state["usuario"]
    permissoes = usuarios[usuario]["permissoes"]
    st.write(f"Saudações, {usuario}!")

    col1, col2 = st.columns(2)

    def render_quadros(chaves, coluna):
        for chave in chaves:
            if chave in permissoes:
                quadro = quadros[chave]
                if coluna.button(quadro["titulo"], key=f"abrir_{chave}"):
                    st.session_state.update({
                        "pagina": "visualizar",
                        "quadro_atual": chave
                    })
                    st.rerun()

    render_quadros(["a", "b", "c"], col1)
    render_quadros(["d", "e", "f"], col2)

    st.divider()
    st.write('### Designações')

    st.markdown(
        '<a href="https://www.dropbox.com/sh/g7i0hvmnbcd495i/AAC_vF7im3ke8-lvRGfjYQRRa?dl=0" target="_blank" style="margin-top: 20px;">📂 Acessar Designações</a>',
        unsafe_allow_html=True
    )
    st.write(
        f'{usuario}, consulte as designações de sua congregação de forma rápida e simples.')

    st.divider()
    st.write('### Territórios')

    st.markdown(
        '<a href="https://www.dropbox.com/scl/fo/cvzev6g0ktlwqqd9sbkcz/AKxNxYXYDq2OgFYSj8szZdw?rlkey=oy5r89ijmjrzrlguf5l0fy8qx&dl=0" target="_blank" style="margin-top: 20px;">📂 Territórios</a>',
        unsafe_allow_html=True
    )
    st.write(
        f'{usuario}, acesse os territórios de sua congregação de forma bem objetiva.')

    st.divider()

    if st.button("Sair"):
        reset_sessao()


def render_visualizar():
    """
    Renderiza a página de visualização de um quadro.
    """
    chave = st.session_state["quadro_atual"]
    quadro = quadros[chave]

    st.title(quadro["titulo"])

    with open(quadro["arquivo"], "rb") as file:
        if quadro["arquivo"].endswith(".png"):
            st.image(
                file.read(), caption=quadro["titulo"], use_container_width=True)
        elif quadro["arquivo"].endswith(".pdf"):
            pdf_base64 = base64.b64encode(file.read()).decode('utf-8')
            st.markdown(
                f'<iframe src="data:application/pdf;base64,{
                    pdf_base64}" width="100%" height="1000px"></iframe>',
                unsafe_allow_html=True
            )

    if st.button("Voltar"):
        st.session_state["pagina"] = "home"
        st.rerun()


def render_eventos(events):
    """
    Renderiza a aba de eventos.
    """
    st.subheader("Próximos Eventos")
    for event in events:
        st.markdown(f"""
        ### 📅 {event['date']}
        #### **{event['event']}**
        """)
        st.divider()

    if st.button("Fechar"):
        reset_sessao()


# Configuração Principal
add_css()
render_header()
events = load_json('events.json')

if "logado" not in st.session_state:
    render_login()
else:
    tab1, tab2 = st.tabs(["Quadro", "Eventos"])

    with tab1:
        if st.session_state.get("pagina") == "home":
            render_home()
        elif st.session_state.get("pagina") == "visualizar":
            render_visualizar()

    with tab2:
        if not st.session_state.get("logado"):
            st.error("Por favor, faça login para acessar esta aba.")
        else:
            render_eventos(events)
