sequencia = list(input("sequencia: "))
num1 = int(sequencia[0])
letra = sequencia[1]
num2 = int(sequencia[2])

if num1 == num2:
    print(num1*num2)
elif letra.isupper():
    print(num2-num1)
elif letra.islower():
    print(num1+num2)

