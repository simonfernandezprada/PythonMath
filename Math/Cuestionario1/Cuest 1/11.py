'''Sea la sucesión (an) = [2,6,18] Con respecto a esta sucesión, tenemos la siguiente suma:
486 + 1.458 + ... + 354.294 ¿Qué expresión(es) es(son) equivalentes a la suma anterior?
an=a1*r**(n-1)
an=2*3**(n-1)
'''
r=3
a1=2
for i in range(12):
    n=i+1
    a = a1*r**(n-1)
    print(f"a({n})={a}")
a6=486
a12=354294

z=[]
suma=0
for i in range(7):
    m=i+5
    z.append(a1*r**(m-1))
    suma=z[i]+suma
print(f"La suma de las posiciones del a(5) al a(12) es {suma}")

e5_12=(a1*((r**12)-1))/r-1
print(e5_12)

# RESPUESTA SOLO I
