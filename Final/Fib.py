











































def FibonacciRecursivo(n):
    if n < 2:
        return n
    else:
        return FibonacciRecursivo(n - 1) + FibonacciRecursivo(n - 2)


def FibonacciDPUtil(n, tab):
    if n < 2:
        tab[0] = 0
        tab[1] = 1
    else:
        FibonacciDPUtil(n - 1, tab)
        tab[n] = tab[n - 1] + tab[n - 2]
            
def FibonacciDP(n):
    tab = [0] * (n + 1)    
    FibonacciDPUtil(n, tab)
    return tab[n]
FibonacciRecursivo(8)

FibonacciDP(8)



































import math

def f(d,p,C,S):
    if p <= 0:
        C[0] = 0
        return
    f(d,p-1,C,S)
    conteo = math.inf
    moneda = 0
    for di in d:
        if di <= p:
            if C[p-di] < conteo:
                conteo = C[p-di]
                moneda = di        
    C[p] = conteo + 1
    S[p] = moneda
        
def monedas(d, n):
    C = [-1] * (n + 1)
    S = [0] * (n + 1)
    f(d,n,C,S)
    return C, S



c, s = monedas([1, 5, 10, 20, 25, 50], monto)
print(c)
print(s)
contar = [0] * (monto + 1)
while monto > 0:
    print(s[monto],monto)
    contar[s[monto]] += 1
    monto -= s[monto]



for x in range(len(contar)):
    if contar[x] > 0:
        print("Hay " + str(contar[x]) + " monedas de " + str(x))




monto = 19
        
