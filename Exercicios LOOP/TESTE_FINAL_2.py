# Teste Final 2

# ========================================
#        BASE DE DADOS DE CLIENTES
# ========================================

clientes = []        # lista de clientes
proximo_num = 1      # número automático


# -------------------------
#     FUNÇÃO DE VALIDAÇÃO
# -------------------------
def ler_numero(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("Valor inválido.")
            else:
                return valor
        except:
            print("Entrada inválida.")


def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto != "":
            return texto
        else:
            print("Campo obrigatório!")


# -------------------------
#     CÁLCULO DO DESCONTO
# -------------------------
def calcular_desconto(compra):
    if 100 <= compra <= 200:
        return compra * 0.05
    elif 200 < compra < 500:
        return compra * 0.10
    elif compra >= 500:
        return compra * 0.15
    else:
        return 0


# -----------------------------------
#     INSERIR NOVO CLIENTE
# -----------------------------------
def inserir_cliente():
    global proximo_num

    print("\n=== INSERIR CLIENTE ===")

    nome = ler_texto("Nome: ")
    morada = ler_texto("Morada: ")
    telefone = ler_texto("Telefone: ")
    nif = ler_texto("NIF: ")
    compra = ler_numero("Valor da compra: ")

    desconto = calcular_desconto(compra)
    div_final = compra - desconto

    cliente = {
        "num": proximo_num,
        "nome": nome,
        "morada": morada,
        "telefone": telefone,
        "nif": nif,
        "compra": compra,
        "desconto": desconto,
        "div_final": div_final
    }

    clientes.append(cliente)
    print(f"\nCliente inserido com sucesso! Número do cliente: {proximo_num}\n")

    proximo_num += 1


# -----------------------------------
#     LISTAR CLIENTES (1 a 1)
# -----------------------------------
def listar_clientes():
    if len(clientes) == 0:
        print("\nNão existem clientes registados.\n")
        return

    print("\n==== LISTAGEM DE CLIENTES ====\n")

    for cliente in clientes:
        print(f"Número: {cliente['num']}")
        print(f"Nome: {cliente['nome']}")
        print(f"Morada: {cliente['morada']}")
        print(f"Telefone: {cliente['telefone']}")
        print(f"NIF: {cliente['nif']}")
        print(f"Compra: {cliente['compra']} €")
        print(f"Desconto: {cliente['desconto']} €")
        print(f"Valor Final: {cliente['div_final']} €")
        print("\n--------------------------\n")

        continuar = input("ENTER para continuar, 'sair' para parar: ")
        if continuar.lower() == "sair":
            break


# -----------------------------------
#     PESQUISAR POR NÚMERO
# -----------------------------------
def pesquisar_cliente():
    if len(clientes) == 0:
        print("\nNão existem clientes registados.\n")
        return

    num = int(ler_numero("Digite o número do cliente: "))

    encontrado = False

    for cliente in clientes:
        if cliente["num"] == num:
            encontrado = True
            print("\n=== CLIENTE ENCONTRADO ===")
            print(f"Número: {cliente['num']}")
            print(f"Nome: {cliente['nome']}")
            print(f"Morada: {cliente['morada']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"NIF: {cliente['nif']}")
            print(f"Compra: {cliente['compra']} €")
            print(f"Desconto: {cliente['desconto']} €")
            print(f"Valor Final: {cliente['div_final']} €")
            print()
            break

    if not encontrado:
        print("Cliente não encontrado.")


# -----------------------------------
#     MENU PRINCIPAL
# -----------------------------------
def main():
    while True:
        print("\n======= MENU CLIENTES =======")
        print("1 - Inserir Cliente")
        print("2 - Listar Clientes")
        print("3 - Pesquisar Cliente por Número")
        print("0 - Sair")
        print("==============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            pesquisar_cliente()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")


# INICIAR PROGRAMA
main()
