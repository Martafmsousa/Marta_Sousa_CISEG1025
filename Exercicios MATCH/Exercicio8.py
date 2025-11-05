# Exercício 8 – Operação matemática

operacao = input("Operação (soma, subtrai, multiplica, divide): ").lower()
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))

match operacao:
    case "soma":
        print("Resultado:", n1 + n2)
    case "subtrai":
        print("Resultado:", n1 - n2)
    case "multiplica":
        print("Resultado:", n1 * n2)
    case "divide":
        if n2 != 0:
            print("Resultado:", n1 / n2)
        else:
            print("Erro: divisão por zero")
    case _:
        print("Operação inválida")
