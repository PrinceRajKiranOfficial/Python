# 13practice4
# pie_chart_activities.py
import matplotlib.pyplot as plt

activities = ["Sleep", "Study", "Exercise", "Leisure", "Others"]
hours = [8, 5, 2, 4, 5]

plt.pie(hours, labels=activities, autopct="%1.1f%%", startangle=90)
plt.title("Daily Activities Distribution")
plt.axis("equal")  # Equal aspect ratio ensures circle
plt.savefig("daily_activities_pie.png", dpi=300)
plt.show()
