# Exercicio 9 - Escreva um programa que solicite um número ao utilizador até que o valor deste esteja entre os valores 1 e 100. (Usar o ciclo do ... while)

while True:
    n = int(input("Digite um número entre 1 e 100: "))

    if 1 <= n <= 100:
        print("Número válido")
        break
    else:
        print("Valor inválido, tente novamente.")
