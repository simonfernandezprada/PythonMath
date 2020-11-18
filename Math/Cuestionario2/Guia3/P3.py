print(" a) Indique el orden de cada matriz.\n\nEl orden es 3x4")

print("\n b) Calcule la matriz S = A+B \n")
A=[ [2.6,4.8,1.8,0.9],
    [3.2,4.4,2.5,2.8],
    [2.4,3.6,3.8,2.5] ]

B=[ [3.6,2.5,3.0,2.5],
    [4.5,5.0,3.5,3.8],
    [2.9,3.0,4.6,4.0] ]

S= [ [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0] ]

for i in range(3):
  for j in range(4):
    S[i][j]=round(A[i][j]+B[i][j],1)
  print(S[i])


print("\n c) Indique e interprete el valor de los elementos s24 y d24.\n")

A=[ [2.6,4.8,1.8,0.9],
    [3.2,4.4,2.5,2.8],
    [2.4,3.6,3.8,2.5] ]

B=[ [3.6,2.5,3.0,2.5],
    [4.5,5.0,3.5,3.8],
    [2.9,3.0,4.6,4.0] ]

S= [ [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0] ]

for i in range(3):
  for j in range(4):
    S[i][j]=round(B[i][j]-A[i][j],2)
  print(S[i])

print("""
s24 = 6.6 y d24 = 1.0.
s24 = venta total del producto 2 de la región 4
d24 = la diferencia de ventas del producto 2 de la región 4\n """)

print(" \n e) Para el tercer añoo de funcionamiento, los tres productos ahora estan disponibles en seis regiones. Durante este año, las ventas de esta empresa estaran registradas en una matriz E. ¿Es posible determinar la matriz T = A + B + E ? Justifique su respuesta.")
print(" \nNo porque si bien siguen siendo 3 productos, ahora son 6 regiones lo que cambioa el orden y no nos permite calcular")
