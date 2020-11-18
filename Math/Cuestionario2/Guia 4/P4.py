print("""Una companía, que fabrica un determinado producto, tiene 4 plantas de producción
y 5 bodegas de almacenamiento. La matriz T = (tij) nos indica las unidades de este
producto que se generan mensualmente en la planta i, y que son transportadas a la
bodega j para quedar almacenadas ahí durante ese mes que fueron producidas.
Ademas, tenemos la matriz C = (cij) que nos detalla para el primer semestre del
presente ano el costo en dólares de almacenar una unidad del producto durante el
mes j en la bodega i.
""")

print("""
Si estas matrices T y C estan definidas respectivamente por las expresiones
tij = 100ij 1 <= i <= 4 y 1 <= j <= 5
cij = 3i+5j 1 <= i <= 5 y 1 <= j <= 6

entonces
a) Indique el orden de cada matriz y analice si es posible realizar C·T. Justifique.
T 4x5 y C 5x6. No es posible ya que la columna de C no es igual a la fila de T.

b) Determine todos los elementos que componen cada matriz.
""")

print('matriz T')

#iniciando T como una matriz de ceros de orden 4x5
T=[]
for i in range(4):
  T.append([0]*5)

#recalculando todos los elementos de la matriz T
for i in range(4):
  for j in range(5):
    fila=i+1
    columna=j+1
    T[i][j]=100*fila*columna
  print(T[i]) #imprimiendo cada fila de la matriz T

#iniciando C como una matriz de ceros de orden 5x6

print('matriz C')
C=[]
for i in range(5):
  C.append([0]*6)

#recalculando todos los elementos de la matriz C
for i in range(5):
  for j in range(6):
    fila=i+1
    columna=j+1
    C[i][j]=3*fila+5*columna
  print(C[i]) #imprimiendo cada fila de la matriz C


print("c) Determine la matriz G = T·C.")

print('matriz G')
#iniciando la matriz G de orden 4x6
G=[]
for i in range(4):
  G.append([0]*6)

#calculando G, las matrices T y C ya están en memoria
for i in range(4):
  for j in range(6):
    suma=0
    for k in range(5): #T tiene 5 columnas y C tiene 5 filas
      suma=suma + T[i][k]*C[k][j]
    G[i][j]=suma
  print(G[i]) #imprimiendo en pantalla las filas de la matriz G

print("""
d) Interprete los elementos t14, c52 y g35.
t14: Mensualmente 400 unidades de este producto son transportadas desde la planta 1 a la bodega 4.
c52: Durante el fes de febrero, almacenar 1 unidad de este producto en la bodega 5 tiene un costo de 25 dólares.
g35: Durante el mes de mayo, por almacenar en bodegas la producción mensual de la planta 3 la empresa tuvo que invertir un total de 162.000 dólares.

e) ¿Cuánto cuesta almacenar una unidad en la bodega 4 durante marzo de este año?
respuesta: cuesta 37 dólares.

f) ¿A cuanto asciende el total de dinero que gasta esta empresa por almacenar
la produccion mensual de la planta 2 durante el mes de abril?
respuesta: en total esta empresa debe gastar 93.000 dólares por almacenar la producción de la planta 2 en el mes de abril.
""")
