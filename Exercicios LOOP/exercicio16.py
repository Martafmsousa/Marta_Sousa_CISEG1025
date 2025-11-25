# Exercicio 16 

soma = 0
cont = 0

while cont < 30:
    n = int(input("Digite um número par entre 1 e 50: "))

    if 1 <= n <= 50 and n % 2 == 0:
        soma = soma + n
        cont = cont + 1
    else:
        print("Valor inválido.")

media = soma / 30
print("Média =", media)
