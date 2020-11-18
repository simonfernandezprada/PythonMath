# Considere la sucesion (b sub n) de termino general (1 + 1/n)**n
# a) Usando todos los decimales que entrega Python, determine los terminos b10, b100, b1.000, b10.000, b100.000.
from math import e

n = 10
b = []
for i in range(5):
    b.append((1+1/n)**n)
    print(f'b({n})={b[i]}')
    if b[i] > e:
        print(f"Este número es mayor que el número e (2,71828)\n")
    else:
        print(f"Este número NO es mayor que el número e (2,71828)\n")
    n=n*10

# b) Despues de calcular los terminos anteriores, ¿que tipo de sucesion es (b sub n)?

# Es una sucesión monotona creciente

# c) ¿Algun termino es mayor que el numero de Eulere?
# No
