# Create a line plot for temperature data across a weeek

"""
Matplotlib Practice: Weekly Temperature Line Plot
Author:"Prince Raj Kiran"
Description:
This script creates a line plot to visualize temperature data over a week.
"""
import matplotlib.pyplot as plt


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperature = [22, 24, 21, 25, 26, 23, 24]

plt.plot(days, temperature, marker='o', color='r', label='Temperature (°C)')

plt.title('Weekly Temperature Variation')
plt.xlabel('Day of the Week')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.savefig('temperature_line_plot.png', dpi=300) 

plt.show()
