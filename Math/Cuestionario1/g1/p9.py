print('''Considere las sucesiones
(t sub n) = (2, 5, 10, 17, 26, 37,...),
(u sub n) = (0, 3, 8, 15, 24, 35,...) y
(v sub n) = (10, 40, 90, 160, 250, 360,...).

a) Para cada sucesión, determine la expresión algebraica del término de lugar n.

(t sub n) = (2, 5, 10, 17, 26, 37,...) = (n^2)+1
(u sub n) = (0, 3, 8, 15, 24, 35,...) = (n^2)-1
(v sub n) = (10, 40, 90, 160, 250, 360,...) = (n^2)*10

b) Compruebe las tres expresiones en un mismo código Python.
''')
t = []
u = []
v = []
for i in range(6):
    n=i+1
    t.append((n**2)+1)
    print(f"t({n})={t[i]}")
print("")
for i in range(6):
    n=i+1
    u.append((n**2)-1)
    print(f"u({n})={u[i]}")
print("")
for i in range(6):
    n=i+1
    v.append((n**2)*10)
    print(f"v({n})={v[i]}")
