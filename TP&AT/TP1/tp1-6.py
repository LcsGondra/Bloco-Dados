vetor_1 = []
for i in range(3):
    vetor_1.append(int(input('insira um numero para adicionar ao vetor 1: ')))

vetor_2 = []
for i in range(3):
    vetor_2.append(int(input('insira um numero para adicionar ao vetor 2: ')))

def soma_vetor(v1,v2):
    vetor_3= []
    for i in range(3):
        vetor_3.append(v1[i] + v2[i])
    print(vetor_3)

soma_vetor(vetor_1, vetor_2)