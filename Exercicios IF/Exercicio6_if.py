# Exercício 6 – Desconto de compra

nome = input("Nome do cliente: ")
compra = float(input("Valor da compra: "))

if compra <= 200:
    desconto = compra * 0.10
elif compra <= 500:
    desconto = compra * 0.15
else:
    desconto = compra * 0.20

total = compra - desconto

print("Nome:", nome)
print("Compra:", compra, "€")
print("Desconto:", round(desconto, 2), "€")
print("Total a pagar:", round(total, 2), "€")
