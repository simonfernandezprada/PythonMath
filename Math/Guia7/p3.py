import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

x=np.arange(0,181,1) #definimos los valores de x con un salto de 0,1 y va desde 0 a 12
y=x**2-180*x+20000    #forma algebraica

#titulos
plt.title("Costo en madera por cada casa prefabricada")
plt.xlabel("Cantidad de casas prefabricadas(unidades)")
plt.ylabel("Costo de la madera")

plt.plot(x,y,color="b")  #color azul de la linea de la curva
plt.axis([0,180,10000,20000])   #el valor de los ejes x e y respectivamente

plt.grid(True)   #grilla
plt.show()

print("""
Para la construccion de casas prefabricadas, el costo de la madera (en cientos de
pesos, por casa) esta dado por la funcion
C(x) = x ** 2 - 180 * x + 20000 donde x
corresponde a la cantidad de casas prefabricadas.

a) Realice el grafico de esta funcion. Indicando en cada eje el nombre de la
variable correspondiente junto con la unidad de medida.

b) Determine los valores de x que permiten que C(x) = 14.400 e interprete estos dos puntos.""")
a=1
b=-180
c=5600
if ((b**2)-4*a*c) < 0:
    print("La solución es con números complejos")
else:
    x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
    print(f"Las soluciones de la ecuación son:\n{x1}\n{x2}\nEl costo de la madera será 14.400 cuando se hayan construido {x1} y {x2} casitas")

print("c) Determine e interprete las coordenadas del vertice de esta funcion cuadratica.")
v=-b/2*a
print(f"\nEl vértice de la parábola, es decir el costo más bajo de la madera es a las ({v}) unidades")

print("\nd) Verifique graficamente los resultados obtenidos en b) y en c).")
