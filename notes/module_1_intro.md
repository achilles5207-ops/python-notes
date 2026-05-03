# 📘 The Ultimate Master Guide: Module 1 - Introduction to Python

---

## 📖 Section 1: Introduction to Python
Python is a widely-used, interpreted, object-oriented, and high-level programming language with dynamic semantics. Created by **Guido van Rossum** and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant indentation.

### Why Learn Python?
1. **Data Science & AI:** It is the undisputed king of machine learning (TensorFlow, PyTorch) and data analysis (Pandas, NumPy).
2. **Web Development:** Frameworks like Django and Flask power massive websites (e.g., Instagram, Spotify).
3. **Automation:** Python scripts are universally used to automate repetitive OS tasks.

---

## 🌟 Section 2: Features of Python
Python is packed with features that make it a favorite among developers:

1. **Simple and Easy to Learn:** Python has a very simple and elegant syntax. It reads almost like English.
2. **Freeware and Open Source:** You can download it for free, and its source code is open for modification.
3. **High-Level Language:** Programmers don't need to remember system architecture or manage memory manually.
4. **Platform Independent:** "Write Once, Run Anywhere". The Python Virtual Machine (PVM) interprets bytecode so the same `.py` file runs on Windows, Mac, and Linux.
5. **Dynamically Typed:** In C or Java, you must declare `int x = 10;`. In Python, you just write `x = 10`. The interpreter determines the type at runtime.
6. **Interpreted Language:** Code is executed line-by-line. If there's an error on line 10, lines 1-9 will still run successfully before the program crashes.
7. **Extensive Standard Library:** "Batteries included" philosophy. Python comes with modules for regex, databases, unit testing, and web scraping right out of the box.

---

## 🔤 Section 3: Identifiers, Keywords, and Variables

### Identifiers
Identifiers are names given to entities like variables, functions, and classes.
**Rules for Identifiers:**
- Must start with a letter (A-Z, a-z) or an underscore (`_`).
- Can contain letters, numbers, and underscores.
- **Cannot** start with a number (e.g., `1variable` is invalid).
- **Cannot** be a keyword.
- Case-sensitive (`Age` and `age` are different).

### Keywords
Keywords are reserved words that have special meaning to the interpreter. You cannot use them as variable names.
You can view all keywords using:
```python
import keyword
print(keyword.kwlist)
# Output includes: False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield.
```

### Variables and Memory Management
Variables are simply **references** (pointers) to objects in memory.
```python
a = 10
b = 10
print(id(a)) # Gets memory address: e.g., 140734260340800
print(id(b)) # Exactly the SAME address because Python caches small integers!
```

---

## 📦 Section 4: Data Types and Literals

Python provides several built-in data types.

### 1. Numeric Types
- **`int` (Integer):** Whole numbers. Can be represented in Decimal (Base 10), Binary (`0b1010`), Octal (`0o12`), or Hexadecimal (`0xA`). Python integers have arbitrary precision (no maximum limit).
- **`float` (Floating Point):** Decimal numbers. Can use scientific notation: `1.2e3` represents `1200.0`.
- **`complex` (Complex Numbers):** Written as `real + imag j`. e.g., `c = 3 + 4j`.

### 2. Boolean (`bool`)
Represents `True` or `False`. Internally, `True` is treated as `1` and `False` as `0`.
```python
print(True + True) # Output: 2
```

### 3. Strings (`str`)
A sequence of characters enclosed in quotes.
- Single line: `'Hello'` or `"Hello"`
- Multi-line: `'''Hello World'''`
- **Escape Characters:** `\n` (newline), `\t` (tab), `\\` (backslash).
- **Raw Strings:** Prefix with `r` to ignore escape characters. `r"C:\new_folder"`
- **f-Strings:** Used for formatting. `f"My age is {age}"`.

### Type Casting (Explicit Conversion)
Converting one data type to another.
```python
print(int(3.14))    # Output: 3 (Truncates decimal)
print(float(5))     # Output: 5.0
print(bool(0))      # Output: False (0, empty strings, empty lists are False)
print(str(100))     # Output: "100"
```

---

## 📥 Section 5: Input and Output Statements

### Output (`print`)
The `print()` function displays data to the console.
**Syntax:** `print(*objects, sep=' ', end='\n')`
```python
print("Apple", "Banana", "Cherry", sep=" | ", end="!!!\n")
# Output: Apple | Banana | Cherry!!!
```

### Input (`input`)
Reads a line from the console as a **String**.
```python
age = int(input("Enter age: ")) # Must cast to int if you want to do math
```

### Taking Multiple Inputs
```python
x, y = input("Enter two numbers: ").split() # Assumes space separation
```

---

## 🧮 Section 6: Operators, Precedence, and Associativity

### 1. Arithmetic Operators
- `+` (Addition), `-` (Subtraction), `*` (Multiplication)
- `/` (True Division): ALWAYS returns a float. `10 / 2` is `5.0`.
- `//` (Floor Division): Returns an integer, rounded DOWN. `-10 // 3` is `-4`.
- `%` (Modulus): Returns the remainder. `10 % 3` is `1`.
- `**` (Exponentiation): `2 ** 3` is `8`.

