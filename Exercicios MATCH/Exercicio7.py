# Exercício 7 – Classificação de produto

categoria = input("Categoria (eletrônico/alimento): ").lower()
preco = float(input("Preço: "))

produto = {"categoria": categoria, "preco": preco}

match produto:
    case {"categoria": "eletrônico" | "eletronico", "preco": p} if p > 1000:
        print("Produto de luxo")
    case {"categoria": "eletrônico" | "eletronico", "preco": p} if p <= 1000:
        print("Produto comum")
    case {"categoria": "alimento", "preco": _}:
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")

