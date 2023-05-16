array1 = []
array2 = []
array3 = []
array4 = []

num = 0

while(num >= 0):
    num = int(input('insira um numero: '))
    if(0 <= num <= 25):
        array1.append(num)
    elif(26 <= num <= 50):
        array2.append(num)
    elif(51 <= num <= 75):
        array3.append(num)
    elif(76 <= num <= 100):
        array4.append(num)

print(f'numeros entre 0 e 25: {len(array1)}')
print(f'numeros entre 26 e 50: {len(array2)}')
print(f'numeros entre 51 e 75: {len(array3)}')
print(f'numeros entre 76 e 100: {len(array4)}')
