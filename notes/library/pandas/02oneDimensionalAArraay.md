# Pandas: Series vs DataFrame

## 📌 1D Array using Series
In Pandas, if you want to make a **1D array**, you can use the **Series** data structure.  
A `Series` is essentially a **one-dimensional labeled array** capable of holding any data type (integers, strings, floats, etc.).

### ✅ Example: Creating a Series
```python
import pandas as pd

# Create a 1D array (Series)
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Display the Series
print(series)


import pandas as pd

# Create a 2D array (DataFrame)
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)
```