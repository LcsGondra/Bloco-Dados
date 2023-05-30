ddds = {
    11:'sao paulo',
    19:'Campinas',
    21:'Rio de Janeiro',
    27:'Vitória',
    31:'Belo Horizonte',
    32:'Juiz de Fora',
    61:'Brasília',
    71:'Salvador'
}
codigo = int(input('numero do ddd: '))
if codigo not in ddds:
    print('DDD não cadastrado')
else:
    print(ddds[codigo])