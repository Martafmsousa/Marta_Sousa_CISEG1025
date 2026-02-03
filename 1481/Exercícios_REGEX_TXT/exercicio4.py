import re

def extrair_nomes():
    with open("dados.txt", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()
        
        padrao = r"Nome:\s*([^,]+)"
        
        nomes = re.findall(padrao, conteudo)
        
        for nome in nomes:
            print(nome.strip())

if __name__ == "__main__":
    extrair_nomes()