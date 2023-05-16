import random
numeros = []
for i in range(10):
    numeros.append(random.randint(0,100))
print(numeros)
if len(set(numeros)) < len(numeros):
    print('existem duplicatas')
else:
    print('nao existem duplicatas')

dic_nums = {}
for i in numeros:
    dic_nums[i] = numeros.count(i)
print(dic_nums)
