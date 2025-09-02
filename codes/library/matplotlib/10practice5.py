# 14practice5.py# subplots_example.py
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [10, 8, 6, 4, 2]

plt.subplot(1, 2, 1)
plt.plot(x, y1, label="Increasing", color="blue", marker="o")
plt.plot(x, y2, label="Decreasing", color="red", marker="s")
plt.title("Line Plots")
plt.legend()

plt.subplot(1, 2, 2)
plt.bar(x, y1, color="purple")
plt.title("Bar Chart Example")
plt.xlabel("X-axis")
plt.ylabel("Values")

plt.tight_layout()
plt.savefig("subplots_example.png", dpi=300)
plt.show()
