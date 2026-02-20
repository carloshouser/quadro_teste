#  pip install Authlib

import streamlit as st
from acessos import usuarios


# ===============================
# Autenticação tradicional
# ===============================
def autenticar_usuario(usuario: str, senha: str) -> bool:

    return (
        usuario in usuarios
        and usuarios[usuario]["senha"] == senha
    )


# ===============================
# Encontrar usuário pelo email Google
# ===============================
def encontrar_usuario_por_email(email):

    for login, dados in usuarios.items():

        if dados.get("email") == email:
            return login

    return None


# ===============================
# Render da tela de login
# ===============================
def render_login():

    st.title("Flamboyant - Quadro de Anúncios")

    # -------------------------------
    # SE JÁ ESTÁ LOGADO COM GOOGLE
    # -------------------------------
    try:

        if hasattr(st, "user") and st.user.is_logged_in:

            email = st.user.email

            usuario = encontrar_usuario_por_email(email)

            if usuario:

                st.session_state["logado"] = True
                st.session_state["usuario"] = usuario
                st.session_state["pagina"] = "home"

                st.rerun()

            else:

                st.error(
                    "Este email não tem acesso ao sistema. Informe seu email ao irmão das designações")

                if st.button(
                    "Voltar para tela de login",
                    use_container_width=True,
                    key="login_usuario_voltar",
                ):
                    st.logout()

                st.stop()

    except AttributeError:
        # Streamlit Cloud ainda não inicializou o sistema de autenticação
        pass

    # -------------------------------
    # BOTÃO LOGIN GOOGLE
    # -------------------------------
    tab_login_google, tab_login = st.tabs(["Login Google", "Login Tradicional"])

    with tab_login_google:
        st.button(
            "Entrar com Google",
            on_click=st.login,
            use_container_width=True,
            key="login_usuario_google",
        )

    with tab_login:    

        # -------------------------------
        # LOGIN TRADICIONAL
        # -------------------------------
        st.subheader("Ou entre com usuário e senha")

        usuario = st.text_input("Usuário", key="login_usuario_input")
        senha = st.text_input("Senha", type="password", key="login_senha_input")

        if st.button("Entrar", use_container_width=True, key="login_usuario_entrar"):

            if autenticar_usuario(usuario, senha):

                st.session_state["logado"] = True
                st.session_state["usuario"] = usuario
                st.session_state["pagina"] = "home"

                st.rerun()

            else:

                st.error("Usuário ou senha incorretos.")

        # ⛔ MUITO IMPORTANTE
        st.stop()
