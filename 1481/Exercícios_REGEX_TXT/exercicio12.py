import re

def criar_resumo():
    with open("registos.txt", "r", encoding="utf-8") as origem:
        linhas = origem.readlines()
    
    with open("resumo.txt", "w", encoding="utf-8") as destino:
        for linha in linhas:
            nome = re.search(r"Nome:\s*([^|]+)", linha)
            nif = re.search(r"NIF:\s*(\d{9})", linha)
            data = re.search(r"Data:\s*(\d{2}/\d{2}/\d{4})", linha)
            cp = re.search(r"Código Postal:\s*(\d{4}-\d{3})", linha)
            site = re.search(r"https?://([^\s|]+)", linha)
            
            if nome and nif and data and cp and site:
                n = nome.group(1).strip()
                ni = nif.group(1).strip()
                d = data.group(1).strip()
                c = cp.group(1).strip()
                s = site.group(1).strip()
                
                destino.write(f"{n} | {ni} | {d} | {c} | {s}\n")

if __name__ == "__main__":
    criar_resumo()