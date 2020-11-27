import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-10,15,1)
f=-1.6*x**2+1.3*x+141.3
g=1.4*x**2-5.6*x+12.6

plt.plot(x,f,color='b')
plt.plot(x,g,color='g')

plt.axis([-10,15,-30,200])
plt.xlabel('tiempo en minutos')
plt.ylabel('desplazamiento / velocidad')
plt.title('')



plt.grid(True)
plt.show()
