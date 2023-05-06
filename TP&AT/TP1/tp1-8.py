vetor = []
for i in range(5):
    vetor.append(int(input('insira um numero para adicionar ao vetor: ')))

def posicao(valor, vetor):
    if vetor.count(valor) == 0:
        print('-1')
    else:
        print(f'posicao {vetor.index(valor)}')

posicao(int(input('insira um numero para achar a posicao no vetor: ')), vetor)