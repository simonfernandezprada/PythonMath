import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

print("""De un mismo hogar han sido robados simultáneamente, una moto y un automóvil, los cuales
están siendo monitoreados por su propio dueño a través de dispositivos de rastreo GPS.
Al cabo de x minutos del robo, la moto se desplaza con una velocidad en km/h dada por la
función r(x). Mientras que, en ese mismo instante, el automóvil tiene una velocidad
también medida en km/h dada por la función s(x).""")

x=np.arange(-9,12,1)
s=-1.6*x**2+1.3*x+141.3
r=1.4*x**2-5.6*x+12.6

plt.xlabel("Tiempo en minutos (m)")
plt.ylabel("Velocidad en kilómetros por hora (km/h)")

plt.plot(x,s,color="b")
plt.plot(x,r,color="r")
plt.axis([-9,12,0,150])

plt.grid(True)
plt.show()

print("""
a) A partir de la igualdad entre ambas funciones, obtener una ecuación de la forma: a*x^2 + b*x + c = 0, que tenga relación con la intersección de las dos curvas cuadráticas.

a = 3
b = -6.9
c = -128.7
""")

a = 3
b = -6.9
c = -128.7

print("""b) Determine las 2 soluciones de la ecuación planteada anteriormente. Justifique sus resultados con desarrollo matemático o con un código Python. (2 puntos)""")

if ((b**2)-4*a*c) < 0:
    print("La solución es con números complejos")
else:
    x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
    print(f"Las soluciones de la ecuación son:\nx1 = {x1}\nx2 = {x2}")

print("""
c) Según el contexto del problema y la gráfica, indique el rango de tiempo para el cual la velocidad de la moto es menor a la velocidad del automóvil.

Desde el minuto -5,5 hasta el minuto 7,8 la moto es menor a la velocidad del automóvil, es decir, durante 13,3 minutos
""")
