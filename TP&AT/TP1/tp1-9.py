import random

vetor_dados = []
for i in range(50):
    vetor_dados.append(random.randint(1,6))


def check_6(vetor):
    print(f'quantidade de vezes que rolou 6: {vetor.count(6)}')

check_6(vetor_dados)
