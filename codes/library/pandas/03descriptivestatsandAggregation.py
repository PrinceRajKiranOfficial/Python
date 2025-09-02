"""
Pandas Example: Descriptive Statistics and Aggregation
Author: [Your Name]
Description:
This script demonstrates how to:
1. Generate descriptive statistics using describe().
2. Calculate the mean of a numeric column.
3. Perform aggregation using groupby().
"""

import pandas as pd

# --------------------------------------------------------
# 1. Create a DataFrame
# --------------------------------------------------------
data = {
    "Name": ["Ayasha", "Sahil", "Keshav", "Nishant"],
    "Grade": ["A", "B", "A", "B"],
    "Marks": [90, 75, 85, 70]
}

df = pd.DataFrame(data)

print("=== Original DataFrame ===")
print(df, "\n")

# --------------------------------------------------------
# 2. Descriptive Statistics
# --------------------------------------------------------
print("=== Descriptive Statistics (describe) ===")
print(df.describe(), "\n")

# --------------------------------------------------------
# 3. Mean of Numeric Values
# --------------------------------------------------------
average_marks = df["Marks"].mean()
print("=== Mean of Marks ===")
print("Average Marks:", average_marks, "\n")

# --------------------------------------------------------
# 4. Aggregation using GroupBy
# --------------------------------------------------------
print("=== Group By 'Grade' and Calculate Mean Marks ===")
print(df.groupby("Grade")["Marks"].mean())
