lista_num = [1, 67, 78, 34, 90, 876, 0, 12, 8, 3, 56, 987, 3, 2,45,12,10, 45]

def detect_num(lista, numero):
    if numero in lista:
        print(f'quantidade de vezes que {numero} aparece: {lista.count(numero)}')
    else:
        print(f'o numero {numero} nao aparece na lista')
detect_num(lista_num, int(input('insira um numero para detectar na lista : ')))