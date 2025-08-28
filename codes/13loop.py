"""
Loop Examples in Python
This script demonstrates different types of loops in Python:
1. While loop
2. For loop with range
3. For loop with string
4. Break statement
"""

# -------------------------------
# Example 1: While loop (counting from 1 to 5)
# -------------------------------

count = 1  # Initialize counter
while count <= 5:
    print(count)  # Print current value
    count += 1    # Increment counter


# -------------------------------
# Example 2: For loop with range
# -------------------------------
# range(1, 6) generates numbers from 1 to 5
for i in range(1, 6):
    print("for o/p", i)


# -------------------------------
# Example 3: For loop with a string
# -------------------------------
# Iterates through each character in the string "prince"
for letter in "prince":
    print("letter", letter)


# -------------------------------
# Example 4: Break statement
# -------------------------------
# Loop runs from 1 to 5, but stops immediately when i == 3
for i in range(1, 6):
    if i == 3:
        break  # Exit the loop
    print("break o/p", i)



# continue - if condition is true skip the statement
for i in range(1,11):
    if i == 7:
        continue  # Skip the rest of the loop when i == 7
    print("continue o/p", i)