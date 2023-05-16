frase = "a ligeira raposa marrom saltou sobre o cachorro cansado"
fraselist = frase.split(' ')

def cifra(lista):
    frase_plus = []
    for palavra in lista:
        palavra_plus = []
        for c in list(palavra):
            c_plus = ord(c)+3
            palavra_plus.append(chr(c_plus))
        frase_plus.append(''.join(palavra_plus))
    return frase_plus

print(f"frase original: {frase} \nfrase cifrada + 3: {' '.join(cifra(fraselist))}")

