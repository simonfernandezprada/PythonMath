import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 12, 0.1) #comienzo de x, final de x, paso
y = 2.3 * x + 48
 #fórmula
plt.plot(x, y)
plt.axis([0, 12, 0, 100]) #comienzo de x, final de x, comienzo de y, final de y
plt.xlabel("Edad expresada en Meses") #nombre eje x
plt.ylabel("Altura promedio en (cm) Centímetros") #nombre eje y
plt.title("Altura del niño durante el primer año de vida") #Título gráfico
plt.grid(True)
plt.show()

print("""
La altura promedio en centimetros H(a) de un niño durante su primer año de vida,
se puede estimar mediante la función H(a) = 2.3*a + 48, donde a es la edad
expresada en meses.

a) Defina las variables dependiente e independiente, indicando unidad de
medida.
Independiente X Edad expresada en Meses (m)
Dependiente Y Altura promedio en Centímetros (cm)

b) ¿Cuál es el dominio contextualizado de la función?
DC = !R

c) Interpreta las coordenadas del punto E que aparece en el gráfico.
A los 9 meses, un niño mide 68.7cm promedio

d) Determina e interpreta H(0).
Un recién nacido mide 48cm promedio

e) ¿Es posible determinar a que edad los niños miden en promedio 60,65 cm?
Justifica.
60.65 = 2.3 * x + 48
60.65 - 48 = 2.3 * x
12.65 = 2.3 * x
12.65 / 2.3 = x
5.5 = x
A los 5 meses y medio los niños miden aproximadamente 60.65cm

f) ¿Es posible determinar a que edad los niños miden en promedio 80 cm?
Justifica.
No porque está fuera de rango

g) ¿Cuanto crecen, en promedio, los niños mensualmente hasta el primer año
de vida?
los niños crecen mensualmente 2.3 cm hasta el primer año, tal como se observa en el siguiente ciclo

""")
def f(x):
    f = 2.3 * x + 48
    return f
x = 0
salto = 1
while x <= 12:
    y=f(x)
    print(f"f({x})={round(y,2)}")
    x=x+salto
