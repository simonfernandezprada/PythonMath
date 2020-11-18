from time import time
t1=time()

n_al_cubo=40000/5
n=(n_al_cubo)**(1/3)

if round(n)-n < 1e-6:
    print(f"\n40.000 pertenece a la sucesión y ocupa el lugar " + str(round(n)) )
else:
    print("40.000 no pertenece a la sucesión.")
t2=time()
s=t2-t1
print(f"Esta ecuación tomó {s} segundos")
