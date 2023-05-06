import random

vet = []
for i in range(20):
    vet.append(random.randrange(-10, 10))

print(f'vetor original: {vet}')
vet_pos = []
for i in vet:
    if i >= 0:
        vet_pos.append(i)

print(f'vetor com positivos: {vet_pos}')
print(f'vetor sem repeticao: {set(vet_pos)}')