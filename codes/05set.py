'''# Demonstrating set operations in Python

# Sets automatically remove duplicate elements
a = {'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd'}
print(a)  # Output: {'a', 'b', 'c', 'd'} (order is not guaranteed; e.g., could be {'d', 'b', 'a', 'c'})

b = {1, 2, 3, 4, 5, 2, 3, 4, 1}
print(b)  # Output: {1, 2, 3, 4, 5}

# add() adds an element to the set
b.add(6)
print(b)  # Output: {1, 2, 3, 4, 5, 6}

# remove() deletes an element from the set; raises KeyError if the element is not found
b.remove(3)
print(b)  # Output: {1, 2, 4, 5, 6}
# b.remove(10)  # Uncommenting this line will raise a KeyError since 10 is not in the set

# discard() deletes an element from the set; does NOT raise an error if the element is not found
b.discard(3)  # 3 is not in the set, so nothing happens
print(b)      # Output: {1, 2, 4, 5, 6}
b.discard(3)  # Still does nothing
print(b)      # Output: {1, 2, 4, 5, 6}

# Check for existence of an element in the set
print(3 in b)       # Output: False
print(10 in b)      # Output: False
print(10 not in b)  # Output: True

# Get the number of elements in the set
print(len(b))  # Output: 5
'''


# Demonstrating how to add elements to a set in Python
x = {1, 2, 3, 4}

# The add() method adds a single element to the set
x.add(5)
print(x)  # Output: {1, 2, 3, 4, 5}

# x.add(6, 7)  # This will raise a TypeError because add() accepts only one argument

# The update() method adds multiple elements to the set from an iterable
x.update([6, 7, 8])
print(x)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# x.update(9, 10)  # This will raise a TypeError because update() expects a single iterable argument

y = x.copy()  # Creates a shallow copy of the set x
print(y)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# The pop() method removes and returns a random element from the set
y.pop()
print(x)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(y)  # Output: {remaining 7 elements after pop}

# Demonstrating set operations in Python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))              # Output: {1, 2, 3, 4, 5, 6}
print(a | b)                   # Output: {1, 2, 3, 4, 5, 6}

print(a.intersection(b))       # Output: {3, 4}
print(a & b)                   # Output: {3, 4}

print(a.difference(b))         # Output: {1, 2}
print(a - b)                   # Output: {1, 2}

print(b.difference(a))         # Output: {5, 6}
print(b - a)                   # Output: {5, 6}

print(a.symmetric_difference(b))  # Output: {1, 2, 5, 6}
print(a ^ b)                      # Output: {1, 2, 5, 6}
                

# frozen set: immutable set
a = frozenset([1, 2, 3, 4, 5])
print(a)  # Output: frozenset({1, 2, 3, 4, 5})
# a.add(6)  # This will raise an AttributeError because frozenset is immutable
# a.remove(3)  # This will also raise an AttributeError because frozenset is immutable
print(type(a))  # Output: <class 'frozenset'>



x.clear()
print(x)  # Output: set()