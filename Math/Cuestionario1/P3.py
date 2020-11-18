
# Considere la sucesion (kn) definida por su termino general (-1)**n
# a) Los primeros 20 términos.

b=[]
for i in range (20):
    n=i+1
    b.append((-1)**n)
    print (f'b({n})={b[i]}')

# b) ¿Que se puede afirmar acerca de los términos de esta sucesión?

# Qué son detonados?

# c) ¿Cual es el término que ocupa la posición 2.020?
x = ((-1)**2020)
print(f'El término que ocupa la posición 2.020 es {x}')
