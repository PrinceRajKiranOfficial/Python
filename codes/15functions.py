# --------------------------------------------
# BASIC FUNCTION PRACTICE IN PYTHON
# --------------------------------------------

# 1️⃣ Simple functions without parameters

def add():
    print(10 + 10)  # Output: 20

def sub():
    print(10 - 5)   # Output: 5

def mul():
    print(10 * 5)   # Output: 50

add()               # Output: 20

# ------------------------------------------------------------

# 2️⃣ Function with parameters

def hi(name):
    print("Hello", name)  # Output: Hello Prince

hi("Prince")              # Output: Hello Prince

# ------------------------------------------------------------

# 3️⃣ Function with return value

def square(x):
    return x * x          # Returns: 25

result = square(5)
print(result)             # Output: 25