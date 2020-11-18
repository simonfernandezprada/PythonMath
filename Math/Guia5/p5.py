import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 1000, 0.01) #comienzo de x, final de x, paso
y = 1 - (300 / (300 + x )) ** 3
plt.plot(x, y)
plt.axis([0, 1000, 0, 1]) #comienzo de x, final de x, comienzo de y, final de y
plt.xlabel("Número de días")
plt.ylabel("Individuos dados de alta")
plt.title("Proporción dados de alta al final de t días de hospitalizacion")
plt.grid(True)
plt.show()



print("""
Una compañía de seguros examinó el registro de un grupo de individuos hospitalizados
por una enfermedad en particular. Se encontró que la proporción total de quienes
habían sido dados de alta al final de t días de hospitalizacion, está dada por la
función p(t), donde

p(t) = 1 - (300 / 300 + t ) ** 3

a) ¿Que cantidad de individuos han sido dados de alta al comienzo, t = 0, de la
hospitalización?
0 Individuos

b) ¿Cuál es el porcentaje de individuos que han sido dados de alta al final del día 100?
1 - (300 / 300 + 100) ** 3
1 - (300 / 400) ** 3
1 - 0.75 ** 3
1 - 0.421875
0.8578125 individuos han sido dados de alta al final del día 100
""")
