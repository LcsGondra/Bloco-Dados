def serie_termos(n):
    lista_termos = []
    soma = 0
    for i in range(1,n+1):
        if i == 1:
            lista_termos.append(f'{i}/{i}')
            soma += (i/i)
        else:
            lista_termos.append(f'{i}/{i+1}')
            soma += (i/(i+1))
        
    print(lista_termos)
    print(soma)

serie_termos(int(input('insira um numero para ver a serie: ')))
