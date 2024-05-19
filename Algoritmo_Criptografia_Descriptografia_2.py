question = input("Voce gostaria de criptografar ou descriptografar uma mensagem?")

if question == "Criptografar" or question == "criptografar" or question == "CRIPTOGRAFAR":
    ascii = {"a": "01000001", "b": "01000010", "c": "01000011", "d": "01000100", "e": "01000101", "f": "01000110",
             "g": "01000111", "h": "01001000", "i": "01001001", "j": "01001010", "k": "01001011",
             "l": "01001100", "m": "01001101", "n": "01001110", "o": "01001111", "p": "01010000", "q": "01010001",
             "r": "01010010", "s": "01010011", "t": "01010100", "u": "01010101", "v": "01010110",
             "w": "01010111", "x": "01011000", "y": "01011001", "z": "01011010"}

    palavra = input("Digite a palavra: ")
    chave = input("Digite a chave: ")
    cifra = ""
    chave_binario = ""
    palavra_binario = ""


    for letra in palavra:
        aux = ascii[letra]
        palavra_binario = palavra_binario + aux


    for letra in chave:
        aux = ascii[letra]
        chave_binario = chave_binario + aux

    if len(palavra) > len(chave):
        complemento = len(palavra) - len(chave)
        question = input("Voce gostaria de complementar a chave para ficar do mesmo tamanho da mensagem ou podemos complementar com 0s (não recomendado): \n Digite SIM para adicionar complemento e NÃO para adicionarmos 0s a sua chave.\n")
        if question == "Não" or question == "NÃO" or question == "não":
            complemento = complemento * "0"
            chave_binario = chave_binario + complemento
        else:
            complemento = input("Digite o complemento: ")
            for letra in complemento:
                aux = ascii[letra]
                chave_binario = chave_binario + aux


    for i in range(0, len(palavra_binario)):
        if palavra_binario[i] == chave_binario[i]:
             cifra = cifra + "0"
        else:
             cifra = cifra + "1"

    print(cifra)

elif question == "Descriptografar" or question == "descriptografar" or question == "DESCRIPTOGRAFAR":

    ascii = {"01000001": "a", "01000010": "b", "01000011": "c", "01000100": "d", "01000101": "e", "01000110": "f",
             "01000111": "g", "01001000": "h", "01001001": "i", "01001010": "j", "01001011": "k",
             "01001100": "l", "01001101": "m", "01001110": "n", "01001111": "o", "01010000": "p", "01010001": "q",
             "01010010": "r", "01010011": "s", "01010100": "t", "01010101": "u", "01010110": "v",
             "01010111": "w", "01011000": "x", "01011001": "y", "01011010": "z"}

    cifra = input("Digite a cifra: ")
    chave = input("Digite a chave: ")
    texto_claro = ""
    texto_bin = ""


    for i in range(0, len(cifra)):
        if cifra[i] == chave[i]:
            texto_bin = texto_bin + "0"
        else:
            texto_bin = texto_bin + "1"



    for k in range(0,len(texto_bin),8):
        aux = texto_bin[k:k+8]
        aux = ascii[aux]
        texto_claro = texto_claro + aux

    print(texto_claro)

else:
    print("Opção Invalida")