#aggeregate function .py
import numpy as np
arr = np.array([[1,2],[3,4]])
print(arr.sum())
print(arr.mean())
print(np.median(arr))
print(arr.max())

#boolean indexing and filtering
x = np.array([1,2,3,4])
y = x>3
print(x[y])