# 2. Logical Operators in Python

Logical operators are used to combine conditional statements.

| Operator | Description                               | Example          | Result  |
|----------|-------------------------------------------|------------------|---------|
| `and`    | Returns `True` if **both** conditions are `True` | `True and True`  | `True`  |
| `or`     | Returns `True` if **at least one** condition is `True` | `True or False` | `True`  |
| `not`    | Reverses the result (logical negation)    | `not True`       | `False` |

---

## Example Code

```python
# Using 'and' operator
print(True and True)   # Output: True
print(True and False)  # Output: False

# Using 'or' operator
print(True or False)   # Output: True
print(False or False)  # Output: False

# Using 'not' operator
print(not True)        # Output: False
print(not False)       # Output: True
