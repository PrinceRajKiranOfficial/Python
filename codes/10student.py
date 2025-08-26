marks = input("Enter your marks ✌️✌️: ")
# using int we can stor only integer value but using float we can stroe both integer and decimal value
if marks.replace(".", "", 1).isdigit():
    marks = float(marks)
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
else:
    print("Invalid input. Please enter a number.")
