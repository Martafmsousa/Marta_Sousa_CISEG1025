# Exercício 5 – 3 valores em ordem crescente e decrescente

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))

lista = [num1, num2, num3]
lista.sort()

print("Crescente:", lista)
lista.reverse()
print("Decrescente:", lista)
