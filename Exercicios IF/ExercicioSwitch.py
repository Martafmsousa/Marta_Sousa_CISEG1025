# Exercício Switch – Exibir nome do mês

mes = int(input("Número do mês (1 a 12): "))

meses = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}

if mes in meses:
    print("Mês:", meses[mes])
else:
    print("Número inválido!")

