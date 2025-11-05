# Exercício 4 – Verificar se o cheque pode ser descontado

saldo = float(input("Saldo: "))
cheque = float(input("Valor do cheque: "))

if cheque <= saldo:
    saldo = saldo - cheque
    print("Cheque descontado. Saldo:", saldo)
else:
    print("Saldo insuficiente. O cheque não pode ser descontado.")
