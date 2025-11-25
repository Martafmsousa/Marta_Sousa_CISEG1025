# Exercicio 10 - Elabore um programa que lê um número e escreve quantos divisores ele possui

n = int(input("Digite um número: "))
total = 0

for i in range(1, n+1):
    if n % i == 0:
        total = total + 1

print("Quantidade de divisores =", total)
