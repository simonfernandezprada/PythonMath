print("Idear un código en Python que calcule un gran número de términos de la sucesión de Fibonacci, \nde manera que se detenga solo cuando la diferencia entre (f sub n / f sub n-1) y phi sea menor a 0,000001.")

#Calculando la constante fi (razón aúrea)
fi = (1+5**(1/2))/2
print (f'\nfi={fi} \n')
n = 2
f = [1,1] #en esta linea declaramos la lista "f" con sus dos primeros elementos: f[0]=1 y f[1]=1
razon = f[1]/f[0]
print(razon)
dif = abs(fi-razon) #la función abs() calcula el valor absoluto del argumento.
print(dif)
#la variable dif nos indica la diferencia en valor absoluto entre la razón de términos consecutivos y la constante FI
print (f'f(1)={f[0]}')
print (f'f(2)={f[1]}')
print (f'f(2)/f(1)={razon}')
print (f'diferencia ={dif} \n')

#a medida que n crece indefinidamente la razón se aproxima al valor de FI, haciendo que la diferencia tienda a CERO.
#la relación recursiva se utiliza desde el tercer término en adelante... f_sub_3 = f[2]
while dif >= 1e-6: #los bucles WHILE se repiten mientras la variable dif sea mayor o igual a 1 millonésima (1E-6)
    f.append(f[n-1]+f[n-2])
    razon = f[n]/f[n-1]
    dif = abs(fi - razon)
    print (f'f({n+1})={f[n]}')
    print (f'f({n+1})/f({n})={razon}')
    print (f'diferencia = {dif} \n')
    n=n+1

'''
n = 0
for i in range (10):

    if n < 2:
        n=1
    elif n > 2:
        n = (n-1) + (n-2)
    print(f"f({i+1})={n}")
    n=i+1
'''
