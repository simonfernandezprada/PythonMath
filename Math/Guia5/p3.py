

print("""
a) ¿Que titulo deberia llevar cada eje coordenado?
Eje x Horizontal: Tiempo en minutos
Eje y Vertical: Altura en metros

b) ¿Cual es el dominio contextualizado de la funcion?
D = !R
DC = {0, 4}

c) Interprete las coordenadas del punto B dado en el grafico.
En 1.5 minutos el montacargas se ha elevado 93.75 mts

d) Estime e interprete f(1). Escriba las coordenadas (1, f (1)) en la grafica.
Al minuto 1 el montacargas se ha elevado 75mts

e) Si f (x) = 75, estime los valores de x e interprete resultados.
x = 1
x = 3

f) Si viene de regreso y su altura es 45 metros, estime el tiempo desde que se
inicio el recorrido.
3.5 minutos

g) Si la forma algebraica de la funcion es f (x) = 25x^2 +100x, calcule f(2)
a los 2 minutos 100 metros es la altura del montacarga
y f(3.55), luego interprete resultados.
a los 3.55 minutos 39.94 metros es la altura del montacarga
""")

def f(x):
    f=(-25*x**2)+(100*x)
    return f

x=2
salto=1.55
while x <= 4:
    y=f(x)
    print(f"f({x})={round(y,2)}")
    x=x+salto

print("""
h) ¿Cuantos minutos han transcurrido desde que se inicio el recorrido para
que la distancia recorrida por el montacargas sea de 125 metros?
3 minutos
""")
