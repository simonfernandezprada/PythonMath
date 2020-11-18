print('''
Considere la sucesion an = 3*n^2+7. Determine
a) La suma de los 12 primeros terminos. En el codigo Python, utilice listas para almacenar los terminos de la sucesion an considerados en la suma.
b) La suma desde el 13avo al 24avo termino. En este caso, idear un codigo Python que sume valores con ciclos for o while pero sin acumularlos en una lista.
''')
suma=0
print("a) Si an = 3*n**2+7 entonces:")
b = []
for i in range(12):
    n=i+1
    b.append(3*n**2+7)
    suma=suma+b[i]
print(f"La suma de los 12 primeros terminos es {suma}")
cuma=0
for j in range(12):
    n=j+13
    b=(3*n**2+7)
    cuma=cuma+b
print(f"b) La suma desde el 13avo al 24avo termino es {cuma}")
