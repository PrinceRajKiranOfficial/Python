# Different Ways to Import Modules in Python

This document demonstrates various ways to import modules in Python, with short explanations and examples.

## 1. Import full module
You can import the entire module and then use its functions with the module name as a prefix.
```python
import random
print(random.randint(1, 10))
```
*Example:* Here, we import the `random` module and use `random.randint()` to generate a random integer between 1 and 10.

## 2. Import specific function
Instead of importing the entire module, you can import only the function you need.
```python
from math import sqrt
print(sqrt(25))
```
*Example:* We import only the `sqrt` function from the `math` module and use it directly without prefixing it with `math.`.

## 3. Import with alias
Modules can be imported with an alias to shorten their names when used in the code.
```python
import datetime as dt
print(dt.datetime.now())
```
*Example:* The `datetime` module is imported as `dt`. This makes the code shorter and often more readable.

## 4. Import all functions from a module
```python
from math import *
print(sqrt(25))
print(factorial(5))
```
*Example:* Here, we import all functions from the `math` module, allowing us to use them directly without any prefix.