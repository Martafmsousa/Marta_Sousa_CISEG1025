# Exercicio 12

n = int(input("Digite um número: "))
operacoes = 0

for i in range(1, n):
    print(n, "+", i, "=", n + i)
    operacoes = operacoes + 1

    print(n, "-", i, "=", n - i)
    operacoes = operacoes + 1

    print(n, "*", i, "=", n * i)
    operacoes = operacoes + 1

    print(n, "/", i, "=", n / i)
    operacoes = operacoes + 1
    print()

print("Total de operações realizadas:", operacoes)
