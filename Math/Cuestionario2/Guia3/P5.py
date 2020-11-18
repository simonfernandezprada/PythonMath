print("La empresa Beta tiene dos plantas en Chile y en cada una de ellas fabrica tres productos. El número de unidades del producto i fabricados en la planta j en una semana está representado en la matriz C en el elemento C sub ij. ")

print("""
    PL1 PL2
C=[[120,70], Producto 1
   [150,110],Producto 2
   [80,160]] Producto 3
   """)

print("La empresa se expande, creando dos plantas en Ecuador que producen los mismos tres productos. \nLa produccion semanal de esta filial estará representada por una matriz E.")

print("\na) Si se sabe que los volúmenes de producción semanal de la filial en Ecuador son un 20 % menor que en Chile, entonces indique la operacion necesaria para calcular cada elemento de la matriz E utilizando notación matricial.\nE = 0,8C\nE = ")

C=[[120,70],
[150,110],
[80,160]]

E=[[0,0],
   [0,0],
   [0,0]]

for i in range(3):
  for j in range(2):
    E[i][j]=0.8*C[i][j]
  print(E[i])

print ("\nb) Si representamos la produccion semanal total de la empresa Beta, considerando ambas filiales, por la matriz T, escriba la expresion que calcula cada elemento de la matriz T usando notacion matricial.\nT = C + E")

print ("\nc) Calcule la matriz T")

T=[[0,0],
   [0,0],
   [0,0]]

for i in range(3):
  for j in range(2):
    T[i][j]=C[i][j]+E[i][j]
  print(T[i])

#T = C + E
#print (T)
