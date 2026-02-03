import re

def extrair_nifs():
    with open("registos.txt", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()
        
        padrao = r'\b\d{9}\b'
        
        nifs = re.findall(padrao, conteudo)
        
        for nif in nifs:
            print(nif)

if __name__ == "__main__":
    extrair_nifs()