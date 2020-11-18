'''En una sucesión aritmética, la diferencia entre un término y el anterior es 8,7 y el término de lugar 15 es -449. Determine el primer término.'''

a1=-5.1*15-477.8
print(a1)

a=-8.7*15-449
print(a)

d=8.7
b=-579.5
b1=-579.5
b14=-457.7
b15=-449

for i in range(20):
    print(f"b({i}={b})")
    b=b+d
    i=i+1
