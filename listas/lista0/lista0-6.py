def factorial():
    n = int(input("fatorial de: "))
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact
    
def joanizacao(fact):
    fact_j = str(fact).replace('0','')
    print(fact_j[-1])

joanizacao(factorial())