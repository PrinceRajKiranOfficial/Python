
"""
Matplotlib Example: Subplots
Author: "Prince Raj Kiran"
Description:
This script demonstrates how to create multiple plots (line + bar)
in a single figure using Matplotlib's subplot functionality.
"""

import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------------
# 1. Data Preparation
# --------------------------------------------------------
x = [1, 2, 3, 4, 5]
y = [5, 7, 4, 6, 8]

# --------------------------------------------------------
# 2. Create Subplots
# --------------------------------------------------------
plt.subplot(1, 2, 1)       # 1 row, 2 columns, position 1
plt.plot(x, y, marker="o", color="blue")
plt.title("Line Plot")

plt.subplot(1, 2, 2)       # 1 row, 2 columns, position 2
plt.bar(x, y, color="green")
plt.title("Bar Chart")

# --------------------------------------------------------
# 3. Adjust Layout
# --------------------------------------------------------
plt.tight_layout()  # avoids overlapping of titles/labels
plt.savefig("subplot.png", dpi=430)

# --------------------------------------------------------
# 4. Display
# --------------------------------------------------------
plt.show()
