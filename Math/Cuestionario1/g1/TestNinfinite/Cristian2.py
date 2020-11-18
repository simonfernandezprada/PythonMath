'''Al llenar un tambor con agua, se registra que durante el minuto 5 el tambor recibe 185 litros y durante el minuto 14 recibe 51 litros. Sabiendo que entre cada minuto disminuye una cantidad "d" de litros de agua menos que en el minuto anterior. Determina la cantidad "d" de litros de agua que recibe minuto a minuto (en caso de aproximar, usar un decimal).

m=234.22222222222223
d=-13.555555555555555
i=1
while i<16:
    print(f"m({i})={m}")
    i=i+1
    m=m+d

m5=180
m14=58
dt=m5-m14
print("d total = ")
print(dt)
d=dt/9
print("d =")
print(d)
m1=m5+d*4
print("m1 = ")
print(m1)
'''
a747=(3/2) * (747 ** 3) - (2 * 747)
print(a747)
