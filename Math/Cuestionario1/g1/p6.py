# Considere la sucesion (b sub n) de termino general (1 + 1/n)^n
# a) Usando todos los decimales que entrega Python, determine los terminos b10, b100, b1.000, b10.000, b100.000.
print(f"b(10)={(1+1/10)**10}")
print(f"b(100)={(1+1/100)**100}")
print(f"b(1000)={(1+1/1000)**1000}")
print(f"b(10000)={(1+1/10000)**10000}")
print(f"b(100000)={(1+1/100000)**100000}")
# b) Despues de calcular los terminos anteriores,
print("\nQué tipo de sucesión es (b sub n)?\nEs monótona creciente")
# c) ¿Algun termino es mayor que el numero de Euler?
from math import e
print(f"\nEl número Euler es : {e}")
print("¿Algun término es mayor que el número de Euler?\nNo")
