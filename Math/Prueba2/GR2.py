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


print("""El costo de arriendo de una casa comenzo en $350.000, acordando un incremento de $26.000 anualmente.
Si el contrato de arriendo duro 10 años
a) Determine la forma algebraica de funcion que determina el costo del arriendo, en miles de pesos,
despues de transcurridos x años desde que se inicia el contrato.
b) Defina la variable dependiente e independiente, indicando unidad de medida.
c) Determine el dominio contextualizado de la funcion.
d) ¿Cual fue el costo de arriendo al cabo de 5 años?
e) Interprete el valor de la pendiente de la funcion.
f) ¿Despues de cuantos años el costo de arriendo de la casa fue de $532.000?""")
