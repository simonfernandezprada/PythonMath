# Considera la sucesion (5, 10, 15, 20, 25, 30,...).
print("Comparando con el ejemplo 1 de esta guía, ¿qué caracteriza a estos números?\n Que podemos escribir la sucesion (5, 10, 15, 20, 25, 30,...) como 5 sub n.")
print("\nDetermine la expresion algebraica del termino generico de lugar n.\n5(n)")
print("\nCompruebe si su expresion es correcta usando codigo Python")
b = []
n = 0
for i in range (6):
    n=1+i
    b.append(5*n)
    print(f"5({n})={b[i]}")
