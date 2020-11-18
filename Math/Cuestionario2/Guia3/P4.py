A = [ [71,80,75,90],
      [65,58,74,82] ]

D = [ [75,83,80,94],
      [67,60,78,85] ]

V = [ [0,0,0,0],
      [0,0,0,0] ]

print("""La matriz A muestra los pesos, en kilogramos, de cuatro hombres y cuatro mujeres
antes de fiestas patrias, mientras que la matriz D muestra sus pesos despues de dichas festividades

        1  2  3  4
A = [ [71,80,75,90],  Hombres
      [65,58,74,82] ] Mujeres

        1  2  3  4
D = [ [75,83,80,94],  Hombres
      [67,60,78,85] ] Mujeres

a) La matriz V nos entrega las variaciones de pesos para estas ocho personas.
¿Qué operación entre las matrices A y D debemos realizar para obtener V?
Restar D - A = V

b) Calcule la matriz V. """)

for i in range(2):
  for j in range(4):
    V[i][j]=D[i][j]-A[i][j]
  print(V[i])

print("\nc) ¿Cuánto fue el aumento de peso para la mujer 3 y el hombre 2? Responda usando notacion matricial")
print(f" Mujer 3, es decir v23, tuvo un aumento de {V[1][2]} kilos\nHombre 2, es decir v12, tuvo un aumento de {V[0][1]} kilos")

print("""
d) Interprete los elementos a21, d14 y v22.
a21 correspone al peso inicial de la mujer 1.
d14 correspone al peso final de el hombre 4.
v22 correspone al peso ganado por la mujer 26
""")
