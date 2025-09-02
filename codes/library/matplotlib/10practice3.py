# scatter_plot.py
import matplotlib.pyplot as plt

height = [150, 160, 170, 180, 190]
weight = [50, 60, 70, 80, 90]

plt.scatter(height, weight, color="green", marker="o")
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.savefig("scatter_plot.png", dpi=300)
plt.show()
