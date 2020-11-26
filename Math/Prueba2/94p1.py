import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,3.5,0.1)
f=29.4-9.8*x

plt.xlabel("Tiempo (segundos)")
plt.ylabel("Velocidad de la pelota (m/s)")

plt.plot(x  ,f,color="b")
plt.axis([0,3.5,0,30])

plt.grid(True)

plt.show()

print("""
La velocidad de una pelota lanzada hacia arriba, en m/s, mientras esta subiendo esta dada por la funcion
v (t) = 29,4 - 9,8 ·t, donde t es el tiempo medido en segundos desde fue lanzada.
a) Defina las variables dependiente e independiente, indicando unidad de medida.
b) Determine el dominio contextualizado de esta funcion. Considere que la pelota deja de subir cuando
esta se detiene.
c) Grafique la funcion v(t).
d) Determine e interprete v(1,1).
e) Si la pelota sube con una velocidad de 8,82 m/s, ¿cuantos segundos han transcurrido?
f) Interprete la pendiente de la funcion.""")
