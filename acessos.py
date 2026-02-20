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

    "Anderson Valle": {
        "email": "andersonvalle93@gmail.com",
        "senha": "@moabe566",
        "permissoes": acesso_nivel_3,
        "sexo": "M",
        "nome": "Anderson do Vale",
    },

    "Aparecida Spina": {
        "senha": "@samaria56",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Aparecida Spina",
    },

    "Arenusa Odor": {
        "senha": "@eva",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Arenusa Odor",
    },

    "Arileide": {
        "senha": "@sarepta56",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Arileide Cristina Alves",
    },

    "Arlene": {
        "senha": "@tiberias54",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Arlene Trinco",
    },

    "Armando": {
        "senha": "@edom1",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "Armando",
    },

    "Aron": {
        "senha": "@genesis10",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "Aron Stachecka",
    },

    "Bernardo": {
            "senha": "@Isaias10",
            "nome": "Bernardo",            
            "sexo": "M",
            "permissoes": acesso_nivel_3
        },

    "Bibiane": {
        "senha": "@galatia32",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Bibiane Vieira",
    },

    "Camila": {
        "senha": "@Genesis50",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Camila Bernardo",
    },

    "Carlos": {
        "email": "carloshouser@gmail.com",
        "senha": "ddd",
        "nome": "Carlos",        
        "sexo": "M",
        "permissoes" : acesso_nivel_1,
    },

    "Carina": {
        "senha": "@bereia2",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Carina Wojcik",
    },

    "Carlos Montesino": {
        "senha": "@gibeon2",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "Carlos Montesino",
    },

    "Clarice": {
        "senha": "@jerusalem13",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Clarice Colaço",
    },

    "Cleusa": {
        "senha": "@babel58",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Cleusa",
    },

    "Daiane": {
        "senha": "@corinto13",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Daiane Almeida",
    },

    "Daiane Graciela": {
        "senha": "@juda33",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Daiane Graciela",
    },

    "Daniele": {
        "senha": "@magdala6",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Daniele Colaço",
    },

    "Daniela Rodrigues": {
        "senha": "@samaria411",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Daniela Rodrigues",
    },

    "David Affonso": {
        "email": "david.affonso1218@gmail.com",
        "senha": "@zion12",
        "permissoes": acesso_nivel_2,
        "sexo": "M",
        "nome": "David Affonso",
    },

    "Davides": {
        "senha": "@nazir23",
        "permissoes": acesso_nivel_3,
        "sexo": "M",
        "nome": "Davides Affonso",
    },

    "Debora": {
        "senha": "@debora10",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Débora de Julio",
    },

    "Denise": {
        "senha": "@exodo10",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Denise Mann",
    },

    "Derli": {
        "senha": "@mara10",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Derli Gonçalves",
    },

    "Doris": {
        "senha": "@arao123",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Doris Foltran",
    },

    "Dulce": {
        "senha": "@rute321",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Dulce Nogueira",
    },

    "Ederson": {
        "senha": "@hebron11",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "Ederson Carneiro",
    },

    "Edilene": {
        "senha": "@sarai123",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Edilene Silva",
    },

    "Edson": {
        "senha": "@siloe21",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "Edson Padilha",
    },

    "Eduarda": {
        "senha": "@dbora411",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Eduarda Monteiro",
    },    

    "Elber": {
        "senha": "@juizes10",        
        "nome": "Elber Soares",
        "sexo": "M",
        'permissoes' : acesso_nivel_3,        
    },    

    "Emilly": {
        "senha": "@ester235",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Emilly Carneiro",
    },

    "Erica": {
        "senha": "@ligia4",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Érica Rodrigues",
    },

    "Esli": {
        "senha": "@gade22",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Esli Santos",
    },

    "Ester": {
        "senha": "@hama41",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Ester Machado",
    },

    "Eva": {
        "senha": "@adao245",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Eva Helena",
    },

    "Fernanda Machado": {
        "senha": "@joabe12",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Fernanda Machado",
    },

    "Fernanda Madeira": {
        "senha": "@moises57",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Fernanda Madeira",
    },

    "Felipe Carneiro": {
        "senha": "@tarsis5",
        "permissoes": acesso_nivel_2,
        "sexo": "M",
        "nome": "Felipe Carneiro",
    },

    "Felipe Gobato": {
        "senha": "@jair33",
        "permissoes": acesso_nivel_3,
        "sexo": "M",
        "nome": "Felipe Gobato",
    },

    "Francisco Lezcano": {
        "senha": "@mambre54",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "Francinco Lezcano",
    },

    "Gabriela Ribeiro": {
        "senha": "@levi55",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Gabriela Ribeiro",
    },

    "Gicelle": {
        "senha": "@sela54",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Gicelle Carneiro",
    },

    "Gilmar": {
        "senha": "@betel7",
        "permissoes": acesso_nivel_2,
        "sexo": "M",
        "nome": "Gilmar de Lucas",
    },

    "Giovani": {
        "email": "giovaninv80@gmail.com",
        "senha": "@jerico20",
        "permissoes": acesso_nivel_2,
        "sexo": "M",
        "nome": "Giovani Vieira",
    },

    "Gisele": {
        "senha": "@noga55",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Gisele Vieira",
    },

    "Gessica": {
        "senha": "@sarai",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Gessica Souza",
    },

    "Giuliano Odor": {
        "senha": "@eden",
        "permissoes": acesso_nivel_3,
        "sexo": "M",
        "nome": "Giuliano Odor",
    },

    "Heitor": {
        "senha": "@54540304230@44#@!#$054",
        "permissoes": acesso_nivel_3,
        "sexo": "M",
        "nome": "Heitor Wojcik",
    },

    "Henrique": {
        "senha": "@tequel50",
        "permissoes": acesso_nivel_3,
        "sexo": "M",
        "nome": "Henrique",
    },

    "Herminio": {
        "senha": "@aram44",
        "permissoes": acesso_nivel_3,
        "sexo": "M",
        "nome": "Herminio Maciel",
    },

    "Isabela": {
        "senha": "@tamar22",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Isabela Vieira",
    },

    "Jahina": {
        "senha": "@maom44",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Jahina Gonçalves",
    },

    "Jerome": {
        "senha": "@salmo8318",              
        "nome": "Jerome Sampaio",
        "sexo": "M",
        "permissoes" : acesso_nivel_1,
    },

    "João Batista": {
        "senha": "@nazaro55",
        "permissoes": acesso_nivel_3,
        "sexo": "M",
        "nome": "João Batista",
    },

    "José Francisco": {
        "email": "carmo.jose@gmail.com",
        "senha": "@galileia5",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "José Francisco",
    },

    "Josnei": {
        "senha": "@rebeca57",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "Josnei Machado",
    },

    "Jucimere": {
        "senha": "@sodoma57",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Jucimere Machado",
    },    

    "Ketlin": {
        "senha": "@egito877",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Ketlin Carneiro",
    },

     "Lara": {
        "senha": "@judite55",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Lara Sophia",
    },

    "Laura": {
        "senha": "@ismael44",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Laura Franco",
    },

    "Lidyane": {
        "senha": "@ester10",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Lidyane Soares",
    },

    "Luana": {
        "senha": "@Hebron44",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Luana Ruth Mann",
    },

    "Lucas Daniel": {
        "senha": "@adriel66",
        "permissoes": acesso_nivel_3,
        "sexo": "M",
        "nome": "Lucas Daniel",
    },

    "Luciana": {
        "senha": "@mical112",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Luciana Perpétuo",
    },

    "Luis Claudio": {
        "senha": "@salao77",
        "permissoes": acesso_nivel_2,
        "sexo": "M",
        "nome": "Luis Claudio",
    },

    "Luiz Eleutério": {
        "senha": "@apolo7",
        "permissoes": acesso_nivel_3,
        "sexo": "M",
        "nome": "Luiz Eleutério",
    },

    "Luiz Nogueira": {
        "senha": "@asa4",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "Luiz Nogueira",
    },

    "Marcos Ribeiro": {
        "senha": "@tabor12",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "Marcos Ribeiro",
    },

    "Marcos Woicjki": {
        "senha": "@egito1",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "Marcos Woicjki",
    },

    "Maria": {
        "senha": "@fe23",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Maria da Luz",
    },

    "Maria Dione": {
        "senha": "@orfa98",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Maria Dione",
    },

    "Maria Lucia": {
        "senha": "@maria10",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Gisele Vieira",
    },

    "Miguel Bernardo": {
        "email": 'stormparts22@gmail.com',
        "senha": "@juizes7",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "Miguel Mann Bernardo",
    },

    "Millena": {
        "senha": "@metusala12",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Millena Carneiro",
    },

    "Miriam": {
        "email": "mirianlaraaffonso@gmail.com",
        "senha": "@eva22",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Miriam Affonso",
    },

    "Nadir": {
        "senha": "@tamar14",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Nadir Padilha",
    },
    
    "Natalia": {
        "senha": "@cain78",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Natalia Alves",
    },

    "Nicolas": {
        "senha": "@jope33",
        "permissoes": acesso_nivel_3,
        "sexo": "M",
        "nome": "Nícolas",
    },

    "Noemia": {
        "senha": "@noe54",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Noêmia Melo",
    },

    "Paulo Carvalho": {
        "senha": "@nazare22",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "Paulo Carvalho",
    },

    "Paulo Franco": {
        "senha": "@edom33",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "Paulo Franco",
    },

    "Rafaela": {
        "senha": "@tiro99",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Rafaela Silva",
    },

    "Raphael Madeira": {
        "senha": "@hermom44",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "Raphael Madeira",
    },

    "Regina": {
        "senha": "@hadasa76",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Regina Fonseca",
    },

    "Renato": {
        "email": "renatohorning1434@gmail.com",
        "senha": "8318",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "Renato Horning",
    },

    "Rosa": {
        "senha": "@rute2",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Rosa",
    },

    "Rose Coutinho": {
        "email": "rc568008@gmail.com",
        "senha": "@daniel77",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Rose de Jesus Coutinho",
    },

    "Roseli": {
        "senha": "@jonas25",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Roseli de Julio",
    },

    "Roseni": {
        "senha": "@debora77",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Roseni de Almeida",
    },

    "Santina": {
        "senha": "@rabi55",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Santina Gobato",
    },

    "Sergio Santos": {
        "email": "sergio5521@gmail.com",
        "senha": "@sidom21",
        "permissoes": acesso_nivel_1,
        "sexo": "M",
        "nome": "Sergio Santos",
    },

     "Silmara": {
        "email": "silmaraspinapereira@gmail.com",
        "senha": "sil1734",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Silmara Spina",
    },

    "Silvana": {
        "senha": "@simao34",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Silvana Franco",
    },

    "Silvia": {
        "senha": "@exodo10",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Sylwia Stachecka",
    },

    "Simone": {
        "senha": "@mara76",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Simone Machado",
    },

    "Studzuski": {
        "senha": "@samuel23",
        "permissoes": acesso_nivel_3,
        "sexo": "M",
        "nome": "Claudio Studzuski",
    },

    "Thalita": {
        "senha": "@palma12",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Thalita Castro",
    },

    "Valdir": {
        "senha": "@bara12",
        "permissoes": acesso_nivel_3,
        "sexo": "M",
        "nome": "Valdir Tadra",
    },

    "Vanda": {
        "senha": "@sal91",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Vanda Alves",
    },

    "William": {
        "senha": "@enoque12",
        "permissoes" : acesso_nivel_3,
        "sexo": "M",
        "nome": "William Peres",
    },

    "Yamilet": {
        "senha": "@eloim57",
        "permissoes": acesso_nivel_4,
        "sexo": "F",
        "nome": "Yamilet Prieto Zamora",
    },
    
    
}

def nome_fantasia(dic_usuario, nome):
    if dic_usuario["sexo"] == "M":
        return f"irmão {nome}"
    else:
        return f"irmã {nome}"
    
def usuario_tem_acesso(usuario, acesso):
    return acesso in usuarios.get(usuario, {}).get("permissoes", [])
     
    
