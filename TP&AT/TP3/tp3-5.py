M = int(input('minuto que teodoro comecou o tp: '))
I = int(input('intervalo que teodoro verifica as msg: '))
L = int(input('minuto que larry enviou uma msg: '))

mins1 = M + I
if L <= mins1:
    print(mins1)
else:
    mins2 = mins1 + I
    if L <= mins2:
        print(mins2)
    else:
        mins3 = mins2 + I
        if L <= mins3:
            print(mins3)
        else:
            print('Quem sabe...')


