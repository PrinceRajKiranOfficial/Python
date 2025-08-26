temp = input("Enter temperature in Celsius: ")
if temp.replace(".", "", 1).isdigit():
    temp = float(temp)
    if temp > 45:  
        print("It is hot")
    elif temp > 30:
        print("It is warm")
    elif temp > 15:
        print("It is cool")
    else:
        print("It is cold")
else:
    print("Invalid input. Please enter a number.")
