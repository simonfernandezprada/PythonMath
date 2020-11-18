print("""Supongamos que queremos transponer la matriz
A = [[3, 8],
     [5, 1],
     [2, 6]]

Si lo hacemos a mano, el resultado es
A^T =  [[3, 5, 2 ],
        [8, 1, 6]]

¿Pero en Python? Muy sencillo.
A = [[3, 8],
     [5, 1],
     [2, 6]]

At = [[0, 0, 0],
      [0, 0, 0]]

Iteramos por las filas de la transpuesta
for i in range(len(At)):

Y ahora por las columnas de la transpuesta
for j in range(len(At[0])):

Escribimos los índices al revés
At[i][j] = A[j][i]
print(At)
y obtendremos [[3, 5, 2], [8, 1, 6]]
""")
