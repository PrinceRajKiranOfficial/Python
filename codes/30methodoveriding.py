class Parent:
    def marry(self):
        print("Samanta! You should not marry at the age 13")

class Child(Parent):
    def marry(self):
        print("Paa! I will marry at 30")

c = Child()
c.marry()  # Output: Paa! I will marry at 30