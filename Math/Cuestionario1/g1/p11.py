from time import time
'''
Considere la sucesion aritmetica 25,72; 26,93; 28,14,.... Determine
a) La diferencia aritmetica
b) La expresion algebraica del termino de lugar n.
c) Calcule el termino del lugar 50 con dos codigos de Python diferentes. El 1ro de ellos con la expresion algebraica del
termino de lugar n y el 2do de manera recursiva y compare los tiempos de ejecucion.
d) ¿Que lugar ocupa en esta sucesion el termino 411,71?
'''
# a)

a1 = 25.72
a2 = 26.93
a3 = 28.14

dif1 = a2-a1
dif2 = a3-a2
print("a)")
print (f"La diferencia entre a1 y a2 es: {round(dif1,2)}")
print (f"La diferencia entre a2 y a3 es: {round(dif2,2)}\n")
if dif1 == dif2:
    print("Las diferencias entre a1 y a2; y entre a2 y a3 son iguales, evidencia de que es una sucesión aritmética")
else:
    print("Las diferencias no son iguales. Ojo piojo.")

# b)
print("b)")
print("a sub n = 1,21n+25,72-1,21")
n=int(input("Ingrese un valor entero para n: "))
print(f"a({n})={round(1.21 * n + (25.72-dif1),2)}")

# c1)
t1 = time()
a50 = 1.21*50 +(25.72-1.21)
print(f"a(50)={round(a50,2)}")
t2 = time()
print(f"Esta operación tomó {t2-t1} segundinis")

# c2)
t3 = time()
for i in range (51):
    a_sub_i = 1.21*i +(25.72-1.21)
    n=i+1
    if i== 50:
        print(f"a({i})={round(a_sub_i,2)}")
t4 = time()
print(f"Esta operación tomó {t4-t3} segundinis")

# d)
x=(1.21+411.71-25.72)/1.21
print (round(x))
