# 📘 Comprehensive Textbook Guide: Module 2 - Data Structures, Functions & Modules

## Chapter 5: Linear Data Structures - Lists and Tuples

### 5.1 Introduction to Data Structures
A data structure is a specialized format for organizing, processing, retrieving, and storing data. Python provides four built-in, highly optimized data structures: Lists, Tuples, Dictionaries, and Sets.

### 5.2 Lists
A List is an ordered, mutable (changeable) collection of elements. It can contain duplicate values and heterogeneous data types (e.g., integers, strings, and other lists mixed together). Internally, Python lists are implemented as **Dynamic Arrays**.

#### Creating Lists and Accessing Elements
Lists are created using square brackets `[]` or the `list()` constructor.
```python
my_list = [10, "Apple", 3.14, True]
print(my_list[0])    # Access first element: 10
print(my_list[-1])   # Access last element using negative indexing: True
```

#### List Slicing
Slicing allows you to extract a sublist. The syntax is `list[start : stop : step]`.
*   `start`: Starting index (inclusive). Defaults to 0.
*   `stop`: Ending index (exclusive). Defaults to length of list.
*   `step`: Amount by which the index increases. Defaults to 1.
```python
nums = [0, 10, 20, 30, 40, 50]
print(nums[1:4])     # [10, 20, 30]
print(nums[::2])     # [0, 20, 40] (Every second element)
print(nums[::-1])    # [50, 40, 30, 20, 10, 0] (Reverses the list)
```

#### Built-in List Functions/Methods
1.  **Adding Elements:**
    *   `append(item)`: Adds a single item to the end. Time complexity is $O(1)$.
    *   `insert(index, item)`: Inserts an item at a specific index. Shifts elements to the right $O(N)$.
    *   `extend(iterable)`: Appends elements from another iterable (like another list) to the end.
2.  **Removing Elements:**
    *   `remove(item)`: Removes the *first occurrence* of the specified item. Throws `ValueError` if not found.
    *   `pop(index)`: Removes and returns the item at the given index. If no index is specified, removes and returns the last item.
    *   `clear()`: Empties the entire list.
3.  **Other Operations:**
    *   `index(item)`: Returns the index of the first occurrence of the item.
    *   `count(item)`: Returns the number of times the item appears in the list.
    *   `sort(key=None, reverse=False)`: Sorts the list *in-place*.
    *   `reverse()`: Reverses the elements of the list *in-place*.

#### List Comprehension
A concise, highly optimized way to create lists from existing iterables.
**Syntax:** `[expression for item in iterable if condition]`
```python
# Create a list of squares for even numbers from 0 to 9
squares = [x**2 for x in range(10) if x % 2 == 0]
# Result: [0, 4, 16, 36, 64]
```

### 5.3 Tuples
Tuples are ordered collections, practically identical to lists, EXCEPT they are **Immutable** (they cannot be modified after creation). This immutability makes them faster than lists and allows them to be used as keys in dictionaries.

#### Creating and Accessing Tuples
Created using parentheses `()` or simply separating values by commas (Tuple Packing).
```python
t1 = (1, 2, 3)
t2 = 10, 20, 30      # Tuple Packing
t3 = (5,)            # A single-element tuple MUST have a trailing comma
```

#### Operations Using Built-in Tuple Functions
Since tuples cannot be modified (no `append`, `remove`, `sort`), they only support two main methods:
1.  `count(item)`: Returns occurrences of `item`.
2.  `index(item)`: Returns the first index of `item`.

*Note: You can concatenate tuples using `+` and repeat them using `*`, which creates a entirely new tuple.*

---

## Chapter 6: Non-Linear Data Structures - Dictionaries and Sets

### 6.1 Dictionaries
Dictionaries are mutable, dynamic collections that store data in **Key-Value pairs**. They are implemented as **Hash Tables**, making data retrieval extremely fast — $O(1)$ on average.
*Rules for Keys:* Keys must be immutable types (e.g., Strings, Numbers, Tuples). Lists or other dictionaries cannot be keys.

