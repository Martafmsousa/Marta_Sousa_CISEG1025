# Exercício 2 – Classificação de nota

nota = int(input("Nota (0 a 100): "))

match nota:
    case n if n >= 90:
        print("Excelente")
    case n if n >= 70:
        print("Bom")
    case n if n >= 50:
        print("Suficiente")
    case _:
        print("Insuficiente")
