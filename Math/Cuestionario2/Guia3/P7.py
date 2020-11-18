print("Genere una matriz M de orden 8x9 donde cada término esté definido por\nmij = 8i+12j y calcule su transpuesta.\n")


M=[[0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0]]

for i in range(8): #Cantidad de filas
    fila=i+1 #Inicia en 1 y no 0
    for j in range(9): #Cantidad de columnas
        columna=j+1 #Inicia en 1 y no 0
        M[i][j]=8*fila+12*columna #Calcula mij = 8i+12j para cada valor
    print(M[i])

print("\n")

Mt=[[0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]]

for i in range(9): #Para las filas
  for j in range(8): #Para las columnas
    Mt[i][j]=M[j][i] #Transpone o da vuelta
  print(Mt[i])
