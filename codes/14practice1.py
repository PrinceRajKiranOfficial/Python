# --------------------------------------------
# PRACTICE QUESTIONS: Control Flow & Loops
# Real-Life Example: ATM Simulation (Conceptual)
# --------------------------------------------

# 1️⃣ Check if a number is positive, negative, or zero
# This function uses conditional statements to classify a number.
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# ------------------------------------------------------------

# 2️⃣ Print numbers from 1 to 20, skipping multiples of 3
# Demonstrates use of 'continue' to skip specific values in a loop.
print("\nNumbers from 1 to 20 (excluding multiples of 3):")
for i in range(1, 21):
    if i % 3 == 0:
        continue  # Skip this iteration if i is divisible by 3
    print(i, end=" ")

# ------------------------------------------------------------

# 3️⃣ Loop that stops when a negative number is entered
# Uses an infinite loop with 'break' to exit based on user input.
print("\n\nLoop that stops when a negative number is entered:")
while True:
    num = int(input("\nEnter a number (negative to stop): "))
    if num < 0:
        print("Negative number entered. Stopping the loop.")
        break  # Exit the loop
    print(f"You entered: {num}")
