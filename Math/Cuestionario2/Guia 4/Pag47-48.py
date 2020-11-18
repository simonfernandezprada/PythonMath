import numpy as np
print("""
Multiplicando matrices en Python
Tenemos dos maneras de multiplicar matrices usando Python. La mas sencilla es usando NumPy.

Ejemplo 1
A = [[4, 0],
     [1, 2],
     [7, 8]]
B = [[6, 3, 2, 9],
     [1, 5, 4, 8]]
""")

print("Notemos que A tiene orden 3x2 y B tiene orden 2x4, por lo que se puede multiplicar A·B\nLa matriz C resultante será de orden 3x4.")
# Usando NumPy, la multiplicacion es muy sencilla
# definimos ambas matrices como arrays de numpy
A = np.array([[4, 0],
              [1, 2],
              [7, 8]])
B = np.array([[6, 3, 2, 9],
              [1, 5, 4, 8]])
#listo!
C = A.dot(B)
print(C)
# el resultado es
# [[ 24 12 8 36]
# [ 8 13 10 25]
# [ 50 61 46 127]]
print("""
Otra manera es hacerlo con listas de listas
Ejemplo 1 bis""")
# declaramos las matrices A y B
A=[[4,0],
   [1,2],
   [7,8]]
B=[[6,3,2,9],
   [1,5,4,8]]
# declaramos la matriz C, que contendrá el resultado
C=[[0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]]
# hacemos dos ciclos for, el primero por las filas de C
# el segundo por las columnas de C
for i in range(3):
    for j in range(4):
        suma=0
        for k in range(2): # otro ciclo for, por las columnas de A
# o filas de B
# en el que combinamos los elementos correspondientes
            suma=suma + A[i][k]*B[k][j]
        C[i][j]=suma # asignamos la suma al elemento
    print(C[i])
