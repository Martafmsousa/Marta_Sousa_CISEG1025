def ler_ficheiro():
    with open("dados.txt", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()
        print(conteudo)

if __name__ == "__main__":
    ler_ficheiro()