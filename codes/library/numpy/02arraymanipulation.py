# arraymanipulation.py
"""
Array Manipulation with NumPy

This script demonstrates:
- Indexing and slicing in arrays
- Reshaping arrays
- Flattening multidimensional arrays
"""

import numpy as np

def demo_array_manipulation():
    arr = np.array([[1, 2, 3], 
                    [4, 5, 6]])

    print("Original Array:\n", arr)

    # Indexing
    print("\n--- Indexing ---")
    print("Element at row 0, col 1:", arr[0, 1])  # 2

    # Slicing
    print("\n--- Slicing ---")
    print("All rows, column 1:", arr[:, 1])  # [2, 5]

    # Reshape
    print("\n--- Reshaping ---")
    reshaped = arr.reshape(3, 2)
    print("Reshaped to (3x2):\n", reshaped)

    # Flatten
    print("\n--- Flattening ---")
    flat = arr.flatten()
    print("Flattened array:", flat)


if __name__ == "__main__":
    demo_array_manipulation()
