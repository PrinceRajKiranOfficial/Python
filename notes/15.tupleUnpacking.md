## Tuple Unpacking in Python

Normally, we declare variables and then assign values. With tuple unpacking, we assign values to multiple variables at once.

### Example

```python
person = ("John", 25, "Developer")
name, age, profession = person

print(name)       # Output: John
print(age)        # Output: 25
print(profession) # Output: Developer
```

### Why Use Tuples Instead of Lists?
- **Semantic Meaning:** Tuples are used for heterogeneous (different) data, while lists are for homogeneous (similar) items.
- **Function Returns:** Tuples are commonly used to return multiple values from functions.
- **Performance:** Tuples are faster than lists.
- **Data Integrity:** Tuples are immutable, so data cannot be changed accidentally.
- **Dictionary Keys:** Tuples can be used as keys in dictionaries, unlike lists.