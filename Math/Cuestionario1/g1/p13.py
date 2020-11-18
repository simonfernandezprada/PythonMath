from time import time
import math
print('''
Considere la sucesion geometrica: 4, 6, 9,... Determine
    a) La razon geometrica.
    b) La expresion del termino de lugar n.
    c) El termino de lugar 60. Calcule con la forma directa y con la forma recursiva, compare los tiempos de ejecucion.
    d) ¿Que lugar ocupa en esta sucesion el termino 68,34375? Use logaritmo.''')

r1=6/4
r2=9/6
if r1 == r2:
    r=r1
print(f"\na) La razón geométrica es {r}\n")
a1=4
a2=6
a3=9
print(f"b) La expresión del término de lugar n es an = 4 · 1,5^n-1\n")
# an = 4*1,5**(n-1)
t1 = time()
print(f"c1) El término de lugar 60. Con la forma directa es:   a(60) = {a1*r**(60-1)}\n")
t2 = time()
print(f"Esta operación tomó {t2-t1} segundinis")
t3 = time()
for i in range(61):
    n=i+1
    a=a1*r**(n-1)
    if n == 60:
        print (f"c2) El término de lugar 60. Con la forma recursiva es: a(60) = {a}\n")
t4 = time()
print(f"Esta operación tomó {t4-t3} segundinis")
for j in range(8):
    n=j+1
    b=a1*r**(n-1)
    print(f"b({n})={b}")

xx = round((math.log(68.34375/a1, r))+1)
print(f"\nd) El término 68,34375 ocupa el lugar {xx}")
