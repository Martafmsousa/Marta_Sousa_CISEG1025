import re

def validar_emails_pt():
    with open("dados.txt", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()
        
        padrao = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.pt\b'
        
        emails = re.findall(padrao, conteudo)
        
        for email in emails:
            print(email)

if __name__ == "__main__":
    validar_emails_pt()