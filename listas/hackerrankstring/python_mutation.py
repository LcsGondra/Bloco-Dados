def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:] 
    return string

s = input('string: ')
i, c = input('posicao e caracter (posicao "espaco" caracter):').split()
s_new = mutate_string(s, int(i), c)
print(s_new)