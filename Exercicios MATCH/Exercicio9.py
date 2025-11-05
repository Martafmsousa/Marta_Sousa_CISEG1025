# Exercício 9 – Processamento de requisição

metodo = input("Método (GET/POST): ").upper()
conteudo = input("Conteúdo (pode estar vazio): ")

req = {"metodo": metodo, "conteudo": conteudo}

match req:
    case {"metodo": "GET", "conteudo": _}:
        print("Requisição GET recebida")
    case {"metodo": "POST", "conteudo": c} if c != "":
        print("Requisição POST com dados válidos")
    case {"metodo": "POST", "conteudo": ""}:
        print("Requisição POST sem dados")
    case _:
        print("Método não suportado")

