# Exercicio 4 - Ordenar uma lista de palavras pela quantidade de letras minúsculas

def contar_minusculas(palavra):
    cont = 0
    for letra in palavra:
        if 'a' <= letra <= 'z':
            cont += 1
    return cont


def ordenar_por_minusculas(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - 1):

            p1 = contar_minusculas(lista[j])
            p2 = contar_minusculas(lista[j + 1])

            if p1 > p2:   
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista


# TESTE
palavras = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]
print(ordenar_por_minusculas(palavras))
