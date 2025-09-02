
"""
Pandas Example: Handling Missing Values
Author: [Your Name]
Description:
This script demonstrates how to:
1. Detect missing values using isnull().
2. Fill missing values using fillna().
3. Drop rows with missing values using dropna().
"""

import pandas as pd
import numpy as np

# --------------------------------------------------------
# 1. Create a DataFrame with Missing Values
# --------------------------------------------------------
df = pd.DataFrame({
    "Name": ["Prince", "Raj", None],
    "Marks": [90, np.nan, 90]
})

print("=== Original DataFrame with Missing Values ===")
print(df, "\n")

# --------------------------------------------------------
# 2. Detect Missing Values
# --------------------------------------------------------
print("=== Detect Missing Values (isnull) ===")
print(df.isnull(), "\n")

# --------------------------------------------------------
# 3. Fill Missing Values
# --------------------------------------------------------
# Uncomment below lines to fill missing values with "Prince"
# df.fillna("Prince", inplace=True)
# print("=== After Filling Missing Values ===")
# print(df, "\n")

# --------------------------------------------------------
# 4. Drop Rows with Missing Values
# --------------------------------------------------------
df.dropna(inplace=True)
print("=== After Dropping Rows with Missing Values ===")
print(df)
