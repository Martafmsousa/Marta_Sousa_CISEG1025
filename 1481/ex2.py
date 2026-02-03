import sys

def criptografar(mensagem: str, chave: str):
    if not chave:
        print("Erro: A chave não pode ser vazia.")
        sys.exit()
    
    soma_chave = 0
    for c in chave:
        soma_chave += ord(c)
        
    codigos = []
    for char in mensagem:
        cifrado = ((ord(char) - 32 + soma_chave) % 95) + 32
        codigos.append(cifrado)
    return codigos

def descriptografar(codigos: list, chave: str):
    if not chave:
        sys.exit()
        
    soma_chave = 0
    for c in chave:
        soma_chave += ord(c)
        
    original = ""
    for num in codigos:
        decifrado = ((num - 32 - soma_chave) % 95) + 32
        original += chr(decifrado)
    return original

def listar(codigos: list):
    print(f"Lista de códigos ASCII: {codigos}")
    visual = ""
    for n in codigos:
        visual += chr(n)
    print(f"Mensagem encriptada: {visual}")

def main():
    msg = input("Introduza a mensagem: ")
    chave = input("Introduza a chave string: ")
    
    if not chave:
        print("Erro: A chave não pode ser vazia.")
        return

    resultado_codigos = criptografar(msg, chave)
    listar(resultado_codigos)
    
    msg_final = descriptografar(resultado_codigos, chave)
    print(f"Mensagem original recuperada: {msg_final}")

if __name__ == "__main__":
    main()