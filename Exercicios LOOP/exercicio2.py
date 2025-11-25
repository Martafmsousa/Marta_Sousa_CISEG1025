# Exercicio 2 - Ler 10 números, e determinar se o número par e número impar

for i in range(10):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        print("É par")
    else:
        print("É ímpar")
