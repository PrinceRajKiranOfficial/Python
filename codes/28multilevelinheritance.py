class Father:
    def fatherHouse(self):
        print("Father's property")

class Mother:
    def motherHouse(self):
        print("Mother's property")

class Child(Father,Mother):
    def childHouse(self):
        pass


obj = Child()


obj.fatherHouse()
obj.motherHouse()
obj.childHouse()