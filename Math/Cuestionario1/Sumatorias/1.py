# a sub n = 3n - 5
#   27
#   E  a sub m
#  m =23

a = []
suma = 0
for i in range(5):
    m = i + 23
    a.append(3*m-5)
    suma = a[i] + suma
    print(f'a({m})={a[i]}')
print(f'sumatoria = {suma}')
