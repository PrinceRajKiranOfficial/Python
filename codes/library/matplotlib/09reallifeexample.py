"""
Real-Life Example: Sales Dashboard
Author: "Prince Raj Kiran"
Description:
This script demonstrates a real-life example of visualizing 
monthly sales and profit data using Matplotlib.
"""

import matplotlib.pyplot as plt

# --------------------------------------------------------
# 1. Data Preparation
# --------------------------------------------------------
months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [3000, 4000, 3500, 5000]
profit = [800, 1200, 1000, 1500]

# --------------------------------------------------------
# 2. Plot Sales & Profit
# --------------------------------------------------------
plt.plot(months, sales, label="Sales", marker='o', color='blue', linewidth=2)
plt.plot(months, profit, label="Profit", marker='s', color='green', linewidth=2)

# --------------------------------------------------------
# 3. Chart Customization
# --------------------------------------------------------
plt.title("Monthly Performance Dashboard")
plt.xlabel("Month")
plt.ylabel("Amount (in USD)")
plt.legend()
plt.grid(True)

# --------------------------------------------------------
# 4. Save & Show Plot
# --------------------------------------------------------
plt.savefig("sales_dashboard.png", dpi=300)
plt.show()
