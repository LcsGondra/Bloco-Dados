import random
b_days = []
def gen_bday(bd):
    for i in range (0,23):
        mm = random.randint(1,12)
        if mm == 2:
            dd = random.randint(1,28)
            bd.append(f'{dd}/{mm}')
        elif mm in [4,6,9,11]:
            dd = random.randint(1,30)
            bd.append(f'{dd}/{mm}')
        else:
            dd = random.randint(1,31)
            bd.append(f'{dd}/{mm}')

gen_bday(b_days)

matches = 0
salas = 1
while matches == 0:
    for i in range(0,23):
        if b_days.count(b_days[i]) >= 2:
            matches += (b_days.count(b_days[i])-1)
            print(f'niver repetido: {b_days[i]} \nchance: {matches}/{salas}')
            break
    b_days.clear()
    gen_bday(b_days)
    salas += 1



