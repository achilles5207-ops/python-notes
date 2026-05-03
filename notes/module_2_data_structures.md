# 📘 The Ultimate Master Guide: Module 2 - Data Structures, Functions & Modules

---

## 📚 Section 1: Data Structures - Lists
A List is an ordered, mutable (changeable) collection of elements. It can contain duplicate values and heterogeneous data types (integers, strings, etc., mixed together).
Under the hood, Lists are **Dynamic Arrays**.

### List Creation and Accessing
```python
my_list = [10, "Apple", 3.14, True]
print(my_list[1])    # Output: Apple
print(my_list[-1])   # Output: True (Negative indexing accesses from the end)
```

### List Slicing
Extracting a portion of the list. `list[start:stop:step]`.
```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])     # [1, 2, 3]
print(nums[::-1])    # [5, 4, 3, 2, 1, 0] (Reverses the list)
```

### Built-in List Functions/Methods
- **Adding elements:**
  - `append(x)`: Adds `x` to the end of the list. O(1) time complexity.
  - `insert(i, x)`: Inserts `x` at index `i`. O(N) because elements shift right.
  - `extend(iterable)`: Appends elements from another iterable.
- **Removing elements:**
  - `remove(x)`: Removes the first occurrence of value `x`.
  - `pop(i)`: Removes and returns the element at index `i` (defaults to last element).
  - `clear()`: Removes all items.
- **Other utilities:**
  - `index(x)`: Returns the first index of `x`.
  - `count(x)`: Returns the number of times `x` appears.
  - `sort()`: Sorts the list in ascending order *in-place*.
  - `reverse()`: Reverses the elements *in-place*.

### List Comprehension
An elegant way to create new lists based on existing iterables.
```python
# Create a list of squares for even numbers only
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares) # [0, 4, 16, 36, 64]
```

---

## 📦 Section 2: Data Structures - Tuples
Tuples are ordered collections, identical to lists, EXCEPT they are **Immutable** (cannot be modified after creation).
Because of immutability, Tuples are faster than Lists and can be used as keys in Dictionaries.

### Tuple Creation and Operations
```python
t1 = (1, 2, 3)
t2 = 1, 2, 3       # Parentheses are optional (Tuple Packing)
single_tuple = (5,)# MUST have a comma, otherwise it's just an int

# Unpacking
a, b, c = t1       # a=1, b=2, c=3
```
- **Built-in Functions:** Tuples only support `count()` and `index()` because they cannot be modified.

---

## 📖 Section 3: Data Structures - Dictionaries
Dictionaries are unordered (ordered in Python 3.7+), mutable collections of Key-Value pairs. They are implemented using **Hash Tables**, making lookups O(1) fast.
**Rules for Keys:** Keys must be Immutable (Strings, Numbers, Tuples). Lists cannot be keys.

### Accessing and Modifying
```python
student = {"name": "John", "age": 20, "grades": [90, 85]}

# Accessing
print(student["name"])          # Output: John (Throws KeyError if key doesn't exist)
print(student.get("city", "NY"))# Safe access. Returns "NY" if "city" is not found.

# Adding / Updating
student["age"] = 21             # Updates age
student["city"] = "Boston"      # Adds new key-value pair
```

### Built-in Dictionary Functions
- `keys()`: Returns a view object of all keys.
- `values()`: Returns a view object of all values.
- `items()`: Returns a view object of (key, value) tuples.
- `pop(key)`: Removes the specified key and returns its value.
- `update(dict2)`: Merges dict2 into the dictionary.

---

## 🎯 Section 4: Data Structures - Sets
A Set is an unordered collection of **unique** elements. It is heavily used for mathematical set operations and removing duplicates from a list.

### Set Operations
```python
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

print(setA | setB) # Union: {1, 2, 3, 4, 5, 6}
print(setA & setB) # Intersection: {3, 4}
print(setA - setB) # Difference: {1, 2} (In A, but not B)
print(setA ^ setB) # Symmetric Difference: {1, 2, 5, 6} (In either, but not both)

setA.add(9)        # Adds 9
setA.discard(10)   # Safely removes 10 (does not throw error if 10 isn't there)
```

---

## ⚙️ Section 5: Functions, Recursion, and Anonymous Functions

### Functions
Blocks of reusable code defined using the `def` keyword.
- **Positional vs Keyword Arguments:**
  ```python
  def greet(name, msg):
      print(f"{msg}, {name}")

  greet("Alice", "Hi")          # Positional
  greet(msg="Hello", name="Bob")# Keyword (Order doesn't matter)
  ```
- **Default Arguments:** `def greet(name, msg="Hello"):`

### Variable Length Arguments (`*args` and `**kwargs`)
- `*args`: Collects extra positional arguments into a Tuple.
- `**kwargs`: Collects extra keyword arguments into a Dictionary.
```python
def info(*args, **kwargs):
    print("Args tuple:", args)
    print("Kwargs dict:", kwargs)

info(1, 2, 3, name="Alice", age=25)
```

