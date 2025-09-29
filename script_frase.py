import random

# Lista de frases
frases = [
    "Aprender é a melhor forma de se reinventar!",
    "Hoje é um ótimo dia para codar!",
    "TypeScript é vida! 🚀",
    "Back-end poderoso com Node.js!",
    "React Native deixa tudo mais mobile-friendly!"
]

# Escolher uma frase aleatória
nova_frase = random.choice(frases)

# Lê o README
with open("README.md", "r", encoding="utf-8") as f:
    conteudo = f.read()

# Substitui a linha da curiosidade
import re
conteudo = re.sub(r"(> Aqui vai aparecer uma frase aleatória.*)", f"> {nova_frase}", conteudo)

# Salva o README atualizado
with open("README.md", "w", encoding="utf-8") as f:
    f.write(conteudo)
