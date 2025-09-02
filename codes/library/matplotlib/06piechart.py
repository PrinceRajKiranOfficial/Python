"""
Matplotlib Example: Pie Chart
Author: "Prince Raj Kiran"
Description:
This script demonstrates how to create a pie chart using Matplotlib.
"""

import matplotlib.pyplot as plt

# --------------------------------------------------------
# 1. Data Preparation
# --------------------------------------------------------
labels = ["A", "B", "C", "D"]   # categories
sizes = [15, 30, 45, 10]        # values for each category
# explode = (0, 0.1, 0, 0)      # Uncomment to highlight the 2nd slice (B)

# --------------------------------------------------------
# 2. Create Pie Chart
# --------------------------------------------------------
fig, ax = plt.subplots()
ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",   # format for percentages
    startangle=90        # start from the top
    # explode=explode    # optional highlighting
)

# --------------------------------------------------------
# 3. Customize Plot
# --------------------------------------------------------
ax.axis("equal")   # ensures the pie chart is a circle
plt.title("Pie Chart")

# --------------------------------------------------------
# 4. Save & Show
# --------------------------------------------------------
plt.savefig("piechart.png", dpi=300)
plt.show()
