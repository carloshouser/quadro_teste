
# ⌨️ Atalhos de teclado
# Windows + Ctrl + D → Cria imediatamente uma nova área de trabalho.
# Windows + Ctrl + ← / → → Alterna entre as áreas de trabalho criadas.
# Windows + Tab → Abre a Visão de Tarefas, onde você pode gerenciar 
# e adicionar áreas de trabalho manualmente.

# Variável de ambiente para criptografia: 
# COOKIE_SECRET: xxx
# import secrets
# print(secrets.token_hex(32))

# python.exe -m pip install --upgrade pip
# pip install streamlit
# pip install streamlit-cookies-manager
# pip freeze > requirements.txt
# pip install -r requirements.txt
# Clonar no git: 
## git clone https://github.com/carloshouser/quadro_teste.git

# Como Criar um novo OAuth Client ID (forma correta)
# https://console.cloud.google.com/apis/credentials
# flamboyantdesignacoes@gmail.com

# PASSO 1 — Criar um novo OAuth Client ID (forma correta)

# No Google Cloud Console:

# Vá em
# https://console.cloud.google.com/apis/credentials

# Clique em:
# + Criar credenciais
# Escolha ID do cliente OAuth
# Aplicativo da Web   ← MUITO IMPORTANTE
# PASSO 2 — Preencha
# Nome: Streamlit Flamboyant
# Universal Windows Platform

# Tem que ser Aplicativo da Web

# PASSO 2 — Preencha

# Nome:

# Streamlit Flamboyant

# URIs de redirecionamento autorizados: https://SEU-APP.streamlit.app/oauth2callback
# Clique em criar
# Copie os valores de ClientID e ClientSecret

import streamlit as st

# ===============================
# Configuração da página
# ===============================
st.set_page_config(
    page_title="Flamboyant - Quadro de Anúncios",
    layout="wide",
)


# Controle de sessão e cookies
import sessao_controle

# Estilo global
from estilo import aplicar_estilo

# Telas
from login_usuario import render_login
from paginas.home import render_home
from paginas.lembretes import render_lembretes
from paginas.limpeza import render_limpeza
from paginas.relatorios import render_relatorio
from paginas.painel_ociosidade import render_painel_ociosidade
from paginas.vida_crista_escalas import render_escala
from paginas.painel_frequencia import render_painel_frequencia
from paginas.designacoes_estudantes import render_designacoes_estudantes
from paginas.designacoes_mecanicas import render_designacoes_mecanicas
from paginas.salao_reino_1_campo import render_salao_reino_1_campo
from paginas.entrada_oradores import render_entrada_oradores
from paginas.agenda_oradores import render_agenda_oradores
# (no futuro: dashboard, cadastro, frequência, etc.)



# ===============================
# Estilo global (UMA vez)
# ===============================
aplicar_estilo()

# ===============================
# Inicialização da sessão
# ===============================
sessao_controle.init_sessao()

# ===============================
# Login automático por cookie
# ===============================
#sessao_controle.tentar_login_por_cookie()
sessao_controle.init_sessao()

# ===============================
# Roteamento central
# ===============================
if not st.session_state["logado"]:
    # Tela de login
    render_login()

else:
    pagina = st.session_state["pagina"]

    if pagina == "home":
        render_home()

    elif pagina == 'lembretes':
        render_lembretes()
        
    elif pagina == 'limpeza':
        render_limpeza()

    elif pagina == 'salao_reino_1_campo':
        render_salao_reino_1_campo()

    elif pagina == 'relatorio':
        render_relatorio() 

    elif pagina == "ociosidade":
        render_painel_ociosidade()

    elif pagina == "vida_crista_escalas":
        render_escala()

    elif pagina == "painel_frequencia":
        render_painel_frequencia()
    
    elif pagina == "designacoes_estudantes":
        render_designacoes_estudantes()

    elif pagina == "designacoes_mecanicas":
        render_designacoes_mecanicas()

    elif pagina == "entrada_oradores":
        render_entrada_oradores()
    
    elif pagina == "agenda_oradores":
        render_agenda_oradores()

    else:
        st.error("Página não encontrada.")
