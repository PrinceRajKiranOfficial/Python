
"""
Matplotlib with Pandas Integration
Author: "Prince Raj Kiran"
Description:
This script demonstrates how to integrate Pandas with Matplotlib 
to create a simple bar chart of students' marks.
"""

import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------------
# 1. Create DataFrame
# --------------------------------------------------------
data = {
    "Name": ["Ayasha", "Sahil", "Keshav", "Nishant"],
    "Grade": ["A", "B", "A", "B"],
    "Marks": [90, 75, 85, 70]
}

df = pd.DataFrame(data)

# --------------------------------------------------------
# 2. Plot Bar Chart directly from DataFrame
# --------------------------------------------------------
# Pandas' .plot() method is a convenient wrapper around Matplotlib.
df.plot(
    kind='bar',      # Specify the plot type
    x='Name',        # Column for the x-axis
    y='Marks',       # Column for the y-axis
    color='skyblue',
    legend=False     # Hide the legend as it's redundant here
)

plt.title("Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=0) # Keep student names horizontal for readability
plt.grid(axis='y', linestyle='--', alpha=0.7) # Add a horizontal grid

# Adjust layout to prevent labels from being cut off
plt.tight_layout()

# --------------------------------------------------------
# 3. Save & Show Plot
# --------------------------------------------------------
plt.savefig("bar_chart.png", dpi=300)
plt.show()
