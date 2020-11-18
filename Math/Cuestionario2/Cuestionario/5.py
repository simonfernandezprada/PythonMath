import numpy as np

A = np.array([[1.5, 1.9],
              [0.9, 1.2],
              [1.8, 1.4]])

B = np.array([[461, 757, 584, 512],
              [512, 690, 506, 471]])

C = A.dot(B)
print (f"C = {C}")
