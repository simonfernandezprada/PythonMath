# Considera la sucesion (7, 14, 21, 28, 35, 42,...).
print("Al mirar los términos de esta sucesión,\n(7, 14, 21, 28, 35, 42,...)\n¿Qué puede decir de ellos?\n\nQue son una sucesión aritmética monótona creciente")
print("\nDetermine la expresion algebraica del término genérico de lugar n.\n7n")
print("\nCompruebe si su expresion es correcta usando código Python.")
b = []
n = 0
for i in range(6):
    n=i+1
    b.append(7*n)
    print(f"7({n})={b[i]}")
