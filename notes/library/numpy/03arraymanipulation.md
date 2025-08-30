# Array Manipulation with NumPy

NumPy provides powerful methods for **reshaping, slicing, and flattening arrays**.

---

## Example Code

```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Indexing
print(arr[0, 1])   # 2

# Slicing
print(arr[:, 1])   # [2 5]

# Reshape (2x3 → 3x2)
print(arr.reshape(3, 2))

# Flatten (2D → 1D)
print(arr.flatten())   # [1 2 3 4 5 6]