### Recursion
A function calling itself. Must have a base condition to prevent infinite loops (StackOverflow).
```python
def factorial(n):
    if n == 0 or n == 1: # Base Case
        return 1
    else:                # Recursive Step
        return n * factorial(n - 1)
```

### Anonymous Functions (Lambda)
Functions without a name, created using the `lambda` keyword. Used for small, one-line operations.
**Syntax:** `lambda arguments: expression`
```python
square = lambda x: x * x
print(square(5)) # Output: 25

# Often used with map/filter
nums = [1, 2, 3, 4]
doubles = list(map(lambda x: x * 2, nums))
```

---

## 📁 Section 6: Modules and Packages

### Modules
A module is simply a Python file containing variables, functions, and classes. It allows you to logically organize your code.
- **Importing:**
  ```python
  import math
  print(math.sqrt(16))
  
  from math import pi, factorial
  print(pi)
  ```

### Packages
A package is a folder that contains multiple modules and a special `__init__.py` file. The `__init__.py` file tells the Python interpreter to treat the folder as a package.

---

## 🛠️ Section 7: Essential Built-in Modules & Advanced Sorting (Lab Prerequisites)
To solve complex problems (like those in your labs), you must know these built-in functionalities:

### The `math` Module
Crucial for algorithms like finding prime numbers or simplifying fractions.
```python
import math
print(math.gcd(10, 15))       # Greatest Common Divisor: 5
print(math.hypot(3, 4))       # Distance from origin (Pythagorean): 5.0
```

### Advanced Slicing and String Methods
- **Slicing by Steps:** `tup[::2]` gets every alternate element (e.g., removing elements at odd indices by keeping only even indices).
- **String Case Counting:**
```python
s = "Hello World"
upper_count = sum(1 for char in s if char.isupper())
lower_count = sum(1 for char in s if char.islower())
```

### Sorting Collections of Collections
How to sort a list of tuples based on the 3rd element of each tuple:
```python
students = [("Alice", 20, 85), ("Bob", 19, 90), ("Charlie", 21, 80)]
# Sort descending by the 3rd element (index 2, which is marks)
students.sort(key=lambda x: x[2], reverse=True)
```

---

## 📝 EXAM QUESTION BANK & SOLUTIONS

**Q1. How do you remove duplicates from a list in one line of code?**
```python
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list) # [1, 2, 3, 4, 5]
```

**Q2. Explain the Mutable Default Argument Trap in Python with an example.**
**Answer:** Default arguments are evaluated ONLY ONCE when the function is defined, not every time it's called. If the default argument is mutable (like a list), subsequent calls to the function will share the same list object.
```python
def append_item(item, target=[]):
    target.append(item)
    return target

print(append_item(1)) # Output: [1]
print(append_item(2)) # Output: [1, 2] (Error! It didn't start with a fresh list!)
# Fix: Use target=None, and initialize target=[] inside the function.
```

**Q3. Write a recursive function to find the sum of a list of numbers.**
```python
def recursive_sum(num_list):
    if len(num_list) == 0:
        return 0
    else:
        return num_list[0] + recursive_sum(num_list[1:])

print(recursive_sum([1, 2, 3, 4])) # Output: 10
```

**Q4. Write a program to merge two dictionaries.**
```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Method 1 (Python 3.5+ unpacking)
merged = {**dict1, **dict2}

# Method 2 (Python 3.9+ union operator)
merged_new = dict1 | dict2
print(merged)
```

**Q5. What is the output of `x = (1, 2, 3); x[0] = 5`?**
**Answer:** It throws a `TypeError: 'tuple' object does not support item assignment`. Tuples are immutable and their elements cannot be changed after creation.

**Q6. Write a list comprehension that extracts all words starting with 'p' from a given string.**
```python
text = "python is powerful and programming is fun"
p_words = [word for word in text.split() if word.startswith('p')]
print(p_words) # ['python', 'powerful', 'programming']
```

**Q7. Differentiate between `append()` and `extend()` list methods.**
**Answer:** `append(item)` adds its argument as a *single element* to the end of the list. `extend(iterable)` iterates over its argument adding *each element* to the list.
```python
lst = [1, 2]
lst.append([3, 4]) # [1, 2, [3, 4]]
lst.extend([5, 6]) # [1, 2, [3, 4], 5, 6]
```

**Q8. Write a function that accepts any number of arguments and returns their product.**
```python
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply_all(2, 3, 4)) # Output: 24
```

**Q9. How do you sort a dictionary by its values instead of keys?**
```python
marks = {'Physics': 67, 'Maths': 87, 'History': 75}
# Sort using a lambda function targeting the value (item[1])
sorted_marks = dict(sorted(marks.items(), key=lambda item: item[1]))
print(sorted_marks) # {'Physics': 67, 'History': 75, 'Maths': 87}
```

**Q10. Explain what `*args` and `**kwargs` are.**
**Answer:** They are conventions used to pass a variable number of arguments to a function. `*args` is used to pass a non-keyworded, variable-length argument list (passed as a tuple). `**kwargs` is used to pass a keyworded, variable-length argument list (passed as a dictionary).
