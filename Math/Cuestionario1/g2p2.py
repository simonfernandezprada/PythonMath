a = []
suma=0
n=0
for i in range (12):
    n=i+1
    a.append(3*n**2+7)
    suma=suma+a[i]
print(f"Ls 12 primeros términos son: \n{a}")
print(f"\nLa suma de estos términos es igual a: {suma}")
