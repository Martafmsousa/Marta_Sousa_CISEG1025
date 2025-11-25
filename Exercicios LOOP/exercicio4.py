# Exercicio 4 - Crie um algoritmo que leia um número inteiro, e diga se ele é um número primo ou não

n = int(input("Digite um número: "))
divisores = 0

for i in range(1, n+1):
    if n % i == 0:
        divisores = divisores + 1

if divisores == 2:
    print("É primo")
else:
    print("Não é primo")
