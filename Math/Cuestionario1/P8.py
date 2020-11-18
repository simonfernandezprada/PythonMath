# Considera la sucesion (7, 14, 21, 28, 35, 42,...).
# a) Al mirar los terminos de esta sucesi on, ¿que puede decir de ellos?
# Que son múltiplos de 7 mono crecientes

# b) Determine la expresion algebraica del termino generico de lugar n.
# 7n

# c) Compruebe si su expresion es correcta usando codigo Python.
b = []
for i in range(6):
    n=i+1
    b.append(7*n)
    print(f'b({n})={b[i]}')
