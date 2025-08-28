# Inheritance in Python

**Inheritance** is one of the fundamental concepts of Object-Oriented Programming (OOP). It allows a **child class** to inherit attributes and methods from a **parent class**.

---

## Key Points
- Inheritance promotes **code reusability**.
- The child class can use methods/attributes of the parent class.
- The child class can also define its own methods/attributes.

---

## Example: Basic Inheritance
```python
# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Object creation
d = Dog()

# Using inherited method
d.speak()  # Output: Animal speaks

# Using child class method
d.bark()   # Output: Dog barks
```

Diagram:
```
 Animal (Parent)
     |
     v
   Dog (Child)
```

---

# Types of Inheritance in Python

## 1. Single Inheritance
A child class inherits from a single parent class.
```python
class Parent:
    def show(self):
        print("This is the parent class")

class Child(Parent):
    def display(self):
        print("This is the child class")

obj = Child()
obj.show()
obj.display()
```
Diagram:
```
 Parent
   |
   v
 Child
```

---

## 2. Multiple Inheritance
A child class inherits from **multiple parent classes**.  
*(In Java, we cannot achieve multiple inheritance directly because Java is a statically typed language, but using interfaces we can achieve it.)*
```python
class Father:
    def skills(self):
        print("Good at driving")

class Mother:
    def skills(self):
        print("Good at cooking")

class Child(Father, Mother):
    pass

obj = Child()
obj.skills()  # Uses method resolution order (MRO)
```
Diagram:
```
 Father      Mother
     \      /
      v    v
       Child
```

---

## 3. Multilevel Inheritance
A class inherits from a child class, making a **chain of inheritance**.
```python
class Grandparent:
    def show(self):
        print("Grandparent class")

class Parent(Grandparent):
    def display(self):
        print("Parent class")

class Child(Parent):
    def hello(self):
        print("Child class")

obj = Child()
obj.show()
obj.display()
obj.hello()
```
Diagram:
```
 Grandparent
      |
      v
    Parent
      |
      v
    Child
```

---

## 4. Hierarchical Inheritance
Multiple child classes inherit from a single parent class.
```python
class Parent:
    def show(self):
        print("This is the parent class")

class Child1(Parent):
    def c1(self):
        print("This is child 1")

class Child2(Parent):
    def c2(self):
        print("This is child 2")

obj1 = Child1()
obj2 = Child2()
obj1.show()
obj2.show()
```
Diagram:
```
        Parent
        /   \
       v     v
   Child1   Child2
```

---

## 5. Hybrid Inheritance
A combination of different types of inheritance.
```python
class A:
    def methodA(self):
        print("Class A method")

class B(A):
    def methodB(self):
        print("Class B method")

class C(A):
    def methodC(self):
        print("Class C method")

class D(B, C):
    def methodD(self):
        print("Class D method")

obj = D()
obj.methodA()
obj.methodB()
obj.methodC()
obj.methodD()
```
Diagram:
```
      A
     / \
    v   v
   B     C
    \   /
     v v
      D
```

---

✅ **Summary**: Inheritance in Python can be of **five types**: single, multiple, multilevel, hierarchical, and hybrid. It improves **code reusability, organization, and extensibility**.
