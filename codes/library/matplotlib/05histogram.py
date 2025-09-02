"""
Matplotlib Example: Histogram
Author: "Prince Raj Kiran"
Description:
This script demonstrates how to create a histogram using random numbers
generated with NumPy and visualized with Matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------------
# 1. Generate Random Data
# --------------------------------------------------------
# Normal distribution with mean=0 and std=1
data = np.random.randn(1000)

# --------------------------------------------------------
# 2. Create Histogram
# --------------------------------------------------------
plt.hist(
    data,
    bins=30,            # number of bins
    color="skyblue",    # fill color
    edgecolor="black"   # bin border color
)

# --------------------------------------------------------
# 3. Customize the Plot
# --------------------------------------------------------
plt.title("Histogram of Random Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")

# --------------------------------------------------------
# 4. Save & Show Plot
# --------------------------------------------------------
plt.savefig("histogram.png", dpi=300)
plt.show()

