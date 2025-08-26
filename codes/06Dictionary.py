student = {
    "name": "John",
    "age": 21,
    "courses": "Python"
}

print(student)
# Accessing values by key
print(student["name"])      # Output: John
print(student["courses"])   # Output: ['Python']
print(student.get("age"))   # Output: 21

# Adding or updating a value
student["age"] = 21
print(student)  # Output: {'name': 'John', 'age': 21, 'courses': ['Python']}

student["city"] = "Simri Bakhtiarpur"  # Add a new key-value pair
print(student)  # Output: {'name': 'John', 'age': 21, 'courses': ['Python'], 'city': 'Simri Bakhtiarpur'}

print(student.keys())    # Output: dict_keys(['name', 'age', 'courses', 'city'])
print(student.values())  # Output: dict_values(['John', 21, ['Python'], 'Simri Bakhtiarpur'])
print(student.items())   # Output: dict_items([('name', 'John'), ('age', 21), ('courses', ['Python']), ('city', 'Simri Bakhtiarpur')])

student.update({"age": 22, "gender": "Female"})  # Update existing and add new key-value pairs
print(student)  # Output: {'name': 'John', 'age': 22, 'courses': ['Python'], 'city': 'Simri Bakhtiarpur', 'gender': 'Female'}

student.pop("city")  # Remove a key-value pair by key
print(student)  # Output: {'name': 'John', 'age': 22, 'courses': ['Python'], 'gender': 'Female'}
