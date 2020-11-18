"""
La tasa de crecimiento de la población de una ciudad es del 6,5% anual. Si la población actual es de 596.744 habitantes, se pide determinar cuantos habitantes aproximadamente tendrá dentro de 14 años.
"""
p = 596744
for i in range(14):
    n=i+1
    np=p*0.065
    p=p+np
    print(f"para el año {n} la poblacion será {(p)}")
