from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,16,0.5)
f = ( -4 / 3 ) * x ** 2 + ( 71 / 3 ) * x
g = 2 * x ** 2 - 23 * x + 80
plt.plot(x,f,color="r")
plt.plot(x,g,color="b")
plt.axis([0,15,0,120])
plt.xlabel("Tiempo de Experimentación (m')")
plt.ylabel("Temperatura en grados Celcius (cº)")
plt.title("")
plt.grid(True)
plt.annotate("f(x)=temp. sustancia A",xy=(3,110))
plt.annotate("g(x)=temp. sustancia B",xy=(9,25))
plt.show()
