# string = input('informe uma frase: ')
string_inserida = 'frase inserida de teste'
n_branco = string_inserida.count(' ')
n_vogal_a = string_inserida.count('a')
n_vogal_e = string_inserida.count('e')
n_vogal_i = string_inserida.count('i')
n_vogal_o = string_inserida.count('o')
n_vogal_u = string_inserida.count('u')

print(f'numero de espacos em branco: \n{n_branco}')
print(f"""numero de vogais:
a : {n_vogal_a}
e : {n_vogal_e}
i : {n_vogal_i}
o : {n_vogal_o}
u : {n_vogal_u}""")
