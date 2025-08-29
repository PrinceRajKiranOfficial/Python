# Method Overloading in Python

**Method Overloading** allows the same method name to be used with different numbers of parameters.

In many programming languages (like **Java** or **C++**), you can define multiple methods with the same name but different parameter lists. This is called *compile-time polymorphism*.

However, **Python does not support traditional method overloading** directly. In Python, if you define multiple methods with the same name, the latest definition will overwrite the previous ones. But, we can achieve a similar effect using **default parameters** or `*args`.

---

## Key Concept

- **Same method name, different parameters**
- Behavior changes based on the number of arguments passed.

---

## Example: Simulating Method Overloading using `*args`

```python
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()

print(calc.add(10))              # Output: 10
print(calc.add(10, 20))          # Output: 30
print(calc.add(10, 20, 30))      # Output: 60
print(calc.add(10, 20, 30, 40))  # Output: 100


✅ Python doesn’t support traditional method overloading, but we can achieve similar functionality using:

Default arguments

Variable-length arguments (*args)

This creates the illusion of overloading, also known as virtual polymorphism.


Interview Question

Q: In method overloading, what is overloaded?
A:

The method name is overloaded with different parameter lists.

In Python, technically nothing is overloaded — it only creates the illusion of overloading.

Java supports true method overloading at compile time.