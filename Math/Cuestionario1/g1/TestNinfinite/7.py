"""
La tasa de crecimiento de la población de una ciudad es del 3,3% anual. Si la población actual es de 417894 habitantes, se pide determinar cuantos habitantes aproximadamente tendrá dentro de 12 años.
"""
p = 417894
for i in range(12):
    n=i+1
    np=p*0.033
    p=p+np
    print(f"para el año {n} la poblacion será {(p)}")
