print("Matriz M 100%\n")
M=[[60,70],
[40,50],
[30,60]]
print(f"{M}\n\nMatriz M 80%\n")

for i in range(3):
  for j in range(2):
    M[i][j]=0.8*M[i][j]
  print(M[i])

print("\nMatriz F 100%\n")
F=[[70,80],
   [60,50],
   [20,40]]
print(f"{F}\n\nMatriz F 90%")

for i in range(3):
  for j in range(2):
    F[i][j]=0.9*F[i][j]
  print(F[i])
