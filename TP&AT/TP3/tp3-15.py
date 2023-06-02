salario = float(input('Salario: '))

if salario <= 1600.00:
    print(f'Novo salario: R$ {round(salario*1.15, 2)} \nReajuste ganho: {round(salario*.15, 2)}\nEm percentual: 15%')
elif 1600.00 < salario <= 2400.00:
    print(f'Novo salario: R$ {round(salario*1.12, 2)} \nReajuste ganho: {round(salario*.12, 2)}\nEm percentual: 12%')
elif 2400.00 < salario <= 4000.00:
    print(f'Novo salario: R$ {round(salario*1.10, 2)} \nReajuste ganho: {round(salario*.10, 2)}\nEm percentual: 10%')
else:
    print(f'Novo salario: R$ {round(salario*1.07, 2)} \nReajuste ganho: {round(salario*.07, 2)}\nEm percentual: 7%')
