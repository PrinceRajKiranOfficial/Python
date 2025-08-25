## Python Collection Data Types

| Data Type | Description                       | Example                        |
|-----------|-----------------------------------|--------------------------------|
| `list`    | Ordered, changeable collection    | `colors = ["red", "blue"]`     |
| `tuple`   | Ordered, unchangeable collection  | `point = (10, 20)`             |
| `set`     | Unordered, no duplicates allowed  | `nums = {1, 2, 3}`             |
| `dict`    | Key-value pairs                   | `person = {"name": "Sam"}`     |

### Set Example

```python
a = {1, 2, 3, 1, 2, 3}
print(a)  # Output: {1, 2, 3}

b = {'a', 'b', 'c', 'a', 'b', 'c'}
print(b)  # Output: {'a', 'b', 'c'}
```

> Sets automatically remove duplicate elements.

### Note

- Lists and tuples are similar to arrays.
- Arrays usually store homogeneous elements (same data type).
- Python lists and tuples can store heterogeneous elements.


list and tuple will store heterogenous element 
- Both `list` and `tuple` can store elements of different types, such as integers, strings, and even other collections.

#### Example

```python
mixed_list = [1, "apple", 3.14, [2, 3]]
mixed_tuple = (True, 42, "banana", (5, 6))
print(mixed_list)
print(mixed_tuple)
```