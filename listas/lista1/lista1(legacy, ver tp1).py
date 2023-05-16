# import random
# exercicio1
# tuples = ((1,5,6,10), (2,4,6,8), (2,), (10,20,30,10,80))
# media_sum = 0
# for t in tuples:
#     soma = 0
#     for i in t:
#         soma += i
#     media_sum += soma
#     print(f'tupla: {tuples.index(t)} | soma: {soma}')

# print(f'media: {media_sum/len(tuples)}')

#exercicio2

# n = int(input('insira a quantidade de termos: '))

# termos = []
# for i in range(1, n+1):
#     termo = f'{i}/{(i*2)-1}'
#     termos.append(termo)

# print(termos)

#exercicio 3
# ex_list = [3,7,2,4,9]
# def cumsum(list):
#     new_list = []
#     soma = 0
#     for i in list:
#         soma += i
#         new_list.append(soma)
#     print(f'{new_list}')

# cumsum(ex_list)

#exercicio 4

# palind = ['radar', 'toot', 'bsalbsal', 'Socorram-me subi no ônibus em marrocos']
# import re
# for i in palind:
#     j = i.lower()
#     pattern = '[^A-Za-z0-9]+'
#     j = re.sub(pattern, '', j)
#     print(f'{i} eh um palindromo? {j == j[::-1]}')

# exercicio 5

#minha forma
# def gerar_niver(aniversarios):
#     aniversarios.clear()
#     for i in range(1,24):
#         mm = random.randint(1,12)
#         if mm == 2:
#             dd = random.randint(1,28)
#             aniversarios.append([dd,mm])
#         elif mm in (4, 6, 9, 11) :
#             dd = random.randint(1,30)
#             aniversarios.append([dd,mm])
#         else:
#             dd = random.randint(1,31)
#             aniversarios.append([dd,mm])
#     return aniversarios
# match = False
    

# salas = 0
# while (not match):
#     aniversarios = []
#     gerar_niver(aniversarios)
#     outros_niver = aniversarios.copy()
#     for a in aniversarios:
#         outros_niver.pop(0)
#         for b in outros_niver:
#             if a == b:
#                 match = True
#     salas += 1

# print(match)
# print(f'{1}/{salas}')

# melhor forma

# def gerar_niver():
#     aniversario = []
#     mm = random.randint(1,12)
#     if mm == 2:
#         dd = random.randint(1,28)
#         aniversario = [dd,mm]
#     elif mm in (4, 6, 9, 11) :
#         dd = random.randint(1,30)
#         aniversario = [dd,mm]
#     else:
#         dd = random.randint(1,31)
#         aniversario = [dd,mm]
#     return aniversario


# salas, match  = 0, 0
# for i in range(1000):
#     salas += 1
#     aniversarios = []
#     for j in range(0,23):
#         novo_niver = gerar_niver()
#         if novo_niver in aniversarios:
#             match += 1
#         else:
#             aniversarios.append(novo_niver)

# print(f'{match}/{salas}')

#exercicio 6

# vetor_1 = [1,3,6]

# vetor_2 = [2,5,9,5]

# def soma_vect(v1, v2):
#     vetor_somas = []
#     if len(v1) > len(v2):
#         big_v = len(v1)
#     else:
#         big_v = len(v2)

#     for i in range(big_v):
#         if len(v2)-1 < i:
#             vetor_somas.append(v1[i])
#         elif len(v1)-1 < i:
#             vetor_somas.append(v2[i])
#         else:
#             vetor_somas.append(v1[i] + v2[i])
#     return vetor_somas

# print(soma_vect(vetor_1, vetor_2))

#exercicio 7
# vetor_10 = []
# def fill_vect():
#     for i in range(10):
#         n = input('insira um valor do vetor: ')
#         vetor_10.append(n)

# fill_vect()
# print(len(set(vetor_10)))


