# a sub i = 61 + 7i

# a)
suma = 0
for i in range(1,561):
    suma = suma + 61 + 7*i
print(f'La suma = {suma}')

# b)
termino=61+7*1
suma=termino

for i in range(2,561):
  termino=termino+7
  suma=suma+termino

print(f'suma = {suma}')

# c) n=560 d=7 a1=61+7*1

a1=61+7*1
d=7
n=560

suma=n/2*(2*a1+(n-1)*d)

print(f'suma = {suma}')
