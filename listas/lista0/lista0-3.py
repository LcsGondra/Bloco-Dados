lista_primos = []
int = int(input('insira o numero para ver a quantidade de primos que existem menores q ele: '))
def check_primo(primo):
    for j in range(2, primo):
        if(primo % j == 0):
            return
    lista_primos.append(primo)

for i in range(1, int):
    check_primo(int)

print(lista_primos)