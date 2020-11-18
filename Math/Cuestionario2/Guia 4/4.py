#creando la matriz de ceros
T=[]
for i in range(4):
    T.append([0]*5)

#creando la matriz T
for i in range(4):
    for j in range(5):
        fila=i+1
        columna=j+1
        T[i][j]=100*fila*columna
print(T[i])

#Creando la matriz de ceros
C=[]
for i in range(5):
    C.append([0]*6)

#Creando la matriz C
for i in range(5):
  for j in range(6):
    fila=i+1
    columna=j+1
    C[i][j]=3*fila*+5*columna
  print(C[i])
