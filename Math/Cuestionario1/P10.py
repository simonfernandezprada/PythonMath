phi = (1 + 5 **(1/2))/2     #fórmula para sacar phi
print(f"phi={phi}\n")       #impresión de phi
n=2                         #Ya que los dos primeros de fibonacci son 1 y 1 partiremos del 2
f=[1,1]
dif = 1                     #y dejaremos esos valores por defecto en la lista f[]
while dif > 0.000001:               #bucle de 20 vueltas
    f.append(f[n-1]+f[n-2])         #agregamos un nvo valor a la lista fibonacci al sumar los dos valores anteriores
    print(f"f({n+1})={f[n]}")       #imprimimos fibonacci sub n y su valor
    razon=f[n]/f[n-1]               #pq la razón se calcula al reves?
    dif=phi-razon                   #
    print(razon)
    print(f"{dif}\n")
    n=n+1                           #agregamos +1 al bucle
