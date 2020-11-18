import numpy as np

print("""Una fábrica para un mismo tipo de artículo eléctrico produce 2 modelos, A y B.
Las filas de la matriz M, en orden, nos muestran la cantidad de transistores y resistores
que se requieren por cada artículo, según cada modelo. Por otra parte, las filas de la
matriz Q nos reportan las cantidades producidas de cada modelo para las 3 primeras semanas
del mes pasado.

      mA mB
M = [[9, 14], Transistores
     [4, 5]]  Resistores

      1Sm  2Sm  3Sm
Q = [[200, 240, 220], Mod A
     [175, 210, 215]] Mod B
""")

M = np.array([[9, 14],
              [4, 5]])

Q = np.array([[200, 240, 220],
              [175, 210, 215]])

G = M.dot(Q)
print (f"G = {G}")
print(f"""
Ademas, considere las matrices G=M·Q y H=Q·M.
a) Indique el orden de M y Q.
M 2x2, Q 2x3

b) ¿Es posible calcular las matrices G y H? Justifique.
G, si ya que la columna de M y la fila de Q son iguales.
H, no ya que la columna de Q y la fila de M no son iguales.

c) Determine e interprete g23 y g12.
(Si decide calcular manualmente, no es necesario calcular toda la
matriz G para obtener los elementos que se indican)
g23, {G[1][2]} es la cantidad de Resistores que se requieren por cada artículo durante la 3ra semana.
g12, {G[0][1]} es la cantidad de Transistores que se requieren por cada artículo durante la 2da semana.
""")