### 2. Relational / Comparison Operators
Return Boolean values.
- `<`, `>`, `<=`, `>=`, `==` (Equal to), `!=` (Not equal to).

### 3. Logical Operators (Short-Circuiting)
- `and`: Returns True if BOTH are True. (If first is False, second is NOT evaluated).
- `or`: Returns True if AT LEAST ONE is True. (If first is True, second is NOT evaluated).
- `not`: Reverses the boolean state.

### 4. Bitwise Operators
Operate on the binary representations of numbers.
- `&` (Bitwise AND), `|` (Bitwise OR), `^` (Bitwise XOR)
- `~` (Bitwise NOT): Mathematically `~x` equals `-(x + 1)`.
- `<<` (Left Shift): Shifts bits left. Effectively multiplies by $2^n$.
- `>>` (Right Shift): Shifts bits right. Effectively divides by $2^n$.

### 5. Identity and Membership Operators
- **Identity (`is`, `is not`):** Checks if two variables point to the EXACT SAME memory location.
- **Membership (`in`, `not in`):** Checks if a sequence contains a value.
```python
print("y" in "Python") # True
```

### Operator Precedence (Highest to Lowest)
1. `()` Parentheses
2. `**` Exponentiation
3. `+x, -x, ~x` Unary plus/minus/bitwise NOT
4. `*, /, //, %` Multiplication/Division/Modulus
5. `+, -` Addition/Subtraction
6. `<<, >>` Bitwise Shifts
7. `&` Bitwise AND
8. `^` Bitwise XOR
9. `|` Bitwise OR
10. `==, !=, >, >=, <, <=, is, is not, in, not in` Comparisons/Identity/Membership
11. `not` Logical NOT
12. `and` Logical AND
13. `or` Logical OR

*Associativity is mostly Left-to-Right, EXCEPT for Exponentiation `**` which is Right-to-Left.*

---

## 🔀 Section 7: Control Statements

### Conditional Statements
Used for decision making.
```python
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")
```

### Looping Statements
**`while` Loop:** Executes as long as condition is True.
```python
count = 5
while count > 0:
    print(count)
    count -= 1
```

**`for` Loop:** Iterates over a sequence (string, list, tuple, range).
```python
for i in range(1, 10, 2): # Start 1, Stop 10 (exclusive), Step 2
    print(i) # Prints 1, 3, 5, 7, 9
```

### Loop Control
- `break`: Exits the loop entirely.
- `continue`: Skips the remaining code in the current iteration and jumps to the next iteration.
- `pass`: A null statement. Used to create empty blocks without getting a syntax error.

### The `else` block with Loops
Unique to Python. The `else` block executes ONLY if the loop finishes normally (without hitting a `break`).
```python
for num in range(5):
    if num == 3:
        break
    print(num)
else:
    print("This will NOT print because the loop broke.")
```

---

## 📝 EXAM QUESTION BANK & SOLUTIONS

**Q1. Explain the difference between `==` and `is`.**
**Answer:** `==` is an equality operator that checks if the *values* of two objects are the same. `is` is an identity operator that checks if two variables point to the *exact same object in memory* (i.e., they have the same `id()`).

**Q2. Write a Python program to swap two variables without using a temporary variable.**
```python
x = 10
y = 20
x, y = y, x # Tuple unpacking
print(f"x={x}, y={y}") # x=20, y=10
```

**Q3. Write a program to find if a given number is an Armstrong number.**
*Explanation: An Armstrong number of 3 digits is an integer such that the sum of the cubes of its digits is equal to the number itself.*
```python
num = int(input("Enter number: "))
sum_of_cubes = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //= 10

if num == sum_of_cubes:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
```

**Q4. Predict the output of `-15 // 4` and explain why.**
**Answer:** The output is `-4`. The `//` operator performs Floor Division. `-15 / 4` is `-3.75`. The floor of a number is the largest integer less than or equal to it. The next integer less than `-3.75` is `-4`.

**Q5. Write a program to print the Fibonacci series up to `n` terms.**
```python
n = int(input("Enter number of terms: "))
n1, n2 = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence:", n1)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
```

**Q6. What will be the output of `print(bool("False"))`?**
**Answer:** `True`. Any non-empty string evaluates to `True` in Python, even if the string's content spells the word "False".

**Q7. Write a program to calculate the factorial of a number using a loop.**
```python
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial}")
```

**Q8. What is the `pass` statement in Python? Give an example.**
**Answer:** It is a null operation. It serves as a placeholder when a statement is required syntactically but you do not want any command or code to execute.
```python
def future_function():
    pass # Will be implemented later. Prevents IndentationError.
```

**Q9. Write a program to reverse a given integer.**
```python
num = int(input("Enter integer: "))
reversed_num = 0
while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num = num // 10
print(f"Reversed number is: {reversed_num}")
```

**Q10. Explain Short-Circuit Evaluation.**
**Answer:** It is a mechanism where the second argument in a logical `and` or `or` expression is only evaluated if the first argument does not determine the overall value. For `A and B`, if `A` is False, `B` is not evaluated (result is False). For `A or B`, if `A` is True, `B` is not evaluated (result is True).
