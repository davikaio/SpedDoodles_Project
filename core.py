import random

PALAVRAS_POR_DIFICULDADE = {
    "Iniciante 😇": [
        "bola", "gato", "flor", "carro", "lua", "árvore", "nuvem", "sol", "copo", "fogo","chapéu", "estrela", "porta", "chuva", "pássaro", "cachorro", "barco", "mochila", "copo térmico", "óculos"
    ],
    "Intermediário 😠": [
        "castelo", "espelho", "bússola", "trono", "engrenagem", "búfalo", "poção", "búzio", "lanterna", "relógio", "espantalho", "navio", "dinossauro", "túnel", "ponte", "relâmpago", "máscara", "foguete", "armadura", "templário"
    ],
    "Experiente 😈": [
        "ocultismo", "dimensão", "cristalização", "introspecção", "metamorfose", "alquimia", "eternidade", "abismo", "vórtice", "transcendência", "ressurreição", "paradoxo", "espiral do tempo", "memória ancestral", "despertar", "simbiose", "convergência", "dualidade", "fragmento cósmico", "alquimia espiritual"

    ]
}

def gerar_duas_palavras(dificuldade):
    palavras = PALAVRAS_POR_DIFICULDADE.get(dificuldade, [])
    if len(palavras) < 2:
        return ["Erro", "Poucas palavras"]
    return random.sample(palavras, 2)