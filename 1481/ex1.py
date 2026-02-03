import sys

def validar_nome_ascii():
   
    nome = input("Introduza o seu nome completo: ")

    if not nome:
        print("Nome inválido: contém caracteres não permitidos.")
        sys.exit()

    for i in range(len(nome)):
        char = nome[i]
        codigo = ord(char)

    
        if not (codigo == 32 or (65 <= codigo <= 90) or (97 <= codigo <= 122)):
            print("Nome inválido: contém caracteres não permitidos.")
            sys.exit()

    
        if i == 0 or ord(nome[i-1]) == 32:
            if not (65 <= codigo <= 90): 
                print("Nome inválido: contém caracteres não permitidos.")
                sys.exit()
        
    
        else:
            if (65 <= codigo <= 90): 
                print("Nome inválido: contém caracteres não permitidos.")
                sys.exit()

    print("Nome válido!")

if __name__ == "__main__":
    validar_nome_ascii()