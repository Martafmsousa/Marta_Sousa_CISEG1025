# Exercício 1 – Converter segundos em horas, minutos e segundos

segundos = int(input("Quantos segundos? "))

horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

print(horas, "hora(s),", minutos, "minuto(s) e", segundos, "segundo(s)")
