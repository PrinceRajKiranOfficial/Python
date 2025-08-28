"""
Student Class Example in Python
-------------------------------
This script demonstrates how to define a class with attributes and methods,
create objects from that class, and access object data.
"""

# Class definition
class Student:
    def __init__(self, name, age, rollno):
        # Initializing attributes using self
        self.name = name
        self.age = age
        self.rollno = rollno

    def hiFunction(self):
        # Method to display student information
        print(f"Hello, my name is {self.name} and I am {self.age} years old. "
              f"And my roll no is {self.rollno}")


# Object creation
s1 = Student("Prince", 20, 235)

# Method call
s1.hiFunction()
# Accessing object data
print(s1.name)
print(s1.age)
print(s1.rollno)