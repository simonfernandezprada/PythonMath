#Considere la sucesion (g sub n) cuyo termino general es 5n**3. Implemente un codigo Python que muestre en pantalla
#
#a) Los primeros 4 terminos.
#b) Los 4 terminos que vienen inmediatamente despues del octavo termino.
#c) ¿El termino 40.000 pertenece a la sucesion? Verificarlo resolviendo una ecuacion en Python y usando bucles. ¿Cual es mas rapido?

n = 0
i = 0
s= []

for i in range(12):
    n=i+1
    s.append(5*n**3)
    if n==1:
        print('Los 4 primeros términos son: ')
    elif n==9:
        print('\nLos 4 términos inmediatamente después del octavo son: ')

    if n<5 or n>8:
        print(f's({n})={5*n**3}')
