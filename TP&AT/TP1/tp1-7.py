vetor = []
for i in range(10):
    vetor.append(input('insira um numero para adicionar ao vetor: '))

print(f'valores diferentes no vetor inserido: {len(set(vetor))}')