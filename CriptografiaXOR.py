#CriptografiaXor

ascii = {"a": "01000001", "b": "01000010", "c": "01000011", "d": "01000100", "e": "01000101", "f": "01000110", "g": "01000111", "h": "01001000", "i": "01001001", "j": "01001010", "k": "01001011",
         "l": "01001100", "m": "01001101", "n": "01001110","o": "01001111", "p": "01010000", "q": "01010001", "r": "01010010", "s": "01010011","t": "01010100","u": "01010101", "v": "01010110",
         "w": "01010111", "x": "01011000","y": "01011001", "z": "01011010"}

q = int(input("Qual o número de letras da palavra: "))
chave = input("Digite a chave: ")
c = ""
aux = 1
while aux <= q:
    if aux == 1:
        l = input("Digite a primeira letra: ")
        l = ascii[l]
        for i in range(0,8):
            if l[i] == chave[i]:
                c = c + "0"
            else:
                c = c + "1"
        c = c + " "
        aux += 1
    elif aux > 1 and aux < q:
        l = input("Digite a proxima letra: ")
        l = ascii[l]
        for i in range(0, 8):
            if l[i] == chave[i]:
                c = c + "0"
            else:
                c = c + "1"
        c = c + " "
        aux += 1
    else:
        l = input("Digite a última letra: ")
        l = ascii[l]
        for i in range(0, 8):
            if l[i] == chave[i]:
                c = c + "0"
            else:
                c = c + "1"
        c = c + " "
        aux += 1
print(c)
