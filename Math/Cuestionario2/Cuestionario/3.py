import numpy as np

M = np.array([[4, 6],
              [2, 8]])

Q = np.array([[3, 7],
              [9, 12]])

H = M.dot(Q)
print (f"H = {H}")
