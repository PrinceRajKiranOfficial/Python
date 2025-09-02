# Plot a bar chart comparing marks of students in 4 subjects.
# bar_chart_subjects.py

import matplotlib.pyplot as plt

# Subjects and marks
subjects = ["Math", "Science", "English", "Computer"]
marks = [85, 90, 78, 88]

# Create bar chart
plt.bar(subjects, marks, color="skyblue", edgecolor="black")

# Add labels and title
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Marks of a Student in 4 Subjects")

# Save and show plot
plt.savefig("student_marks.png", dpi=300)
plt.show()
