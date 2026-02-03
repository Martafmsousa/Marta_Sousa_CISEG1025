import re

def extrair_telemoveis():
    with open("dados.txt", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()
        
        padrao = r'\d{3}[- ]?\d{3}[- ]?\d{3}'
        
        telemoveis = re.findall(padrao, conteudo)
        
        for numero in telemoveis:
            print(numero)

if __name__ == "__main__":
    extrair_telemoveis()