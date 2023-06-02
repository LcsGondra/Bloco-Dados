jogadores = input('Jogadores, dividido por espaco: ').split()
numeros = list(map(int,input('numero escolhido pelos respectivos jogadores, dividido por espaco: ').split()))

if sum(numeros) %2 == 0:
    print(jogadores[0])
else:
    print(jogadores[1])
