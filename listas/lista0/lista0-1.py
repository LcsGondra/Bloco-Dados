pares = 0
impares = 0
for i in range(3):
    numero = int(input(f'Insira o {i+1}º numero: '))
    if(numero % 2 == 0):
        pares += 1
    else:
        impares += 1

print(f'quantidade de numeros pares: {pares}')
print(f'quantidade de numeros impares: {impares}')
