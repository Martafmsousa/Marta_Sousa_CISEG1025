import re

def validar_nifs_validos():
    with open("registos.txt", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()
        
        padrao = r'\b[123568]\d{8}\b'
        
        nifs_validos = re.findall(padrao, conteudo)
        
        for nif in nifs_validos:
            print(nif)

if __name__ == "__main__":
    validar_nifs_validos()