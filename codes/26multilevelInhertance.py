# 26 multilevel Inheritance.py
class Grandparent:
    def grandparentHouse(self):
        print("This is grandparent property")


class Parent(Grandparent):
    def parentHouse(self):
        print("This is parent property")


class Child(Parent):
    def childHouse(self):
        print("This is child property")


c1 = Child()
c1.grandparentHouse()   
c1.parentHouse()
c1.childHouse()
