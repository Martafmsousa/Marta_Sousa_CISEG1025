# Exercício 3 – Tipo de pedido

pedido = {"tipo": input("Tipo (compra/venda): ").lower(), "valor": float(input("Valor (€): "))}

match pedido["tipo"]:
    case "compra":
        print(f"Compra de {pedido['valor']}€")
    case "venda":
        print(f"Venda de {pedido['valor']}€")
    case _:
        print("Pedido desconhecido")
