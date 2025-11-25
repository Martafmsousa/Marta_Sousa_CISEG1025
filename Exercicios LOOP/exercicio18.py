# Exercicio 18

limite = int(input("Digite um número: "))
total = 0

for n in range(1, limite+1):
    soma = 0

    for i in range(1, n):
        if n % i == 0:
            soma = soma + i

    if soma == n:
        print(n, "é perfeito")
        total = total + 1

print("Quantidade de números perfeitos:", total)
