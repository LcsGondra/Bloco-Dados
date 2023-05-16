import random
from collections import Counter
votos = []
for i in range(100):
    votos.append(random.randint(1,6))

# a
list = Counter(votos)

print(list)
print(f'porcentagem de nulos: {(list[5]/len(votos))*100}%')
print(f'porcentagem de votos brancos{(list[6]/len(votos))*100}%')
