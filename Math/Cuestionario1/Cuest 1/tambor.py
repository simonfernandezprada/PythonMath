'''Al llenar un tambor con agua, se registra que durante el minuto 5 el tambor recibe 185 litros y durante el minuto 14 recibe 51 litros. Sabiendo que entre cada minuto disminuye una cantidad "d" de litros de agua menos que en el minuto anterior. Determina la cantidad "d" de litros de agua que recibe minuto a minuto (en caso de aproximar, usar un decimal).'''
m=244.55555555555554
d=-14.88888888888889
i=1
while i<16:
    print(f"m({i})={m}")
    i=i+1
    m=m+d
'''
m5=185
m14=51
dt=m5-m14
print(dt)
d=dt/9
print(d)
m1=m5+d*4
print(m1)
'''
