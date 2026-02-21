import streamlit as st


# ===============================
# Inicialização do session_state
# ===============================
def init_sessao():
    """
    Garante que todas as chaves necessárias existam no session_state.
    Cada usuário terá sua própria sessão isolada automaticamente pelo Streamlit.
    """
    if "logado" not in st.session_state:
        st.session_state["logado"] = False

    if "usuario" not in st.session_state:
        st.session_state["usuario"] = None

    if "pagina" not in st.session_state:
        st.session_state["pagina"] = "login"


# ===============================
# Logout
# ===============================
def reset_sessao():
    """
    Logout completo e seguro.
    Funciona tanto para Google quanto login tradicional.
    """

    # Caso esteja logado via Google
    if st.user.is_logged_in:

        # Limpa sessão local primeiro
        st.session_state.clear()

        # Logout Google (encerra sessão e reinicia automaticamente)
        st.logout()

        return  # importante

    # Caso seja login tradicional
    st.session_state.clear()

    # Estado inicial
    st.session_state["logado"] = False
    st.session_state["usuario"] = None
    st.session_state["pagina"] = "login"

    st.rerun()


