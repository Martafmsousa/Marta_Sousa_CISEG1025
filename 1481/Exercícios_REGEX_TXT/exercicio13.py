import re
from datetime import datetime

def filtrar_datas_anteriores_2025():
    try:
        with open("registos.txt", "r", encoding="utf-8") as ficheiro:
            linhas = ficheiro.readlines()
            
            for linha in linhas:
                match = re.search(r'(\d{2}/\d{2}/\d{4})', linha)
                
                if match:
                    data_str = match.group(1)
                    data_objeto = datetime.strptime(data_str, "%d/%m/%Y")
                    
                    if data_objeto.year < 2025:
                        print(f"Registo encontrado: {linha.strip()}")
                        
    except FileNotFoundError:
        print("Erro: O ficheiro 'registos.txt' não foi encontrado.")

if __name__ == "__main__":
    filtrar_datas_anteriores_2025()