C = [[300, 95],
    [250, 100],
    [200, 100]]

I = [[190, 90],
    [200, 100],
    [150, 80]]

T = [[0, 0],
     [0, 0],
     [0, 0]]

D = [[0, 0],
     [0, 0],
     [0, 0]]

print("""Una empresa de motocicletas dispone de dos plantas de fabricacion,
una en China y la otra en Indonesia, en las que fabrica dos modelos de motos
M1 y M2 en tres colores, rojo, verde y azul. Su capacidad de produccion diaria,
en cada planta, está representada por las matrices C (para China) e I (para Indonesia).

      M1   M2
C = [[300, 95], Rojo
    [250, 100], Verde
    [200, 100]] Azul

      M1   M2
I = [[190, 90], Rojo
    [200, 100], Verde
    [150, 80]]  Azul

a) Indique el orden de cada matriz.
C 3x2, I 3x2

b) Interprete los elementos c21 e i32.
c21 = La producción de M1, color verde, en la planta China asciende a 250 motos diarias.
i32 = La producción de M2, color azul, en la planta Indonesia asciende a 80 motos diarias.

c) Determine la matriz T = C + I.
Matriz T =""")
for i in range(3):
    for j in range(2):
        T[i][j] = C[i][j]+I[i][j]
    print(T[i])

print("""
d) Interprete los elementos t31 y t12.
t31 = 350, La producción diaria total entre las 2 plantas de la moto M1, color Azul.
t12 = 185, La producción diaria total entre las 2 plantas de la moto M2, color Rojo.

e) Determine la matriz D = C - I.
Matriz D =""")
for i in range(3):
    for j in range(2):
        D[i][j] = C[i][j]-I[i][j]
    print(D[i])


print("""
f) Interprete d22 y d11.
d22 = La producción extra total diaria China de la moto M2, color Verde
d11 = La producción extra total diaria China de la moto M1, color Rojo
""")
