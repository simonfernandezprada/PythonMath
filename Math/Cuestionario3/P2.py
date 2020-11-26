import matplotlib.pyplot as plt
import numpy as np
x = np.arange(2, 12, 0.01)
# para cada elemento del dominio, aplicaremos la función
y = -45*x+550
# le pedimos a matplotlib que genere un gráfico
plt.plot(x, y)
# cuyos ejes van de 0 a 12 en la x, de 0 a 60 en la y
plt.axis([2, 12, 0, 465])
# con un título de eje x
plt.xlabel('Eje x')
# y un título de eje y
plt.ylabel('Eje y')
# y un titulo del gráfico
plt.title('Ejercicio 2')
# pedimos mostrar una grilla para facilitar la lectura
plt.grid(True)
# y que nos muestre el gráfico
plt.show()
