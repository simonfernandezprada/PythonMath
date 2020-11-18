# Sea la sucesion (h sub n) definida por su termino general 6n(-1)n.
# a) Determine los 100 primeros terminos.

b = []
n = 0

for i in range(100):
    n=i+1
    b.append(6*n*(-1)**n)
    print(f'h({n})={b[i]}')

# b) Basándose en la sucesión anterior, ¿que caracterısticas observas en los terminos de esta sucesión?
# Que el signo se alterna y que si fuera absoluto adicionaría 6 constantemente
