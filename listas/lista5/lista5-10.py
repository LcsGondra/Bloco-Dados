def gerar_matriz(N):
    matrix = []
    for i in range(N):
        line = []
        for j in range(N):
            line.append(0)
        matrix.append(line)
    return matrix

print(gerar_matriz(4))