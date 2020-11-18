import math
print('''El tercer termino de una sucesion geometrica es 5 y el sexto termino es 40. Determine
    a) La razon geometrica. Analice cuantos pasos hay entre ambos terminos que se indican.
    b) El primer termino.
    c) La expresion del termino de lugar n.
    d) El octavo termino. Calcule con la forma que estime conveniente.
    e) ¿Que lugar ocupa en esta sucesion el termino 20.480? Use logaritmo.
''')
r=2
a1=1.25
a3=5
a4=10
a5=20
a6=40
print(f"a) La razon geométrica es igual a {r}. La cantidad de pasos entre ambos terminos que se indican es igual a 3 pasos.")
print(f"b) El primer término es a(1) = {(5/2)/2}")
print(f"c) La expresión del término de lugar n es an = 1.25*2**(n-1)")
print(f"d) El octavo término es a(8) = {round(1.25*2**(8-1))}")
x = round((math.log(20480/a1, r))+1)
print(f"e) El término 20.480 ocupa el lugar {x}")
