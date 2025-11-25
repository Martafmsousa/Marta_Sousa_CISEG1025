# Teste Final 1

# ============================
#     FUNÇÕES DE CÁLCULO
# ============================

def eh_primo(n):
    if n < 2:
        return False
    div = 0
    for i in range(1, n+1):
        if n % i == 0:
            div += 1
    return div == 2


def contar_divisores(n):
    total = 0
    for i in range(1, n+1):
        if n % i == 0:
            total += 1
    return total


def eh_perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma == n


# ============================
#     FUNÇÃO PRINCIPAL DO TESTE
# ============================

def analisar_numeros():
    
    while True:
        valor = int(input("Digite um valor entre 1 e 30000: "))
        if 1 <= valor <= 30000:
            break
        print("Entrada inválida.")

    contador = 0

    
    for num in range(valor, 0, -1):
        print("\nNúmero:", num)
        print("Primo:", "Sim" if eh_primo(num) else "Não")
        print("Divisores:", contar_divisores(num))
        print("Perfeito:", "Sim" if eh_perfeito(num) else "Não")

        contador += 1

        
        if contador == 10:
            continuar = input("\nDeseja continuar? (s/n): ")
            if continuar.lower() != "s":
                break
            contador = 0


# ============================
#     MENU DA CALCULADORA
# ============================

def tabuada():
   
    while True:
        n = int(input("Digite um número entre 1 e 1000: "))
        if 1 <= n <= 1000:
            break
        print("Valor inválido.")

    contador = 0

    for i in range(1, n+1):
        print(n, "x", i, "=", n * i)
        contador += 1

        if contador == 20:
            input("Pressione ENTER para continuar...")
            contador = 0


def calculadora():
    while True:
        print("\n===== MENU CALCULADORA =====")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Tabuada")
        print("0 - Voltar ao menu principal")

        op = input("Escolha uma opção: ")

        if op == "0":
            break
        elif op == "5":
            tabuada()
        else:
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))

            if op == "1":
                print("Resultado:", a + b)
            elif op == "2":
                print("Resultado:", a - b)
            elif op == "3":
                print("Resultado:", a * b)
            elif op == "4":
                if b == 0:
                    print("Impossível dividir por zero")
                else:
                    print("Resultado:", a / b)
            else:
                print("Opção inválida!")


# ============================
#     MENU GERAL DO PROGRAMA
# ============================

def main():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Analisar números (primo, divisores, perfeito)")
        print("2 - Calculadora + Tabuada")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            analisar_numeros()
        elif opcao == "2":
            calculadora()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")


# INICIAR PROGRAMA
main()


