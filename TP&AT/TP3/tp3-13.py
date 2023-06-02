A = float(input('valor1: '))
B = float(input('valor2: '))
C = float(input('valor3: '))
if A >= B >= C:
    if (A + B > C) and (A + C > B) and (B + C >A):
        print(f"Forma un triangulo. Perimetro: {A+B+C}")
    else:
        print(f"Trapezio. Area: {((A+B)/2)*C}")