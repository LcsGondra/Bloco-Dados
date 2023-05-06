#com biblioteca
import num2words
numero = int(input('insira um numero de 0 ate 99: '))
if(numero > 99):
    print('numero maior que 99, insira um numero de 0 ate 99 ')
elif(numero < 0):
    print('numero menor que 0, insira um numero de 0 ate 99 ')
else:
    to_ptbr = num2words.num2words(numero, lang='pt-br')
    print(f'numero em extenso: {to_ptbr}')

# sem biblioteca
numeros = {
    0: "zero", 1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco",
    6: "seis", 7: "sete", 8: "oito", 9: "nove", 10: "dez", 11: "onze",
    12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis",
    17: "dezessete", 18: "dezoito", 19: "dezenove", 20: "vinte", 30: "trinta",
    40: "quarenta", 50: "cinquenta", 60: "sessenta", 70: "setenta",
    80: "oitenta", 90: "noventa"
}

def n_extenso(n):
    if n <0 or n >99:
        return "Número inválido."
    if n in numeros:
        return numeros[n]
    else:
        dezenas = n - (n %10) 
        unidades = n %10 
        return numeros[dezenas] + ' e ' + numeros[unidades]
    
print(n_extenso(int(input('numero: '))))