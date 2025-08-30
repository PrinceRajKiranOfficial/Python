# numpy_arrays.py
"""
NumPy Arrays and Common Array Creators

This script demonstrates:
- Creating 1D and 2D NumPy arrays
- Checking array properties (shape, dimensions, data type)
- Using common NumPy array creator functions
"""

import numpy as np

def demo_arrays():
    # 1D array
    a = np.array([1, 2, 3])
    print("1D Array:\n", a)

    # 2D array
    b = np.array([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]])
    print("\n2D Array:\n", b)

    # Array properties
    print("\n--- Array Properties ---")
    print("a.shape:", a.shape)   # (3,)
    print("b.shape:", b.shape)   # (3, 3)

    print("a.ndim:", a.ndim)     # 1
    print("b.ndim:", b.ndim)     # 2

    print("a.dtype:", a.dtype)   # int64 (may vary depending on system)
    print("b.dtype:", b.dtype)

    # Common creators
    print("\n--- Common Array Creators ---")
    print("Zeros (2x3):\n", np.zeros([2, 3]))
    print("Ones (3x2):\n", np.ones([3, 2]))
    print("Identity Matrix (3x3):\n", np.eye(3))
    print("Range with step (1 to 100, step 10):\n", np.arange(1, 100, 10))
    print("Linearly spaced values (0 to 1, 5 points):\n", np.linspace(0, 1, 5))


if __name__ == "__main__":
    demo_arrays()
# --- IGNORE ---