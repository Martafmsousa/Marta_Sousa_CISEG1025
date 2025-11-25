# Exercicio 1- Ordenar uma lista de palavras por ordem alfabética (A → Z)
def ordenar_az(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - 1):
            
            p1 = lista[j]
            p2 = lista[j + 1]

            k = 0
            trocou = False

            while k < len(p1) and k < len(p2):
                if ord(p1[k]) > ord(p2[k]):   
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
                    break

                elif ord(p1[k]) < ord(p2[k]): 
                    trocou = True
                    break

                else:
                    k += 1   

            
            if not trocou and len(p1) > len(p2):
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista


# TESTE
palavras = ["banana", "uva", "abacaxi", "laranja"]
print(ordenar_az(palavras))

