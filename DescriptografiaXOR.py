#DescriptografiaXor

ascii = { "01000001":"a", "01000010":"b", "01000011":"c", "01000100":"d", "01000101":"e", "01000110":"f", "01000111":"g", "01001000":"h", "01001001":"i", "01001010":"j", "01001011":"k",
        "01001100":"l", "01001101":"m", "01001110":"n", "01001111":"o", "01010000":"p", "01010001":"q", "01010010":"r", "01010011":"s", "01010100":"t", "01010101":"u", "01010110":"v",
        "01010111":"w", "01011000":"x", "01011001":"y", "01011010":"z"}

q = int(input("Quantas letras serão descriptografadas: "))
chave = input("Digite a chave: ")
p = ""
aux = 1
while aux <= q:
    print("{}ºparte".format(aux))
    l = input("Digite: ")
    c = ""
    for i in range(0,8):
        if l[i] == chave[i]:
            c = c +"0"
        else:
            c = c +"1"
    p = p + ascii[c]
    aux += 1
print(p)
