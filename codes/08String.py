# """
# String Operations in Python
# ---------------------------
# This script demonstrates common string manipulation techniques in Python.
# Each example includes comments and output for clarity.
# """

# # Define a string variable
# text = "python"

# # Accessing characters by index
# print("First character:", text[0])      # Output: First character: p
# print("Last character:", text[-1])      # Output: Last character: n

# # Getting the length of a string
# print("Length of text:", len(text))     # Output: Length of text: 6

# # Define another string variable
# a = "hello world"

# # Changing case
# print("Uppercase:", a.upper())          # Output: Uppercase: HELLO WORLD
# print("Lowercase:", a.lower())          # Output: Lowercase: hello world
# print("Title case:", a.title())         # Output: Title case: Hello World

# # Removing leading and trailing spaces
# b = "   hello world   "
# print("Original with spaces:", repr(b)) # Output: Original with spaces: '   hello world   '
# print("After strip():", repr(b.strip()))# Output: After strip(): 'hello world'

# # Replacing substrings
# print("Replace 'world' with 'python':", b.replace("world", "python"))
# # Output: Replace 'world' with 'python': '   hello python   '

# # Splitting a string into a list of words
# words = b.split()
# print("Split into words:", words)  # Output: Split into words: ['hello', 'world']

# # Joining a list of words into a single string
# joined = " ".join(words)
# print("Joined with spaces:", joined)  # Output: Joined with spaces: hello world

# # Finding substrings within a string
# string = "hello world, welcome to python programming"
# print("Find 'world':", string.find("world"))    # Output: Find 'world': 6
# print("Find 'Python':", string.find("Python"))  # Output: Find 'Python': -1 (not found)

# # Counting occurrences of a substring
# print("Count 'o':", string.count("o"))          # Output: Count 'o': 4
# print("Count 'a':", "banana".count("a"))        # Output: Count 'a': 3

# # Checking if a string starts or ends with a specific substring
# print("Starts with 'hello':", string.startswith("hello"))      # Output: True
# print("Starts with 'Hello':", string.startswith("Hello"))      # Output: False
# print("Ends with 'programming':", string.endswith("programming"))  # Output: True
# print("Ends with 'Programming':", string.endswith("Programming"))  # Output: False

# String formatting examples
name = "Prince Raj Kiran"
age = 23

# Concatenation using commas
print("My name is", name, "and my age is", age) 

# Using f-strings (recommended for readability)
print(f"My name is {name} and my age is {age}")

# Using the format() method
print("My name is {} and my age is {}".format(name, age))

# String Concatenation
# --------------------
# Combine multiple strings into one using the + operator.
greeting = "Hello"
target = "World"
combined = greeting + " " + target
print("Concatenated string:", combined)  # Output: Concatenated string: Hello World

# String Repetition
# -----------------
# Repeat a string multiple times using the * operator.
repeated = greeting + " "
print("Repeated string:", repeated * 3)  # Output: Repeated string: Hello Hello Hello 

# Membership Operators
# --------------------
# Check if a substring exists within another string using 'in' and 'not in'.
phrase = "Hello World"
print("'Hello' in phrase:", "Hello" in phrase)   # Output: 'Hello' in phrase: True
print("'World' not in combined:", "World" not in combined)  # Output: 'World' not in combined: False