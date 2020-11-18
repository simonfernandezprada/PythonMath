print('''
En una sucesion aritmetica, la diferencia entre un termino y el anterior es 4 y el decimo termino es -20. Determine

    a) El primer término.
    b) La expresión del término de lugar n.
    c) El término que ocupa el lugar 100. Utilice un código de forma recursiva y otro con el término de lugar n.
    d) ¿Qué lugar ocupa en esta sucesión el término 1.680?
''')

a1=-4*9-20 #la diferencia es negativa pq estamos avanzando hacia la izquierda en la recta numérica
print(f"a)El primer término es {a1}\n")
print("b)La expresión para n es:      a1+(n-1)*d\n  En este caso                -56+(n-1)*4\n")
# c)
z=a1+(100-1)*4
print(f"c)El lugar número 100, es decir a sub 100 es igual a = {z}\n")
# d)
x=1740/4
print(f"d)La sucesión 1.680 ocupa el lugar {round(x)}")
y=a1+(435-1)*4
