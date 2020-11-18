import numpy as np

V = [[1300, 900, 800],
    [2100, 1700, 1500],
    [1500, 1200, 900]]

P =  [3600, 900, 1500]

print("""Una pequena cadena tiene restaurantes de comida rápida en Santiago,
Concepción y Antofagasta, en los que vende hamburguesa, completos y malteada.
En un fin de semana, las cantidades de cada comida segun cada sucursal se
distribuyeron de acuerdo con la matriz V, donde las filas corresponden a los
productos y las columnas a las sucursales, mientras que los precios, en pesos,
de cada producto estan expresados en la matriz P.

                       Stgo  Cnce  Antfg
                   V = [[1300, 900, 800],  Anvorguesas
                       [2100, 1700, 1500], Tocomples
                       [1500, 1200, 900]]  Maltitas

     Hmbrg  Cmpl  Mlts
P =  [3600, 900, 1500] Precios

Si I = P·V
a) Indique el orden de las matrices P, V e I.
P 1x3, V 3x3, I 1x3
""")

i11 = 3600*1300+900*2100+1500*1500
i12 = 3600*900+900*1700+1500*1200
i13 = 3600*800+900*1500+1500*900
v32 = V[2][1]

print(f"""b) Determine manualmente la matriz I.
i11 = 3600*1300+900*2100+1500*1500 = {i11}
i12 = 3600*900+900*1700+1500*1200  = {i12}
i13 = 3600*800+900*1500+1500*900   = {i13}

I = [{i11}, {i12}, {i13}]

c) Interprete los elementos v32, p12 e i13.
v32 = {v32} es la cantidad de Maltitas en Conce
p12 = {P[1]} es el precio de los tocomples
i13 = {i13} es la venta total de los productos en Antofapasti
""")

V = np.array([[1300, 900, 800],
              [2100, 1700, 1500],
              [1500, 1200, 900]])

P = np.array([3600, 900, 1500])

I = P.dot(V)
print(I)
