# Considera la sucesion (5, 10, 15, 20, 25, 30,...).
# a) Comparando con el ejemplo 1 de esta guıa, ¿que caracteriza a estos números?
# Que avanza de 5 en 5 y por eso podemos escribirlo como 5n. Es mono creciente.

# b) Determine la expresion algebraica del termino generico de lugar n.
# 5n

# c) Compruebe si su expresion es correcta usando codigo Python

b = []
for i in range (6):
    n=i+1
    b.append(5*n)
    print(f'b({n})={b[i]}')
