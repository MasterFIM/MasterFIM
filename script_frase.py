import random

# Lista de frases
frases = [
    "Sempre buscando melhorar minhas habilidades! ",
    "Cada projeto é uma oportunidade de aprendizado ",
    "Front-end ou back-end, o importante é criar soluções! ",
    "Codar é transformar ideias em realidade ",
    "Desenvolvimento web é minha paixão ",
    "Um commit por vez, construindo o futuro "
]

# Escolhe uma frase aleatória
frase = random.choice(frases)

# Lê o README atual
with open("README.md", "r", encoding="utf-8") as f:
    conteudo = f.readlines()

# Substitui a linha da curiosidade
novo_conteudo = []
for linha in conteudo:
    if linha.strip().startswith("> Aqui vai aparecer"):
        novo_conteudo.append(f"> {frase}\n")
    else:
        novo_conteudo.append(linha)

# Salva o README atualizado
with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(novo_conteudo)
