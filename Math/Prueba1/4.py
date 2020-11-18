z = 2000000
for j in range (4):
    z = z * 1.015
    j = j + 1
    print(f"z({j})={z}")

print("\na)")
for i in range(4):
    i = i + 1
    s = 2000000 + 30000 * (i - 1)
    print(f"s({i})={s}")

print("\nb)")
for i in range(4):
    i = i + 1
    s = 2000000 * 1.015**(i-1)
    print(f"s({i})={s}")

print("\nc)")
for i in range(4):
    i = i + 1
    s = 2030000*1.015**(i-1)
    print(f"s({i})={s}")
