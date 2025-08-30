# Pandas: Powerful Data Analysis Library

## 📌 Introduction
Pandas is an **open-source Python library** primarily used for **data manipulation and analysis**.  
It provides two main data structures:  
- **DataFrame** → A 2D labeled data structure (like an Excel sheet or SQL table).  
- **Series** → A 1D labeled array (like a column in Excel).  

These are designed to handle **tabular data** and **time-series data** efficiently.

---

## 📌 Key Features
- Easy handling of **missing data**.  
- Powerful **group by** functionality for aggregating and summarizing data.  
- Tools for reading and writing data between in-memory structures and different file formats like:  
  - CSV files  
  - Excel spreadsheets  
  - SQL databases  
  - JSON, HTML, and more  

⚠️ Note: Pandas is **not a database**, but it can work seamlessly with data from various sources.

---

## 📌 What Can Pandas Do?
Pandas gives you quick and powerful insights about the data. For example:  
- Is there a correlation between two or more columns?  
- What is the **average value** of a column?  
- What is the **maximum value** in a dataset?  
- What is the **minimum value**?  

---

## 📌 Example Usage
```python
import pandas as pd

# Create a simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Perform basic operations
print("Average Age:", df["Age"].mean())
print("Max Salary:", df["Salary"].max())
print("Min Salary:", df["Salary"].min())
