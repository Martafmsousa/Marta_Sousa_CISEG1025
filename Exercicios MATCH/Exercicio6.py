# Exercício 6 – Estado do servidor

status = input("Status (ok/erro): ").lower()
tempo = int(input("Tempo de resposta (ms): "))

dados = {"status": status, "tempo_resposta": tempo}

match dados:
    case {"status": "ok", "tempo_resposta": t} if t > 200:
        print("Servidor lento")
    case {"status": "ok", "tempo_resposta": _}:
        print("Servidor ativo")
    case {"status": "erro", "tempo_resposta": _}:
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")
