# hierarchical_inheritance.py
"""
This script demonstrates Hierarchical Inheritance in Python.
- One Parent class is inherited by multiple Child classes.
"""

# Parent class
class Parent:
    def parentHouse(self):
        print("Parent's property")


# Child1 class inheriting Parent
class Child1(Parent):
    def child1House(self):
        print("Child1's property")


# Child2 class inheriting Parent
class Child2(Parent):
    def child2House(self):
        print("Child2's property")


# Object creation and method calls
if __name__ == "__main__":
    obj1 = Child1()
    obj2 = Child2()

    # Accessing Parent and Child1 methods
    obj1.parentHouse()
    obj1.child1House()

    # Accessing Parent and Child2 methods
    obj2.parentHouse()
    obj2.child2House()
