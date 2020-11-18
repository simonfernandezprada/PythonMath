import matplotlib.pyplot as plt
import numpy as np
# definimos el rango de x
x = np.arange(-1,6,0.01)
# definimos la funcion

f= -x**2+4*x+5
plt.plot(x, f)

plt.annotate("$f(x)=-x^2+4x+5$", xy=(3.5,8))
# definimos la posici´on de los ejes
ax = plt.gca()
# estos ejes cruzan por el origen
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
# estos ejes quedan invisibles
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
# normalmente, PyPlot dibuja los ejes en el borde de la caja
# pero eso no es como usamos los gr´aficos normalmenet
plt.grid(False)
plt.show()
