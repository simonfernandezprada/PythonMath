import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 12, 0.1)
y = (500*x)/(x+12)
plt.plot(x, y)
plt.axis([0, 12, 0, 500])
plt.xlabel("Edad del niño en años")
plt.ylabel("Dosis en mg de medicamento")
plt.title("Regla de Young")
plt.grid(True)
plt.show()

print("""a) Defina la variable dependiente e independiente, indicando unidad de medida.
Independiente: x, La edad del niño en años
Dependiente: y, La dosis en mg de medicamento

b) Escriba el dominio de la funcion y dominio contextualizado.
D = !R - {-12}
DC = {0, 12}

c) ¿Es correcto administrar 512 mg de paracetamol a un nino de 10,5 anos?
No, ya que el máximo en dosis a adulto es 500.

d) Determine e interprete f(7).
f(7) = la cantidad en mg de medicamento que debe recibir un niño de 7 años
y = 500*7/7+12
y = 3500/19
y = 184.21
A un niño de 7 años le corresponden 184.21 de paracetamol

e) ¿Cuanto medicamento se le debe administrar a un niño de 2 años con 6 meses?
y = 500*2.5/2.5+12
y = 1250 / 14.5
y = 86.21
A un niño de 2,5 años le corresponden 86.21 de paracetamol

f) Si a un niño se le administra 180 mg de paracetamol, ¿cual es su edad?
180 = 500 * x / x + 12
180 * (x + 12) = 500 * x
180x + 2160 = 500x
2160 = 320x
6.75 = x
Su edad es 6 años y 9 meses
""")

def f(x):
    f=(500*x)/(x+12)
    return f

x=1
salto=1
while x <= 12:
    y=f(x)
    print(f"f({x})={round(y,2)}")
    x=x+salto
