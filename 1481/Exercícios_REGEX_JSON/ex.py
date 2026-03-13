import json
import re

# Exercicio 1 
with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

print("Dados lidos:")
print(dados)


# Regex simples
regex_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
regex_nif = r"^[123568]\d{8}$"

registos_validos = []

# Exercicio 2,3,4,5
for pessoa in dados:

    email = pessoa["email"]
    nif = pessoa["nif"]
    telemovel = pessoa["telemovel"]
    site = pessoa["site"]

    # Exercicio 2 
    email_valido = re.match(regex_email, email)

    # Exercicio 4 
    nif_valido = re.match(regex_nif, nif)

    # Exercicio 5 
    numeros = re.sub(r"\D", "", telemovel)
    telemovel_valido = len(numeros) == 9

    # Exercicio 3 
    dominio = site.replace("https://", "").replace("http://", "")
    dominio = dominio.replace("www.", "")

    print("Dominio:", dominio)

    # guardar registos validos
    if email_valido and nif_valido and telemovel_valido:
        registos_validos.append(pessoa)


# Exercicio 5 
with open("validos.json", "w", encoding="utf-8") as f:
    json.dump(registos_validos, f, indent=4, ensure_ascii=False)


# Exercicio 6 
with open("contactos.txt", "w", encoding="utf-8") as f:
    for pessoa in registos_validos:
        f.write(pessoa["nome"] + " - " + pessoa["email"] + "\n")