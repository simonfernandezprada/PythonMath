import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

M=np.array([[100,10,1],[400,20,1],[900,30,1]])
V=np.array([800,1200,1200])

coeficientes=np.linalg.solve(M,V)
print(coeficientes)
