print("""Genere dos matrices:
Una matriz A de orden 5x7, con aij = i·j
Una matriz B de orden 7x5, con bij = 15i-2j

A = """)

A =  [[0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0]]

for i in range(5):
    fila = i+1
    for j in range(7):
        columna = j+1
        A[i][j] = fila * columna
    print(A[i])

print("\nB = ")
B = [[0,0,0,0,0],
     [0,0,0,0,0],
     [0,0,0,0,0],
     [0,0,0,0,0],
     [0,0,0,0,0],
     [0,0,0,0,0],
     [0,0,0,0,0]]

for i in range(7):
    fila = i+1
    for j in range(5):
        columna = j+1
        B[i][j] = fila*15-columna*2
    print(B[i])

print("\ny calcule la matriz C = A^T + 1/2B.\n\nC = ")

C = [[0,0,0,0,0],
     [0,0,0,0,0],
     [0,0,0,0,0],
     [0,0,0,0,0],
     [0,0,0,0,0],
     [0,0,0,0,0],
     [0,0,0,0,0]]

for i in range(7):
    for j in range(5):
        C[i][j]=A[j][i]+0.5*B[i][j]
    print(C[i])
