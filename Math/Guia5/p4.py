import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 6, 0.1) #comienzo de x, final de x, paso
y = 1600*0.25**x
plt.plot(x, y)
plt.axis([0, 6, 0, 1600]) #comienzo de x, final de x, comienzo de y, final de y
plt.xlabel("Tiempo transcurrido en meses (m)")
plt.ylabel("Sustancia radioactiva en gramos (gr)")
plt.title("Desintegración de Sustancia Radiactiva vs Tiempo")
plt.grid(True)
plt.show()

print("""
Una sustancia radiactiva se desintegra a medida que transcurre el tiempo. Esta
situacion se representa por la funcion exponencial R(x) = 1600 * 0,25 ** x donde
R(x) corresponde a la cantidad de sustancia radioactiva, en gramos, y la variable
x al tiempo transcurrido, en meses.

a) ¿Que títulos deberían tener los ejes?
Eje Horizontal x Tiempo transcurrido en meses (m)
Eje Vertical y Sustancia radioactiva en gramos (gr)

b) Interprete las coordenadas del punto A dado en el grafico.
En 2 meses se han desintegrado 1500gr de la sustancia radiactiva

c) Determine e interprete R(5).
R5 = 1.600 * 0,25 ** 5
""")
R5 = 1.600 * 0,25 ** 5
print(f"R5 = {R5}")

print("""
d) Si R(x) = 400, observado el grafico, estime el valor de x e interprete.
En 1 mes se han desintegrado 800gr de Sustancia Radiactiva

e) Escriba dominio contextualizado de la funcion
DC = !R
""")
