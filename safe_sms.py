def criar_dicionario_criptografia():
    return {
'a': '@', 'b': '8', 'c': '(', 'd': '6', 'e': '3',
'f': '#', 'g': '9', 'h': '4', 'i': '1', 'j': '7',
'k': '<', 'l': '*_', 'm': '^^', 'n': '^', 'o': '0',
'p': '?', 'q': '&', 'r': '2', 's': '5', 't': '+',
'u': 'µ', 'v': '√', 'w': 'ω', 'x': '×', 'y': '¥',
'z': '%', ' ': '~' '-'
    }

def criar_dicionario_reverso(dicionario):
    return {v: k for k, v in dicionario.items()}

def codificar(texto, dicionario):
    texto = texto.lower()
    texto_codificado = ""
    
    for char in texto:
        if char in dicionario:
            texto_codificado += dicionario[char]
        else:
            texto_codificado += char
    texto_codificado = texto_codificado[::-1] #ola alo
    
    return texto_codificado

def descodificar(texto_codificado, dicionario_reverso):
    texto_invertido = texto_codificado[::-1]
    
    texto_descodificado = ""
    i = 0
    
    while i < len(texto_invertido):
        if i + 1 < len(texto_invertido):
            dois_chars = texto_invertido[i:i+2]
            if dois_chars in dicionario_reverso:
                texto_descodificado += dicionario_reverso[dois_chars]
                i += 2
                continue
        
        
        char = texto_invertido[i]
        if char in dicionario_reverso:
            texto_descodificado += dicionario_reverso[char]
        else:
            texto_descodificado += char
        i += 1
    
    return texto_descodificado

def main():
    dicionario = criar_dicionario_criptografia()
    dicionario_reverso = criar_dicionario_reverso(dicionario)
    
    print("=" * 50)
    print("          SISTEMA DE CRIPTOGRAFIA SMS")
    print("=" * 50)
    
    while True:
        print("\nOpções:")
        print("1 - Codificar texto")
        print("2 - Descodificar texto")
        print("3 - Sair")
        
        opcao = input("\nEscolha uma opção (1-3): ").strip()
        
        if opcao == '1':
            texto = input("Digite o texto para codificar: ")
            texto_codificado = codificar(texto, dicionario)
            print(f"\nTexto codificado: {texto_codificado}")
            
        elif opcao == '2':
            texto_codificado = input("Digite o texto para descodificar: ")
            try:
                texto_descodificado = descodificar(texto_codificado, dicionario_reverso)
                print(f"\nTexto descodificado: {texto_descodificado}")
            except:
                print("Erro: Texto codificado inválido!")
                
        elif opcao == '3':
            print("Saindo do sistema...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
