# Considere la sucesion (3n**2+7). Por medio de un codigo Python con ciclos for despliegue en pantalla
# a) Los primeros 5 terminos.

b = []
n = 0
for i in range(20):
    n=i+1
    b.append(3*n**2+7)
    if n < 6:
        print(f"b({n})={b[i]}")
# b) Los 5 terminos que vienen inmediatamente despues del decimoquinto termino

    if n > 15:
        print(f"b({n})={b[i]}")
