import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 24, 0.1) #comienzo de x, final de x, paso
y = -(1/6)*(x**2) + (4*x) + 10 #fórmula
plt.plot(x, y)
plt.axis([0, 24, 0, 40]) #comienzo de x, final de x, comienzo de y, final de y
plt.xlabel("Horas")
plt.ylabel("Temperatura en C Celsius")
plt.title("Modelo de la temperatura en la ciudad de Trinidad")
plt.grid(True)
plt.show()

print("""Un modelo de la temperatura en la ciudad de Trinidad, en Cuba, es

C(t) = - (1/6) t ** 2 + 4*t + 10

con t el tiempo despues de la medianoche en horas y C la temperatura en grados Celsius.
a) ¿Cual era la temperatura a las 5 p. m.? """)
T17 = - (1/6) * 17 ** 2 + 4*17 + 10
print(f"La temperatura a las 5pm alcanzó los {round(T17,1)} ºC")

print("""
b) ¿Cuanto aumentó o disminuyó la temperatura entre las 9 am y las 9 pm?
""")
T9 = - (1/6) * 9 ** 2 + 4*9 + 10
print(f"La temperatura a las 9am alcanzó los {round(T9,1)} ºC")
T21 = - (1/6) * 21 ** 2 + 4*21 + 10
print(f"La temperatura a las 9pm alcanzó los {round(T21,1)} ºC")
print("La temperatura disminuyó 12 ºC de 9am a 9pm")
