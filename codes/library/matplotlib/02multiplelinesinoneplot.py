
"""
Matplotlib Example: Multiple Lines in One Plot
Author: "Prince Raj Kiran"
Description:
This script demonstrates how to plot multiple lines on the same graph using Matplotlib.
"""

import matplotlib.pyplot as plt

# --------------------------------------------------------
# 1. Data
# --------------------------------------------------------
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 5, 7, 19]
y2 = [3, 7, 23, 12, 23]

# --------------------------------------------------------
# 2. Create Multiple Line Plots
# --------------------------------------------------------
plt.plot(
    x, y1,
    label="Ascending",
    marker="d",
    color="orange",
    linewidth=2
)

plt.plot(
    x, y2,
    label="Descending",
    marker="d",
    color="blue",
    linewidth=2
)

# --------------------------------------------------------
# 3. Customize the Plot
# --------------------------------------------------------
plt.legend()
plt.title("Multiple Lines in One Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# --------------------------------------------------------
# 4. Save & Show the Plot
# --------------------------------------------------------
plt.savefig("mat2.png", dpi=300)  # Saves the plot as PNG
plt.show()
