# Considere la sucesion aritmetica 25,72; 26,93; 28,14 ... Determine
a = [25.72, 26.93, 28.14]

# a) La diferencia aritmetica
print (f'a(2)-a(1)={a[1]-a[0]}')
print (f'a(3)-a(2)={a[2]-a[1]}')


# b) La expresion algebraica del termino de lugar n.
# 1.21*n-24.51
# or
# an=a1+(n-1)d

# c) Calcule el termino del lugar 50 con dos codigos de Python diferentes. El primero de ellos con la expresion algebraica del termino de lugar n y el segundo de manera recursiva y compare los tiempos de ejecucion.
from time import time

#cálculo con fórmula término de lugar "n"
t1=time()
a1=25.72 #valor del primer término
d=1.21 #valor de la diferencia aritmética
print ('\nCALCULO CON TERMINO DE LUGAR n')
print (f'a(50)={a1+(50-1)*d}')
t2=time()
print (f'tiempo de ejecución = {t2-t1} segundos')

#cálculo con fórmula recursiva
t3=time()
n=50
i=1
a=[]
a.append(a1) #agregando el valor de "a1" como a[0]

while i<n:
  a.append(a[i-1]+d)
  i=i+1
  

print ('\nCALCULO CON FORMULA RECURSIVA')
print (f'a({n})={a[n-1]}')
t4=time()
print (f'tiempo de ejecución = {t4-t3} segundos')

#n=input("ingresa un número para reemplazar a n en: an = 1.21*n-24.51\n\n")
#an = 1.21*n-24.51
#print(an)
# d) ¿Que lugar ocupa en esta sucesion el termino 411,71?

a1=25.72
d=1.21
n=1
a_actual=a1

while a_actual <= 411.71:
  a_anterior=a_actual
  a_actual=a_anterior+d
  n=n+1

print (f'a({n-1})={a_anterior}')
print (f'a({n})={a_actual}')
