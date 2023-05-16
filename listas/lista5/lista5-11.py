def gerar_matriz(N):
    matrix = []
    c = 1
    for i in range(N):
        line = []
        for j in range(N):
            line.append(i+j+c)
        matrix.append(line)
        c += N-1
    return matrix

print(gerar_matriz(4))


# ou com numpy

import numpy as np

n = int(input('n: '))

print(np.arange(n*n).replace(n,n))