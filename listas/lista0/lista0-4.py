tabuada = int(input('montar a tabuada de: '))
inicio = int(input('comecar por: '))
fim = int(input('terminar em: '))
print('Tabuada:')
for i in range(inicio, fim+1):
    print(f'{tabuada}X{i} = {tabuada*i}')