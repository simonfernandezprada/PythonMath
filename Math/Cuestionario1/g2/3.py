print('''Sean (Sn) y (Tn) las sucesiones de los multiplos de 6 y 13, respectivamente. Se pide

a) Escribir la expresion algebraica del termino de lugar n para cada sucesion.
b) Calcular las siguientes sumas, usando Python pero sin necesidad de listas.
    i. La suma de los terminos de (Sn) desde el de posicion 35 hasta el de posicion 61, inclusive.
    ii.La suma de los terminos de (Tn) desde el de posicion 15 hasta el de posicion 36, inclusive.
''')
print(f"a) S(n)=6n\n   T(n)=13n")
suma=0
for i in range (35,62):
    a=6*i
    suma=suma+a
cuma=0
for j in range (15,37):
    b=13*i
    cuma=cuma+b
print (f"b) La suma de los términos de (Sn) desde el de posición 35 hasta el de posición 61 es {suma}\n   La suma de los terminos de (Tn) desde el de posicion 15 hasta el de posicion 36 es {cuma}.")
