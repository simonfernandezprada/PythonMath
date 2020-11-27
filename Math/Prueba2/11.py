import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

a = 2
b = -6.6
c = -14.4
if ((b**2)-4*a*c) < 0:
    print("La solución es con números complejos")
else:
    x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
    print(f"Las soluciones de la ecuación son:\nx1 = {x1}\nx2 = {x2}\n")
print("""
#e) Determine e interprete las coordenadas del vertice de la parábola.
#Vertice de la parábola = -b/2*a
""")
v=-b/2*a
print(f"El vértice de la parábola es ({v})")
