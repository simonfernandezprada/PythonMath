# Sea la sucesion (h sub n) definida por su termino general 6n(-1)^n.
# a) Determine los 100 primeros terminos.

h = []
n = 0

for i in range(100):
    n = i + 1
    h.append(6 * n *(-1) ** n)
    print(f"h({n})={h[i]}")

# b) Basandose en la experiencia con la sucesion de la pregunta anterior, ¿que caracterısticas observas en los terminos de esta sucesion?
print("\n¿Que características observas en los terminos de esta sucesión?")
print("Que la posición impar es negativa y la par es positiva")
