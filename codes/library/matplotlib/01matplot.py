
"""
Matplotlib Example: Basic Line Plot
Author: "Prince Raj Kiran"
Description:
This script demonstrates how to create a simple line plot using Matplotlib.
"""

import matplotlib.pyplot as plt

# --------------------------------------------------------
# 1. Data
# --------------------------------------------------------
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 16]

# --------------------------------------------------------
# 2. Create a Line Plot
# --------------------------------------------------------
plt.plot(x, y, marker="o", color="blue", linestyle="-")

# --------------------------------------------------------
# 3. Customize the Plot
# --------------------------------------------------------
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

# --------------------------------------------------------
# 4. Show the Plot
# --------------------------------------------------------
plt.show()
