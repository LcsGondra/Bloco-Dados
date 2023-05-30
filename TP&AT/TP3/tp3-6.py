B = int(input('temperatura que a agua comeca a ferver: '))

pressao = (5*B) - 400

print(pressao)
if pressao > 100:
    print("-1")
elif pressao == 100:
    print('0')
else:
    print('1')