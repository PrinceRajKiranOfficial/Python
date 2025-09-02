# pandas_visualization.py
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Marks": [85, 90, 78, 88],
    "Age": [20, 21, 19, 22],
}

df = pd.DataFrame(data)

print("Descriptive Statistics:\n", df.describe())

# Plot marks of students
df.plot(kind="bar", x="Name", y="Marks", color="skyblue", legend=False)
plt.title("Marks of Students")
plt.ylabel("Marks")
plt.xlabel("Students")
plt.savefig("marks_chart.png", dpi=300)
plt.show()
