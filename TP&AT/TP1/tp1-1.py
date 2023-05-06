tupla_sq = ((1,5,6,10), (2,4,6,8), (2,), (10,20,30,10,80))
soma_total = 0
for t in tupla_sq:
    t_sum = sum(t)
    soma_total += t_sum
    print(f'{tupla_sq.index(t)} : {t_sum}')

print(f'Media Total: {soma_total/len(tupla_sq)}')