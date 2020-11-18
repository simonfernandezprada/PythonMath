import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,100,10)
g = 3800*x + 24000
a = 4000*x + 18000

plt.plot(x,g,color='b')
plt.plot(x,a,color='g')

plt.axis([0,70,0,400000])
plt.xlabel('Cantidad de agendas')
plt.ylabel('Valor a pagar')
plt.title('Comparacion de costos según imprenta')

plt.grid(True)
plt.show()
