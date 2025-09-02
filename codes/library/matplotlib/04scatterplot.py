
"""
Matplotlib Example: Scatter Plot
Author: "Prince Raj Kiran"
Description:
This script demonstrates how to create a simple scatter plot using Matplotlib.
"""
import matplotlib.pyplot as plt

# --------------------------------------------------------
# 1. Data
# --------------------------------------------------------
x = [1, 2, 3, 4, 5]
y1 = [25, 153, 56, 84, 135]

# --------------------------------------------------------
# 2. Create a Scatter Plot
# --------------------------------------------------------
plt.scatter(x, y1, color="orange", marker="o", edgecolor="black")

# --------------------------------------------------------
# 3. Customize the Plot
# --------------------------------------------------------
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True, linestyle="--", alpha=0.6)

# --------------------------------------------------------
# 4. Save & Show the Plot
# --------------------------------------------------------
plt.savefig("scatter.png", dpi=300)
plt.show()
