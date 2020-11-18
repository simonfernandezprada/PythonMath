import matplotlib.pyplot as plt
import numpy as np

# generaremos una tabla de datos usando numpy
# a la que aplicaremos la función, que es la misma del ejemplo
# tomaremos la variable independiente entre 0 y 6
# y haremos los elementos de la tabla separados en 0,01
x = np.arange(0, 6, 0.01)

# para cada elemento del dominio, aplicaremos la función
y = 120*x+2000

# le pedimos a matplotlib que genere un gráfico
plt.plot(x, y)

# cuyos ejes van de 0 a 6 en la x, de 0 a 2800 en la y
plt.axis([0, 6, 0, 2800])

# con un título de eje x
plt.xlabel('Energía utilizada ({kWh})')

# y un título de eje y
plt.ylabel('Costo para usuario ($)')

# y un titulo del gráfico
plt.title('Costo para el usuario según uso de energía')

# pedimos mostrar una grilla para facilitar la lectura
plt.grid(True)

# y que nos muestre el gráfico
plt.show()
