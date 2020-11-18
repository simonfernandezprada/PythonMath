V = [[30,34,20],
     [45,20,16],
     [14,26,25]]
T = [[35,30,26],
     [52,25,18],
     [23,24,32]]
A = [[0,0,0],
     [0,0,0],
     [0,0,0]]

print("""Una empresa que fabrica zapatos tiene 2 plantas, una en Valparaiso y la otra en Temuco.
Esta produce zapatos de color negro, blanco y café, tanto para niños, damas como caballeros.

La capacidad actual de producción mensual (en miles de pares) para las plantas de
Valparaiso y Temuco, respectivamente, estan dadas por las matrices V y T.

Para ambas matrices, segun el orden en que se mencionan, las filas corresponden al color del calzado y las columnas al tipo de persona que utilizara el calzado.

      nñ dm cb
V = [[30,34,20], Negro
     [45,20,16], Blanco
     [14,26,25]] Café

      nñ dm cb
T = [[35,30,26], Negro
     [52,25,18], Blanco
     [23,24,32]] Café

a) Determine la produccion mensual total de ambas plantas, representándola en una matriz A.
""")

for i in range (3):
    for j in range (3):
        A[i][j]=V[i][j]+T[i][j]
print (f"A = {A}\n")

print("\nb) Interprete el elemento a21.\n\na21 = 97 \nLa produccón total de zapatos blancos para niños es de 97mil pares\n")
print("\nc) Si para el proximo año se estima que la produccion en Valparaiso aumenta en un 30%, mientras que la de Temuco se reduce en un 10 %, represente la nueva produccion total en la matriz B.\n")

B = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range (3):
    for j in range (3):
        B[i][j]=round(1.3*V[i][j]+0.9*T[i][j],1)
print(f"B = {B}\n")
print("\nd) Interprete el elemento b13.\n\nb13 = 49,4 \nSe estima una producción total de 49,4 miles de zapatos negros para caballeros")
