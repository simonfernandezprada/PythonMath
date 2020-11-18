l14=-473.8
l15=-464.1
d=9.7
dt=d*14
l1=l15-dt
l=[]
print (l1)
l.append(l1)
for i in range(15):
    n=i+1
    l.append(l1+(d*n))
    print(f"l({n})={l[i]}")

"""
l15=-445.7
d=10.9
l16=-434.8
dt=d*15
l1=l16-dt
l=[]
l1=-598.3
l.append(l1)
for i in range(16):
    n=i+1
    l.append(l1+(d*n))
    print(f"l({n})={l[i]}")


l15=-442.5
d=11.6
l16=-430.9
dt=d*15
print(dt)
l1=l16-dt
print(l1)
l=[]
l1=-604.9
l.append(l1)
for i in range(16):
    n=i+1
    l.append(l1+(d*n))
    print(f"l({n})={l[i]}")
"""
