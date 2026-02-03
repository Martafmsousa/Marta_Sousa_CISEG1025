import re

def extrair_codigos_postais():
    with open("registos.txt", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()
        
        padrao = r'\d{4}-\d{3}'
        
        codigos = re.findall(padrao, conteudo)
        
        for cp in codigos:
            print(cp)

if __name__ == "__main__":
    extrair_codigos_postais()