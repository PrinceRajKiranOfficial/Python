# Access Modifiers in Python

Access modifiers define the **visibility and accessibility** of class attributes and methods. Python does not have strict access control like Java or C++, but it follows **naming conventions** to indicate the level of access.

---

## 1. Public
- **Definition:** Data and methods are accessible from anywhere.
- **Syntax:** No special syntax (default in Python).

**Example:**
```python
class Student:
    def __init__(self, name):
        self.name = name  # public attribute

obj = Student("Alice")
print(obj.name)  # Accessible anywhere
```

---

## 2. Protected
- **Definition:** Data and methods should be accessible within the class and subclasses (not enforced, just a convention).
- **Syntax:** Prefix with a **single underscore `_`**.

**Example:**
```python
class Student:
    def __init__(self, name, age):
        self._age = age  # protected attribute

obj = Student("Alice", 20)
print(obj._age)  # Accessible, but discouraged outside class/subclass
```

---

## 3. Private
- **Definition:** Data and methods are accessible **only within the class**.
- **Syntax:** Prefix with **double underscores `__`**.

**Example:**
```python
class Student:
    def __init__(self, rollno):
        self.__rollno = rollno  # private attribute

    def get_rollno(self):
        return self.__rollno

obj = Student(101)
# print(obj.__rollno)  # ❌ Error: cannot access directly
print(obj.get_rollno())  # ✅ Access using getter
```

---

✅ **Summary**:
- **Public:** Accessible everywhere (default)
- **Protected:** Accessible within class & subclass (convention: `_var`)
- **Private:** Accessible only inside class (convention: `__var`)
X