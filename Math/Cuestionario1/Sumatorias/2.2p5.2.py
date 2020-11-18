# a sub i = 45 + 4i
suma = 0
for i in range(22,651):
    suma = suma + 45 + 4*i
print(f'La suma = {suma}')

# b)
termino=45 + 4*i
suma=termino

for i in range(23,651):
  termino=termino+4
  suma=suma+termino

print(f'suma = {suma}')

# c) n=560 d=7 a1=61+7*1

a1=61+7*1
d=7
n=560

suma=n/2*(2*a1+(n-1)*d)

print(f'suma = {suma}')
