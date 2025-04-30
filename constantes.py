# Estilização.
estilo = """
        <style>
        /* Corpo do aplicativo */
        body {
            background-color: #F5F7FA;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Títulos */
        h1 {
            color: #2C3E50;
            font-size: 32px;
            text-align: center;
            margin-bottom: 20px;
        }
        h2 {
            color: #34495E;
            font-size: 24px;
            margin-bottom: 10px;
        }

        /* Cartões */
        .card {
            background-color: #FFFFFF;
            border: 1px solid #E0E0E0;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        /* Botões */
        .stButton>button {
            background-color: #3498DB;
            color: white;
            border-radius: 8px;
            border: none;
            font-size: 16px;
            font-weight: bold;
            padding: 12px;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #2980B9;
            transform: scale(1.02);
        }

        /* Links */
        a {
            color: #1ABC9C;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            color: #16A085;
        }

        /* PDFs */
        iframe {
            border: 2px solid #E0E0E0;
            border-radius: 8px;
            margin-top: 20px;
        }
        </style>
    """

# Dicionário com os quadros de anúncios
quadros = {
    "a": {"titulo": "Reuniões para o Serviço de Campo", "arquivo": "servico_campo.png"},
    "b": {"titulo": "Designações de Discurso Público", "arquivo": "discurso_publico.png"},
    "c": {"titulo": "Anúncios e Lembretes", "arquivo": "anuncios.png"},
    "d": {"titulo": "Designações Reuniões Flamboyant", "arquivo": "reunioes_flamboyant.png"},
    "e": {"titulo": "Programação da Reunião do Meio de Semana", "arquivo": "programacao_meio_semana.png"},
    "f": {"titulo": "Designações para Limpeza do Salão do Reino", "arquivo": "limpeza_salao.png"},
}

# Dados fictícios de usuários e permissões
usuarios = {
    "Jerome": {"senha": "@salmo8318", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Carlos": {"senha": "123", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Aron": {"senha": "@genesis10", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Silvia": {"senha": "@exodo10", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Armando": {"senha": "@edom1", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Carlos Montesino": {"senha": "@gibeon2", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "David Affonso": {"senha": "@zion12", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Ederson": {"senha": "@hebron11", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Edson": {"senha": "@siloe21", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Felipe Carneiro": {"senha": "@tarsis5", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Francisco Lezcano": {"senha": "@mambre54", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Gilmar": {"senha": "@betel7", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Giovani": {"senha": "@jerico20", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "José Francisco": {"senha": "@galileia5", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Marcos Ribeiro": {"senha": "@tabor12", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Marcos Woicjki": {"senha": "@egito1", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Paulo Carvalho": {"senha": "@nazare22", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Paulo Franco": {"senha": "@edom33", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Raphael Madeira": {"senha": "@hermom44", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Renato": {"senha": "8318", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Sergio Santos": {"senha": "@sidom21", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Anderson Valle": {"senha": "@moabe566", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Aparecida Spina": {"senha": "@samaria56", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Arileide": {"senha": "@sarepta56", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Arlene": {"senha": "@tiberias54", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Bibiane": {"senha": "@galatia32", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Carina": {"senha": "@bereia2", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Clarice": {"senha": "@jerusalem13", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Studzuski": {"senha": "@samuel23", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Cleusa": {"senha": "@babel58", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Daiane": {"senha": "@corinto13", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Daiane Graciela": {"senha": "@juda33", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Daniele": {"senha": "@magdala6", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Daniela Rodrigues": {"senha": "@samaria411", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Davides": {"senha": "@nazir23", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Derli": {"senha": "@mara10", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Doris": {"senha": "@arao123", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Dulce": {"senha": "@rute321", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Edilene": {"senha": "@sarai123", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Eduarda": {"senha": "@dbora411", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Emilly": {"senha": "@ester235", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Erica": {"senha": "@ligia4", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Esli": {"senha": "@gade22", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Ester": {"senha": "@hama41", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Eva": {"senha": "@adao245", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Felipe Gobato": {"senha": "@jair33", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Fernanda Machado": {"senha": "@joabe12", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Fernanda Madeira": {"senha": "@moises57", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Gabriela Ribeiro": {"senha": "@levi55", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Gicelle": {"senha": "@sela54", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Gisele": {"senha": "@noga55", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Heitor": {"senha": "@urias50", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Henrique": {"senha": "@tequel50", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Herminio": {"senha": "@aram44", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Isabela": {"senha": "@tamar22", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Jahina": {"senha": "@maom44", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "João Batista": {"senha": "@nazaro55", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Josnei": {"senha": "@rebeca57", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Jucimere": {"senha": "@sodoma57", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Ketlin": {"senha": "@egito877", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Lara": {"senha": "@judite55", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Laura": {"senha": "@ismael44", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Lucas Daniel": {"senha": "@adriel66", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Luciana": {"senha": "@mical112", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Luis Claudio": {"senha": "@salao77", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Luiz Eleutério": {"senha": "@apolo7", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Luiz Nogueira": {"senha": "@asa4", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Marcia": {"senha": "@goel21", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Maria": {"senha": "@fe23", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Maria Dione": {"senha": "@orfa98", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Marli": {"senha": "@rute44", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Millena": {"senha": "@metusala12", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Miriam": {"senha": "@eva22", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Nadir": {"senha": "@tamar14", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Natalia": {"senha": "@cain78", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Nicolas": {"senha": "@jope33", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Noemia": {"senha": "@noe54", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Rafaela": {"senha": "@tiro99", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Regina": {"senha": "@hadasa76", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Rose Coutinho": {"senha": "@daniel77", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Roseli": {"senha": "@jonas25", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Roseni": {"senha": "@debora77", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Santina": {"senha": "@rabi55", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Silmara": {"senha": "@joel43", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Silvana": {"senha": "@simao34", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Simone": {"senha": "@mara76", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Thalita": {"senha": "@palma12", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Valdir": {"senha": "@bara12", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Vanda": {"senha": "@sal91", "permissoes": ["a", "b", "c", "d", "e", "f"]},
    "Yamilet": {"senha": "@eloim57", "permissoes": ["a", "b", "c", "d", "e", "f"]},
}
