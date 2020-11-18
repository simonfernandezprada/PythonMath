import numpy as np

print("""La fabrica de bicicletas Expend produce dos modelos de bicicletas: M y N.
La matriz A nos indica las cantidades de acero y aluminio que requiere cada bicicleta,
expresadas en kg segun el modelo a producir, mientras que la matriz B nos entrega
un reporte de la cantidad de bicicletas producidas de ambos modelos para los dos
primeros meses del ano pasado.

      M  N
A = [[1, 2], Acero
     [3, 2]] Aluminio

      Ene  Feb
B = [[290, 312], M
     [345, 413]] N

a) Indique el orden de cada matriz.
A 2x2, B 2x2

b) Determine manualmente la matriz C = A·B
              Ene  Feb
        B = [[290, 312], M
             [345, 413]] N
      M  N
A = [[1, 2],
     [3, 2]]
""")

c11 = 1*290+2*345
c12 = 1*312+2*413
c21 = 3*290+2*345
c22 = 3*312+2*413
print(f"""
c11 = 1*290+2*345 = {c11}
c12 = 1*312+2*413 = {c12}
c21 = 3*290+2*345 = {c21}
c22 = 3*312+2*413 = {c22}
""")

print(f"""
c) Interprete los elementos c21 y c11.
c21 = se requieren {c21} kg de alumnio para la elaboración de la bici M en los 2 meses
c11 = se requieren {c11} kg de acero para la elaboración de la bici M en los 2 meses

""")

# Ahora con NumPy
A = np.array([[1, 2],
              [3, 2]])
B = np.array([[290, 312],
              [345, 413]])
C = A.dot(B)
print(C)
