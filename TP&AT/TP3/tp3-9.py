pos = []
for i in range(6):
    valor = float(input('insira um numero:'))
    if valor > 0:
        pos.append(valor)

print(f"{len(pos)} valor(es) positivos")
print(f"{sum(pos)/len(pos)}")