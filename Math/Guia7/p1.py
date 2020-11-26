from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
# definimos el rango de x
x = np.arange(0, 8, 0.01)
# definimos la funcion
f = -x**2+8*x
plt.plot(x, f)
plt.xlabel("Tiempo en años (a)")
plt.ylabel("Cantidad de trabajadores (u)")
plt.title("Historia de un fracaso")
ax = plt.gca()
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.grid(False)
plt.show()

print("""La propagación de un virus computacional durante los primeros 6 días se modela con la función
f(t) = -t**2 + 8t , donde f(t) indica el numero de computadores infectados (en miles) y t el tiempo transcurrido, en días, desde que se propagó el virus.

a) Defina la variable dependiente e independiente, indicando unidad de medida.
Y, dependiente, Computadores infectados en miles.
X, Independiente, Tiempo en días.

b) Escriba el dominio contextualizado de la función.
dc = {0,6}

c) ¿Cuántos pc habrán contagiados al finalizar el sexto día?""")
x = 6
y = -x**2+8*x
print(f"f(6) = {y}\nAl finalizar el sexto día habrán {y*1000} pc contagiados")
print("""d) ¿Cuándo habrán 15 mil computadores infectados?")

15 = -x**2+8*x
0 = -x**2 +8*x -15
a = -1, b = 8, c = -15 """)
a = -1
b = 8
c = -15
if ((b**2)-4*a*c) < 0:
    print("La solución es con números complejos")
else:
    x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
    print(f"Las soluciones de la ecuación son:\n{x1}\n{x2}\nHabrán 15mil pc infectados los días {x1} y {x2}")
print("""
e) Determine e interprete las coordenadas del vertice de la parábola.
Vertice de la parábola = -b/2*a
""")
v=-b/2*a
print(f"El vértice de la parábola es decir el día con más infectados es d({v})")
y2 = -v**2+8*v
print(f"f({v}) = {y2}\nAl finalizar el día {v} habrán {y2*1000} pc contagiados")
