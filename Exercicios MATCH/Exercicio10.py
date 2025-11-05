# Exercício 10 – Pedra, Papel ou Tesoura

jog1 = input("Jogador 1: ").lower()
jog2 = input("Jogador 2: ").lower()

match (jog1, jog2):
    case (a, b) if a == b:
        print("Empate")
    case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
        print("Jogador 2 venceu")
    case _:
        print("Jogada inválida")
