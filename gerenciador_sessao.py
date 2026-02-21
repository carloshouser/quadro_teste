import secrets
import time

# armazenamento em memória das sessões
sessoes_ativas = {}

# tempo de expiração (opcional)
TEMPO_EXPIRACAO = 60 * 60 * 24 * 7  # 7 dias

def criar_sessao(usuario):
    session_id = secrets.token_urlsafe(32)

    sessoes_ativas[session_id] = {
        "usuario": usuario,
        "criado_em": time.time()
    }

    return session_id


def obter_usuario(session_id):

    if session_id not in sessoes_ativas:
        return None

    sessao = sessoes_ativas[session_id]

    # verifica expiração
    if time.time() - sessao["criado_em"] > TEMPO_EXPIRACAO:
        del sessoes_ativas[session_id]
        return None

    return sessao["usuario"]


def remover_sessao(session_id):

    if session_id in sessoes_ativas:
        del sessoes_ativas[session_id]