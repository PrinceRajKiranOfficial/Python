Email = input("Enter your email : ")

if "@" in Email and Email.endswith(".com"):
    print("Valid email address.")
else:
    print("Invalid email address.")
