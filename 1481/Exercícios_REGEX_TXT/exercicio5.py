import re

def guardar_dados_extraidos():
    with open("dados.txt", "r", encoding="utf-8") as origem:
        linhas = origem.readlines()
    
    with open("extraidos.txt", "w", encoding="utf-8") as destino:
        for linha in linhas:
            nome = re.search(r"Nome:\s*([^,]+)", linha)
            email = re.search(r"Email:\s*([^\s,]+)", linha)
            telemovel = re.search(r"Telemóvel:\s*(.*)", linha)
            
            if nome and email and telemovel:
                n = nome.group(1).strip()
                e = email.group(1).strip()
                t = telemovel.group(1).strip()
                destino.write(f"{n} | {e} | {t}\n")

if __name__ == "__main__":
    guardar_dados_extraidos()