import numpy as np

print("La matriz T =")
T = [[0,0,0],
     [0,0,0]]

for i in range(2):
    f = i+1
    for j in range(3):
        c = j+1
        T[i][j] = 90*f*c
    print(T[i])

print("\nLa matriz U =")
U = [[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]

for i in range(3):
    f = i+1
    for j in range(4):
        c = j+1
        U[i][j] = 3*f+2*c
    print(U[i])

print("\nLa matriz D =")

T = np.array([[90,180,270],
             [180,360,540]])

U = np.array([[5,7,9,11],
            [8,10,12,14],
            [11,13,15,17]])

D = []
D = T.dot(U)
print(D)

print ("""
d14 equivale a 8100. Esto quiere decir que almacenar las unidades producidas en la planta 1 durante el mes de abril cuesta USD$8100.- """)
