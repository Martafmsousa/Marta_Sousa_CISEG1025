# Exercício 8 – Média de 10 notas e contagem acima da média

notas = []
for i in range(10):
    nota = float(input("Nota do aluno " + str(i+1) + ": "))
    notas.append(nota)

media = sum(notas) / 10

acima_media = 0
for nota in notas:
    if nota >= media:
        acima_media += 1

print("Média da turma:", round(media, 1))
print("Alunos com nota >= média:", acima_media)
