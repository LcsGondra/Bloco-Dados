data = '29/10/1973'
data_split = data.split('/')
dia = data_split[0]
mes = data_split[1]
ano = data_split[2]
mes_dict = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril',
            5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro',
            10: 'outubro', 11: 'novembro', 12: 'dezembro' }
print(f' {dia} de {mes_dict[int(mes)]} de {ano}')
