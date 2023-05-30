#nome do programa
print('Bem vindo ao AVALIADOR') 

#linha para o usuario informar o percentual
percent = int(input("informe o percentual de exercicios executados corretamente(0-100 sem %): "))

#aqui verifica se o usuario inseriu valores validos
if percent > 100:
    print('valor muito alto, o valor deve ser entre 100 e 0')
if percent < 0:
    print('valor muito baixo, o valor deve ser entre 100 e 0')

#aqui verifica se o valor se encaixa em uma das possibilidades abaixo:
#possibilidade 1: porcentagem abaixo de 60, nota nd, aluno precisa refazer
if percent < 60:
    print('aluno NÃO PASSOU')
    print('Necessário refazer')
    print('Conceito: "ND"')
#possibilidade 2: porcentagem acima de 60, aluno passou
if percent >= 60:
    print('aluno PASSOU')
#imprime d se o valor foi ente 60 e 89
if 60 <= percent <= 89:
    print('Conceito: "D"')
#imprime dl se o valor foi entre 90 e 99
if 90 <= percent <= 99:
    print('Conceito: "DL"')
#imprime dml se o valor foi igual a 100
if percent == 100:
    print('Conceito: "DML"')