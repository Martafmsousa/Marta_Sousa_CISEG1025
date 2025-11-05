# Exercício 5 – Análise de mensagem

msg = input("Mensagem: ").lower()

match msg:
    case m if m in ["olá", "ola", "bom dia"]:
        print("Saudação")
    case m if m.endswith("?"):
        print("Pergunta")
    case m if "tchau" in m or "adeus" in m:
        print("Despedida")
    case _:
        print("Mensagem genérica")