#### Creating and Accessing Values
```python
student = {"roll": 101, "name": "Alice", "marks": 95.5}

# Accessing
print(student["name"])          # Output: Alice (Throws KeyError if key is missing)
print(student.get("city", "N/A"))# Safe access. Returns "N/A" if "city" is missing.

# Adding / Updating
student["marks"] = 98           # Updates the existing key
student["grade"] = "O"          # Adds a new key-value pair
```

#### Built-in Dictionary Functions
*   `keys()`: Returns a view object of all keys.
*   `values()`: Returns a view object of all values.
*   `items()`: Returns a view object of tuple pairs `(key, value)`.
*   `pop(key)`: Removes the key and returns its value.
*   `popitem()`: Removes and returns the last inserted key-value pair.
*   `update(other_dict)`: Merges another dictionary into the current one.

### 6.2 Sets
A Set is an unordered, mutable collection of **unique** elements. It is highly optimized for checking membership and performing mathematical set operations.

#### Set Operations
```python
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

# Mathematical Operations
print(setA | setB) # Union: {1, 2, 3, 4, 5, 6}
print(setA & setB) # Intersection: {3, 4}
print(setA - setB) # Difference (in A, not in B): {1, 2}
print(setA ^ setB) # Symmetric Difference (in A or B, but not both): {1, 2, 5, 6}

# Set Methods
setA.add(9)        # Adds an element
setA.remove(1)     # Removes element. Throws KeyError if missing.
setA.discard(10)   # Safely removes element. Does nothing if missing.
```

---

## Chapter 7: Functions, Scope, and Recursion

### 7.1 Functions
A function is a block of organized, reusable code that performs a single, related action. It provides better modularity and code reusability. Defined using the `def` keyword.

#### Defining and Calling Functions
```python
def greet():              # Definition
    print("Hello World!")

greet()                   # Calling
```

#### Passing Arguments
1.  **Positional Arguments:** Arguments passed in the exact order as defined.
2.  **Keyword Arguments:** Arguments passed by explicitly naming the parameter, allowing you to ignore the order.
    ```python
    def display_info(name, age):
        print(f"Name: {name}, Age: {age}")
        
    display_info(age=25, name="John") # Keyword arguments
    ```
3.  **Default Arguments:** Parameters that assume a default value if a value is not provided in the function call.
    ```python
    def power(base, exponent=2):
        return base ** exponent
    ```

#### Variable-Length Arguments
Sometimes you don't know how many arguments will be passed.
*   `*args` (Non-Keyword Arguments): Gathers remaining positional arguments into a **Tuple**.
*   `**kwargs` (Keyword Arguments): Gathers remaining keyword arguments into a **Dictionary**.
```python
def student_data(name, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Scores (Tuple): {args}")
    print(f"Details (Dict): {kwargs}")

student_data("Alice", 90, 85, 88, city="NY", grade="A")
```

### 7.2 Scope of Variables (Local vs. Global)
*   **Local Variables:** Defined *inside* a function. They can only be accessed within that specific function.
*   **Global Variables:** Defined *outside* all functions. They can be read by any function in the module.
*   **The `global` Keyword:** If you want to *modify* a global variable from inside a function, you must declare it using the `global` keyword.
```python
count = 10  # Global variable

def increment():
    global count
    count += 1  # Modifying global variable

increment()
print(count)    # 11
```

### 7.3 Recursion
Recursion occurs when a function calls itself. A recursive function must have two parts:
1.  **Base Case:** A condition that stops the recursion to prevent an infinite loop (which causes a `RecursionError` or Stack Overflow).
2.  **Recursive Step:** The part where the function calls itself with a modified parameter moving towards the base case.
```python
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive step
```

### 7.4 Anonymous Functions (Lambda)
Functions without a name, created using the `lambda` keyword. They can take any number of arguments but can only have **one single expression**.
**Syntax:** `lambda arguments : expression`
```python
square = lambda x: x ** 2
print(square(5)) # 25
```
Lambdas are commonly used as arguments to higher-order functions like `map()`, `filter()`, and `sorted()`.

---

## Chapter 8: Modules and Packages

### 8.1 Modules
A module is simply a file containing Python definitions, functions, classes, and variables. The file name is the module name with the suffix `.py` appended.
*Why use modules?* They allow you to logically organize your Python code, grouping related code into a file, making it easier to understand and use.

