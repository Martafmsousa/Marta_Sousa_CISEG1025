# Exericio 3 - Ordenar os caracteres de uma palavra por ordem alfabética

def ordenar_caracteres(palavra):
    lista = list(palavra)  
    n = len(lista)

    
    for i in range(n):
        for j in range(0, n - 1):
            if ord(lista[j]) > ord(lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return "".join(lista)


# TESTE
print(ordenar_caracteres("algoritmo"))  
