import numpy as np

A = np.array([[1, 2, 3],
[4, 5, 6]])

B = np.array([[11, 12, 13],
[14, 15, 16]])

print(A.shape) # Muestra el orden (2, 3), dos filas, tres columnas

# suma
C = A + B
print(f"\nC = \n{C}")
# [[12 14 16]
# [18 20 22]]

# resta
D = B - A
print(f"\nD = \n{D}")
# [[10 10 10]
# [10 10 10]]

# ponderación por escalar
E = 2*A
print(f"\nE = \n{E}")
# [[ 2 4 6]
# [ 8 10 12]]

# transposicion
F = A.T
# o también A.transpose()
print(f"\nF = \n{F}")
# [[1 4]
# [2 5]
# [3 6]]
