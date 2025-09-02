"""
Pandas Example: Series and DataFrame Operations
Author: [Your Name]
Description:
This script demonstrates how to:
1. Create a Series (1D array) with custom indices.
2. Create a DataFrame (2D array) with labeled indices.
3. Access rows and columns using `iloc` and `loc`.
4. Perform basic DataFrame operations: adding, dropping, and renaming columns.
"""

import pandas as pd

# --------------------------------------------------------
# 1. Create a Series (1D Array)
# --------------------------------------------------------
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']

series = pd.Series(data, index=index)

print("=== Series Example ===")
print(series)
print("Access by index position [1]:", series[1])   # Access by integer index
print("Access by label ['c']:", series['c'])       # Access by label
print("\n")

# --------------------------------------------------------
# 2. Create a DataFrame (2D Array)
# --------------------------------------------------------
data = {
    "Name": ["Prince", "Raj", "Kiran"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}

df = pd.DataFrame(data, index=['a', 'b', 'c'])

print("=== DataFrame Example ===")
print(df)
print("\n")

# --------------------------------------------------------
# 3. Data Selection
# --------------------------------------------------------

# Column Access
print("=== Column Access ===")
print(df["Name"])    # Access column using dictionary-style
print(df.Name)       # Access column using attribute-style
print("\n")

# Row Access using iloc (integer-based indexing)
print("=== Row Access using iloc ===")
print(df.iloc[0])    # First row (index position 0)
print("\n")

# Row Access using loc (label-based indexing)
print("=== Row Access using loc ===")
print(df.loc["c"])   # Row with index label 'c'
print("\n")

# --------------------------------------------------------
# 4. DataFrame Operations
# --------------------------------------------------------

# Add new column
df["Experience"] = ["A", "B", "C"]
print("=== After Adding 'Experience' Column ===")
print(df)
print("\n")

# Drop a column
df.drop("Age", axis=1, inplace=True)
print("=== After Dropping 'Age' Column ===")
print(df)
print("\n")

# Rename a column
df.rename(columns={"Name": "Full Name"}, inplace=True)
print("=== After Renaming 'Name' to 'Full Name' ===")
print(df)
