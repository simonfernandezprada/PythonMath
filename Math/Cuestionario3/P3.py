import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 12, 0.01)
# para cada elemento del dominio, aplicaremos la función
y = 2/3*x+48
# le pedimos a matplotlib que genere un gráfico
plt.plot(x, y)
# cuyos ejes van de 0 a 12 en la x, de 0 a 60 en la y
plt.axis([0, 12, 0, 60])
# con un título de eje x
plt.xlabel('Meses (m)')
# y un título de eje y
plt.ylabel('Altura en Centímetros (cm)')
# y un titulo del gráfico
plt.title('Crecimiento del niño durante su primer año de vida')
# pedimos mostrar una grilla para facilitar la lectura
plt.grid(True)
# y que nos muestre el gráfico
plt.show()

print("""
RECUERDA SIEMPRE:
La y depende de la x
X = Independiente
Y = Dependiente

a) Defina la variable dependiente e independiente, indicando unidad de medida.
Independiente = Meses (m) del primer año
Dependiente = Atura (cm)

b) Escriba el dominio de la funcion y el dominio contextualizado.
El dominio de refiere a la variable X, la independiente.
Dom  f(x) = !R
Dom Context = {0, 12}

c) Determine e interprete f(6) y f(8).
f(6) = 2/3*6+48""")
f6 = 2/3*6+48
print(f"f(6) = {f6} Un niño a los 6 meses de vida mide {f6}cm")
print("f(8) = 2/3*8+48")
f8 = 2/3*8+48
print(f"f(8) = {round(f8,2)} Un niño a los 8 meses de vida mide {round(f8,2)}cm")
print("""
d) Si un niño mide 50 cm, ¿cuantos meses de vida tiene?
50 = 2/3*x+48
2 = 2/3*x
x = 2 / (2/3)
x = 3 Un niño de 50 cm tiene 3 meses.

e) ¿Es posible calcular la edad de un niño si su estatura es de 68 cm?
68 = 2/3*x+48
20 = 2/3*x
x = 20 / (2/3)
x = 30
No es posible de calcular ya que el dominio va de 0 a 12 y 30 queda fuera de eso.
""")
