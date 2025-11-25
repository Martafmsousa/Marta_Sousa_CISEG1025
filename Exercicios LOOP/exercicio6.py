# Exercicio 6 - Crie um algoritmo que mostre os 10 primeiros números primos

qtd = 0
num = 2

while qtd < 10:
    divisores = 0

    for i in range(1, num+1):
        if num % i == 0:
            divisores = divisores + 1

    if divisores == 2:
        print(num)
        qtd = qtd + 1

    num = num + 1
