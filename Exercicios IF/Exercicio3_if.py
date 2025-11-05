# Exercício 3 – Mostrar em ordem crescente e decrescente

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

if num1 < num2:
    print("Crescente:", num1, ",", num2)
    print("Decrescente:", num2, ",", num1)
else:
    print("Crescente:", num2, ",", num1)
    print("Decrescente:", num1, ",", num2)
