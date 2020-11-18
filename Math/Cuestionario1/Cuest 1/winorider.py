'''En una bodega hay dos enormes depósitos de vino: A y B.
Todos los días se sacan ciertas cantidades de vino de cada uno de los depósitos.
Del depósito A se extrajeron 5 litros el primer día, 10 litros el segundo día, 15 litros el tercer día, 20 litros el cuarto día y así sucesivamente. Del depósito B se extrajeron 8 litros el primer día, 11 litros el segundo día, 14 litros el tercer día, 17 litros el cuarto día y así sucesivamente.
En el último día de extracción de ambos depósitos, se extrajeron del depósito A 100 litros.

Calcule cuántos litros se extrajeron en total desde el depósito B, desde el primer hasta el último día.
'''
a = []
b = []
suma = 0
for i in range(20):
    n=i+1
    a.append(5+(n-1)*5)
    b.append(8+(n-1)*3)
    suma = suma+b[i]
    print(f" a({n})={a[i]}\t\tb({n})={b[i]}")
print(f"Desde el primer hasta el último día, se extrajeron un total de {suma} litros desde el depósito B")
