# Exercício Loop – Contar pares e ímpares

pares = 0
impares = 0

for i in range(10):
    num = int(input("Número " + str(i+1) + ": "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares:", pares)
print("Ímpares:", impares)
