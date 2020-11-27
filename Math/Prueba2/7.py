from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,120,0.1)
f = -3*x**2+300*x+1
plt.plot(x,f,color="r")
plt.axis([0,120,0,10000])
plt.xlabel("Tiempo (1 hora)")
plt.ylabel("Número de visitas")
plt.title("Influencer")
plt.grid(True)
plt.show()
