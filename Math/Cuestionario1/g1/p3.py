# Sea la sucesion (k sub n) definida por su termino general (-1)^n.
# a) Determine los primeros 20 terminos.
k = []
n = 0
for i in range (20):
    n=1+i
    k.append((-1)**n)
    print(f"k({n})={k[i]}")
# b) ¿Que se puede afirmar acerca de los terminos de esta sucesion?
print("\n¿Que se puede afirmar acerca de los terminos de esta sucesion?")
print("1) Que es no monótona.\n2) Que la posición impar es negativa y la par es positiva. \n3) El resultado absoluto siempre es 1 ")
# c) ¿Cual es el termino que ocupa la posicion 2.020?
print(f"\nEl termino que ocupa la posicion 2.020 es: \nk(2020)={(-1)**2020}")
