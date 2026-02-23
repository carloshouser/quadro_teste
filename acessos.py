import streamlit as st

# Nível de acesso (Anciãos)
acesso_nivel_1 = ("lembretes", 
                  "limpeza", 
                  "relatorio", 
                  "ociosidade", 
                  "vida_crista_escalas",
                  "painel_frequencia",
                  "designacoes_estudantes", 
                  "designacoes_mecanicas",
                  "salao_reino_1_campo",
                  "entrada_oradores",
                  "agenda_oradores"
)

# Nível de acesso (Servos Ministeriais)
acesso_nivel_2 = ("lembretes", 
                  "limpeza", 
                  "relatorio", 
                  "ociosidade", 
                  "vida_crista_escalas",
                  "painel_frequencia",
                  "designacoes_estudantes", 
                  "designacoes_mecanicas",
                  "salao_reino_1_campo",
                  "entrada_oradores",
                  "agenda_oradores"
)

# Nível de acesso (Varões batizados)
acesso_nivel_3 = ("lembretes", 
                  "limpeza", 
                  "relatorio", 
                  "ociosidade", 
                  "vida_crista_escalas",
                  "painel_frequencia",
                  "designacoes_estudantes", 
                  "designacoes_mecanicas"
)

# Nível de acesso (Irmãs)
acesso_nivel_4 = ("lembretes", 
                  "limpeza", 
                  "relatorio",                                                       
                  "designacoes_estudantes"                  
)

# Dicionário com os quadros de anúncios
quadros = {
    "lembretes": {
        "titulo": "Anúncios e Lembretes",
        "arquivo": r"htmls/lembrete.html"
    },

    "limpeza": {
        "titulo": "Limpeza do Salão do Reino",
        "arquivo": r"pdfs/limpeza.pdf"        
    },

    "relatorio": {
        "titulo": "Relatório (Basta preencher, printar e enviar)",
        "arquivo": r"htmls/relatorio.html"
    },

    "ociosidade": {
        "titulo": "Painel de Ociosidade",
        "arquivo": ""
    },

    "vida_crista_escalas": {
        "titulo": "Vida Cristã - Escalas",
        "arquivo": ""
    },

    "designacoes_mecanicas":{
        "titulo": "Designações Mecânicas",
        "arquivo": r"pdfs/designacoes_mecanicas.pdf"
    },

    "salao_reino_1_campo":{
        "titulo": "Salão do Reino 1 - Saídas de Campo",
        "arquivo": r"pdfs/salao_reino_1_campo.pdf"
    },

    "entrada_oradores":{
        "titulo": "Entrada de Oradores",
        "arquivo": r"pdfs/entrada_oradores.pdf"
    },

    "agenda_oradores":{
        "titulo": "Agenda de Oradores",
        "arquivo": r"pdfs/agenda_oradores.pdf"
    }
    
}

usuarios = {   

    "Carlos": {
        "email": "carloshouser@gmail.com",
        "senha": "ddd",
        "nome": "Carlos",        
        "sexo": "M",
        "permissoes" : acesso_nivel_1,
    },

    "Silmara": {
        "email": "silmaraspinapereira@gmail.com",
        "senha": "sil1734",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Silmara Spina",
    }
}

def nome_fantasia(dic_usuario, nome):
    if dic_usuario["sexo"] == "M":
        return f"irmão {nome}"
    else:
        return f"irmã {nome}"
    
def usuario_tem_acesso(usuario, acesso):
    return acesso in usuarios.get(usuario, {}).get("permissoes", [])
     
    
