"""
Matplotlib Example: Bar Chart
Author:"Prince Raj Kiran"
Description:
This script demonstrates how to create a vertical bar chart using Matplotlib.
It also shows how to create a horizontal bar chart as an alternative.
"""

import matplotlib.pyplot as plt

# --------------------------------------------------------
# 1. Data
# --------------------------------------------------------
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]

# --------------------------------------------------------
# 2. Create a Vertical Bar Chart
# --------------------------------------------------------
plt.bar(categories, values, color="purple")

# --------------------------------------------------------
# 3. Customize the Plot
# --------------------------------------------------------
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

# --------------------------------------------------------
# 4. Save & Show the Plot
# --------------------------------------------------------
plt.savefig("bar.png", dpi=250)
plt.show()

# --------------------------------------------------------
# Alternative: Horizontal Bar Chart
# --------------------------------------------------------
# plt.barh(categories, values, color="purple")
# plt.title("Horizontal Bar Chart")
# plt.xlabel("Values")
# plt.ylabel("Categories")
# plt.show()
