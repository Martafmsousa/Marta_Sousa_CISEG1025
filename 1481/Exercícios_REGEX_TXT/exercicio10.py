import re

def extrair_dominios():
    with open("registos.txt", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()
        
        padrao = r'https?://([^\s|]+)'
        
        dominios = re.findall(padrao, conteudo)
        
        for dominio in dominios:
            print(dominio)

if __name__ == "__main__":
    extrair_dominios()