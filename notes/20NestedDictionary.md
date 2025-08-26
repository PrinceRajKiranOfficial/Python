## Nested Dictionary Example

This example demonstrates how to use a nested dictionary in Python to store student information:

```python
students = {
    "101": {"name": "Tom", "grade": "A"},
    "102": {"name": "Jerry", "grade": "B"}
}

# Access the name of the student with ID "101"
print(students["101"]["name"])  # Output: Tom
```

- Each student ID maps to another dictionary containing their name and grade.
- You can access nested values using multiple keys.
