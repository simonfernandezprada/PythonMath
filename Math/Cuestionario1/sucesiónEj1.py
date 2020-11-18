#Considere la sucesion (3n2 +7). Por medio de un codigo Python con ciclos for
#despliegue en pantalla Potencias en Python
#
#a) Los primeros 5 terminos.
#b) Los 5 terminos que vienen inmediatamente despues del decimoquinto termino.

n = 0
i = 0
s= []

for i in range(20):
    n=i+1
    s.append(3*n**2+7)
    if n==1:
        print('Los cinco primeros términos son: ')
    elif n==16:
        print('\nLos cinco términos inmediatamente después del décimo quinto son: ')
    if n<6 or n>15:
        print(f's({n})={s[i]}')
