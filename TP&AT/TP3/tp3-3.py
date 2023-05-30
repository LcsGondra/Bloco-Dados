numero = 5
print("Eu pensei em um número entre 1 e 10")
palpite = int(input("Você consegue adivinhar qual é?"))
if palpite == numero:
    print("Correto!")
if palpite < numero:
    print("Baixo Demais!")
    print("Azar") #adicionado print caso palpite nao seja igual a resposta
if palpite > numero:
    print("Alto Demais!")
    print("Azar") #adicionado print caso palpite nao seja igual a resposta

#adicionado questionario para ver se o usuario conseguiu adivinhar
adivinhou = input("voce conseguiu adivinhar? (y/n)")

if adivinhou == 'y':
    print('Muito bem')
else:
    print("Deixa para lá")

