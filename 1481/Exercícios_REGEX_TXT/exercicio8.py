import re

def extrair_datas():
    with open("registos.txt", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()
        
        padrao = r'\d{2}/\d{2}/\d{4}'
        
        datas = re.findall(padrao, conteudo)
        
        for data in datas:
            print(data)

if __name__ == "__main__":
    extrair_datas()