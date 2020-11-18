from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,12.1,0.1)
f = 100 * x ** 2 - 1200 * x + 4000
plt.plot(x,f,color="r")
plt.axis([0,12,0,4000])
plt.xlabel("Tiempo (meses)")
plt.ylabel("Cantidad de Personas contagiadas")
plt.title("Propagación de un Virs Estival")
plt.grid(True)
plt.show()
print("""La propagacion de un virus estival se modela por la funcion

f(x) = 100 * x ** 2 - 1200*x + 4000

donde f(x) indica el numero de contagiados y x es el tiempo transcurrido, en
meses, desde el inicio hasta el final de un año.

a) Realice la grafica de esta funcion, indicando en cada eje el nombre de la
variable que corresponde, junto con su unidad de medida.

b) Observando dicha grafica, estime el tiempo transcurrido para que haya 2.000
contagiados. Marque y escriba las coordenadas de los puntos en el grafico.
2 dias

c) ¿Cuando habra 2.900 contagiados?""")

a = 100
b = -1200
c = 1100
if ((b**2)-4*a*c) < 0:
    print("La solución es con números complejos")
else:
    x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
    print(f"Las soluciones de la ecuación son:\n{x1}\n{x2}\nHabrán 2900 contagiados los meses {x1} y {x2}")
print("\nd) Marque y escriba en el grafico las coordenadas del vertice de la parabola.")

v=-b/2*a
print(f"El vértice de la parábola es decir el mes con menos contagiados es m({v})")


print("""\ne) ¿Cuando se observa la menor cantidad de contagiados? Indique cantidad de contagiados.
El mes 6

f) ¿Cuando se observa la mayor cantidad de contagiados?
El fin del mes 12 y el comienzo del mes 1
""")
