# Exercício 1 - Dicionário simples

alunos = {
    'Maria': {'idade': 20, 'curso': 'Engenharia'},
    'João': {'idade': 22, 'curso': 'Gestão'},
    'Ana': {'idade': 19, 'curso': 'Informática'}
}

print("Ex1 - Alunos:")
for nome, info in alunos.items():
    print(f"nome: {nome}\nidade: {info['idade']}\ncurso: {info['curso']}\n")


# Exercício 2 - Aceder a valor

carro = {'marca': 'Toyota', 'modelo': 'Corolla', 'ano': 2020}
print("Ex2 - Modelo do carro:", carro['modelo'], "\n")


# Exercício 3 - Produto

produto = {'nome': "Telemóvel", 'preço': 1500, 'stock': 30}
del produto['stock']
print("Ex3 - Produto final:", produto, "\n")


# Exercício 4 - Verificar chave

utilizador = {'nome': 'Carlos', 'idade': 28}
if 'email' in utilizador:
    print("Email encontrado:", utilizador['email'])
else:
    print("Ex4 - Email não encontrado.\n")


# Exercício 5 - Contar letras

palavra = input("Ex5 - Introduz uma palavra: ")
contador = {}
for letra in palavra:
    contador[letra] = contador.get(letra, 0) + 1
print("Contagem de letras:", contador, "\n")


# Exercício 6 - Somar valores

vendas = {'Janeiro': 1000, 'Fevereiro': 1500, 'Março': 1200}
total = sum(vendas.values())
print("Ex6 - Total de vendas:", total, "\n")


# Exercício 7 - Inverter chaves/valores

d = {'a': 1, 'b': 2, 'c': 3}
invertido = {v: k for k, v in d.items()}
print("Ex7 - Dicionário invertido:", invertido, "\n")


# Exercício 8 - Juntar dicionários

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d_junto = {**d1, **d2}
print("Ex8 - Dicionário unido:", d_junto, "\n")


# Exercício 9 - Média notas

notas = {'João':[7,8,9], 'Maria':[10,9,8], 'Ana':[6,7,8]}
print("Ex9 - Médias dos alunos:")
for aluno, lista in notas.items():
    print(f"{aluno}: {sum(lista)/len(lista)}")
print()


# Exercício 10 - Contar palavras

frase = input("Ex10 - Introduz uma frase: ")
palavras = frase.split()
contador_palavras = {}
for p in palavras:
    contador_palavras[p] = contador_palavras.get(p, 0) + 1
print("Contagem de palavras:", contador_palavras)