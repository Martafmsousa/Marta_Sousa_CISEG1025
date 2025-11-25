# Exercicio 15

import time

for i in range(256):
    print(i, "=", chr(i))

    if i % 20 == 0 and i != 0:
        input("Pressione ENTER para continuar...")
