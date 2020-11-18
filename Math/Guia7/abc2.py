import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

M=np.array([[100,10,1],[400,20,1],[1600,40,1]])
V=np.array([3,4,0])

coeficientes=np.linalg.solve(M,V)
print(coeficientes)