#### The `import` Statement
You can bring a module's functionalities into your current script using `import`.
1.  **Importing entire module:**
    ```python
    import math
    print(math.sqrt(16))
    ```
2.  **Importing specific attributes:**
    ```python
    from math import pi, factorial
    print(pi)
    ```
3.  **Importing with an alias:**
    ```python
    import math as m
    print(m.pow(2, 3))
    ```

### 8.2 Creating Modules
You can create your own module by simply saving code in a `.py` file.
*File: `my_math.py`*
```python
def add(a, b):
    return a + b
```
*File: `main.py`*
```python
import my_math
print(my_math.add(5, 10))
```

### 8.3 Packages
A package is a hierarchical file directory structure that defines a single Python application environment containing modules, sub-packages, and so on.
To be recognized as a package, a directory MUST contain a special file named `__init__.py` (it can be completely empty).
```text
my_package/
    __init__.py
    module1.py
    module2.py
```
You can import from it using dot notation: `from my_package import module1`.

---

## 📝 Comprehensive Textbook Exercises and Solutions

### Conceptual Questions

**Q1. What is the difference between a List and a Tuple in Python?**
*Answer:* The primary difference is mutability. Lists are mutable (they can be modified, appended to, sorted in-place), whereas Tuples are immutable (once created, their elements cannot be changed, added, or removed). Lists use square brackets `[]`, and tuples use parentheses `()`. Because of immutability, tuples are generally faster and can be used as dictionary keys.

**Q2. Explain Dictionary Comprehension with an example.**
*Answer:* Similar to list comprehension, it's a concise way to create dictionaries. Syntax: `{key: value for item in iterable}`.
*Example:* `{x: x**2 for x in range(1, 4)}` creates `{1: 1, 2: 4, 3: 9}`.

**Q3. What is the Mutable Default Argument Trap?**
*Answer:* If you use a mutable object (like a list or dictionary) as a default argument in a function, it is evaluated ONLY ONCE when the function is defined. Subsequent calls to the function will share the exact same object in memory, leading to unexpected behavior.
*Fix:* Use `None` as the default, and initialize the list inside the function.

**Q4. Differentiate between `discard()` and `remove()` methods in Sets.**
*Answer:* Both remove an element from a set. However, if the element does not exist, `remove()` raises a `KeyError`, whereas `discard()` does nothing and the program continues execution.

**Q5. What is the purpose of `__init__.py` in a Python package?**
*Answer:* It tells the Python interpreter to treat the directory it resides in as a Python package. It can be empty, or it can execute initialization code for the package or set the `__all__` variable to control what gets imported when `from package import *` is used.

### Programming Problems

**P1. Write a function to remove duplicates from a list while preserving the original order.**
*Textbook Note: Simply converting to a `set` removes duplicates but destroys the order.*
```python
def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates_preserve_order([1, 2, 2, 3, 1, 4, 5, 4])) 
# Output: [1, 2, 3, 4, 5]
```

**P2. Write a recursive function to compute the Nth Fibonacci number.**
```python
def fibonacci(n):
    if n < 0:
        return "Incorrect input"
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        # Recursive step
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7)) # Output: 13
```

**P3. Write a program to count the frequency of each character in a string using a dictionary.**
```python
def count_char_frequency(s):
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

print(count_char_frequency("hello world"))
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

**P4. Write a lambda function to sort a list of tuples based on the second element of each tuple.**
```python
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

# Sort using a lambda function as the key
# x represents each tuple, so x[1] is the score
students.sort(key=lambda x: x[1], reverse=True)

print(students)
# Output: [('Bob', 92), ('Alice', 85), ('Charlie', 78)]
```

**P5. Write a function that accepts an arbitrary number of keyword arguments (`**kwargs`) and prints those whose values are integers.**
```python
def print_int_kwargs(**kwargs):
    for key, value in kwargs.items():
        if isinstance(value, int):
            print(f"{key}: {value}")

print_int_kwargs(name="Alice", age=25, city="NY", score=95)
# Output:
# age: 25
# score: 95
```
