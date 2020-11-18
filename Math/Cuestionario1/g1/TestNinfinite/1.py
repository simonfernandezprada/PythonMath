b= []
bn=0.03125
b.append(bn)
for i in range(17):
    n=i+1
    bn=bn*2
    b.append(bn)
    print (f'b({n})={b[i]}')
