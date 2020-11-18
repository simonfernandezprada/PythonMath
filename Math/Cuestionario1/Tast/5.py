'''d=11.25
m=218
for i in range(12):
    n=i+2
    m=m-d
    print(f"m({n})={m}")'''

m5=185
m14=51 # m5-m14=dt
dt=134 #
d=dt/9
print(d) # m1=m5+d*4
m1=d*4+m5
print(m1)
m=m1
for i in range(15):
    m=m-d
    n=i+2
    print(f"m({n})={m}")
