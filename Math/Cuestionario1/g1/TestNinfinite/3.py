a=[]
a1=5
a.append(a1)
for i in range(3):
    n=i+1
    a.append(a1+(12*n))
    print(f"a({n})={a[i]}")
