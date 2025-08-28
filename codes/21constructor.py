"""
Car Class Example in Python
---------------------------
This script demonstrates how to use the __init__ constructor to initialize
object attributes and display object information using a method.
"""

# Class definition
class Car:
    def __init__(self, name, model, year):
        # Initializing attributes using self
        self.name = name
        self.model = model
        self.year = year

    def carInfo(self):
        # Method to display car information
        print(f"Car Name: {self.name}, Model: {self.model}, Year: {self.year}")


# Object creation
s1 = Car("Toyota", "Camry", 2020)

# Method call
s1.carInfo()