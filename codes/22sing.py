"""
Random Student Selector
-----------------------
This script randomly selects a student from a list
and prints their name as today's singer.
"""

import random

# List of students
students = [
    'sam', 'pratyoosh', 'saket', 'jheel', 'yukta', 'shaswat', 'ali', 'veer',
    'nikita', 'nency', 'neev', 'aayasha', 'vani', 'Harshika', 'keshav',
    'mustafa', 'preet', 'ritesh', 'abishek', 'sonu', 'raj', 'naveen'
]

# Randomly select a student
selected_student = random.choice(students)

# Print the result
print("🎤 Today's singer is:", selected_student)


