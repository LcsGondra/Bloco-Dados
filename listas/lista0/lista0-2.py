primo = int(input('insira um numero para verificar a primalidade: '))

for i in range(2, primo):
    if(primo % i == 0):
        print(f'o numero {primo} nao eh primo')
        break
    
print(f'o numero {primo} eh primo')