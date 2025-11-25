# Exercicio 14 - Altere o programa anterior para que mostre todas as tabuadas de 1 a 100. (ciclos for)

for n in range(1, 101):
    print("\nTabuada de", n)
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
