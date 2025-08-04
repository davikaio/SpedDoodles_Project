import random

PALAVRAS_POR_DIFICULDADE = {
    "Iniciante": [
        "bola", "gato", "flor", "carro", "lua", "árvore", "nuvem", "sol", "copo", "fogo"
    ],
    "Intermediário": [
        "castelo", "espelho", "bússola", "trono", "engrenagem", "búfalo", "poção", "búzio", "lanterna", "relógio"
    ],
    "Experiente": [
        "ocultismo", "dimensão", "cristalização", "introspecção", "metamorfose", "alquimia", "eternidade", "abismo", "vórtice", "transcendência"
    ]
}

def gerar_duas_palavras(dificuldade):
    palavras = PALAVRAS_POR_DIFICULDADE.get(dificuldade, [])
    if len(palavras) < 2:
        return ["Erro", "Poucas palavras"]
    return random.sample(palavras, 2)
