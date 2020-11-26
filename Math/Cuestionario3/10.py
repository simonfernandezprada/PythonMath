import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,16,0.5)
f=(-4/3)*x**2+(71/3)*x
g=2*x**2-23*x+80

plt.xlabel("Tiempo (minutos)")
plt.ylabel("Temperatura (grados celsius)")

plt.plot(x,f,color="b")
plt.plot(x,g,color="g")
plt.axis([0,15,0,120])

plt.grid(True)
plt.annotate("f: Liquido A",xy=(3,110))
plt.annotate("g: Liquido B",xy=(9,25))
plt.show()

a = 10/3
b = -140/3
c = 80
if ((b**2)-4*a*c) < 0:
    print("La solución es con números complejos")
else:
    x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
    print(f"Las soluciones de la ecuación son:\n{x1}\n{x2}\n")
print("""
e) Determine e interprete las coordenadas del vertice de la parábola.
Vertice de la parábola = -b/2*a
""")
v=-b/2*a
print(f"El vértice de la parábola es decir el año con más trabajadores es el año ({v})")
y2 = -v**2+8*v
print(f"f({v}) = {y2}\n")
