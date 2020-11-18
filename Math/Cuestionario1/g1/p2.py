# Considere la sucesion (gn) cuyo termino general es 5n**3. Implemente un codigo Python que muestre en pantalla

# a) Los primeros 4 terminos
g = []
n = 0
for i in range (20):
    n=i+1
    g.append(5*n**3)
    if n < 5 or n > 8:  # b) Los 4 terminos que vienen inmediatamente despues del octavo termino
        print(f"g({n})={g[i]}")

# c) ¿El termino 40.000 pertenece a la sucesion? Verificarlo resolviendo una ecuacion en Python
from time import time
t1=time()
npoder3 = 40000/5
resultado = npoder3**(1/3)
resultado = round(resultado)
print(f"\nEl resultado de la ecuación 40000 = 5n^3 es igual a {resultado}")
t2=time()
print(f"\nEsta operación tomó {t2-t1} segundinis")

# Verificarlo usando bucles.
t3=time()
for i in range (20):
    n=i+1
    g.append(5*n**3)
    if 40000 == g[n]:
        print(f"\nSí, sí chavales, el 40000 pertenece a la sucessao y ocupa la posición g({n+1})")
t4=time()
print(f"\nEsta operación tomó {t4-t3} segundinis")
# ¿Cual es mas rapido?
print("\nFinalmente, comparando los tiempos, en este caso podemos decir que:")
if t2-t1 > t4-t3:
    print("Los buclecitos son el real flash. Le vuelan el OGT a la ecuación")
else:
    print("La ecuación es mucho más veloz que el bucle for")
