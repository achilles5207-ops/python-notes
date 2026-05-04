# 📘 Comprehensive Textbook Guide: Module 1 - Introduction to Python & Control Structures

## Chapter 1: Introduction to Problem Solving and Python

### 1.1 Problem Solving Basics
Before diving into any programming language, it's crucial to understand how to solve problems computationally. Problem solving involves:
1.  **Understanding the Problem:** Clearly define what needs to be solved.
2.  **Devising a Plan (Algorithm):** Creating a step-by-step procedure to solve the problem.
3.  **Executing the Plan (Coding):** Translating the algorithm into a programming language like Python.
4.  **Testing and Debugging:** Verifying that the code works correctly for all edge cases.

#### Algorithms
An algorithm is a finite, ordered sequence of unambiguous instructions that results in a solution to a specific problem.
*Characteristics of a good algorithm:*
*   **Finiteness:** Must terminate after a finite number of steps.
*   **Definiteness:** Each step must be precisely defined.
*   **Input:** Should have zero or more inputs.
*   **Output:** Must produce at least one output.
*   **Effectiveness:** Each operation must be basic enough to be carried out exactly and in a finite length of time.

#### Flowcharts and Pseudocode
*   **Flowchart:** A visual representation of an algorithm using standard symbols (ovals for start/stop, parallelograms for input/output, rectangles for processing, diamonds for decision making).
*   **Pseudocode:** An informal high-level description of the operating principle of a computer program or algorithm. It uses structural conventions of normal programming languages but is intended for human reading.

### 1.2 Introduction to Python
Python is a high-level, interpreted, general-purpose programming language. Created by **Guido van Rossum** and first released in 1991, Python's design philosophy emphasizes code readability with its use of significant indentation.

#### Why Python?
*   Readability and maintainability.
*   Multiple programming paradigms supported (Object-oriented, procedural, functional).
*   Compatible with major platforms and systems.
*   Robust standard library.

### 1.3 Features of Python
1.  **Simple and Easy to Learn:** Python has a relatively few keywords, simple structure, and a clearly defined syntax.
2.  **Freeware and Open Source:** Python can be freely downloaded and its source code is openly available.
3.  **High-Level Language:** It abstracts away system-level details like memory management (handled by Python's Garbage Collector).
4.  **Dynamically Typed:** You don't need to declare the type of a variable. The type is determined at runtime (e.g., `x = 10` automatically makes `x` an integer).
5.  **Interpreted Language:** Python code is processed at runtime by the interpreter. You do not need to compile your program before executing it.
6.  **Platform Independent (Cross-Platform):** Python code can run on Windows, macOS, Linux, etc., without any modification ("Write Once, Run Anywhere").
7.  **Object-Oriented:** Python supports OOP concepts like classes, inheritance, and encapsulation.
8.  **Extensive Standard Library:** It provides a rich set of modules and functions for tasks ranging from regular expressions to web servers.

---

## Chapter 2: Python Fundamentals

### 2.1 Character Set, Identifiers, and Keywords
#### Character Set
Python supports the standard ASCII and Unicode character sets, allowing representation of almost any character from worldwide languages.

#### Keywords
Keywords are reserved words that convey a special meaning to the Python interpreter. They cannot be used as variable names, function names, or any other identifier.
*Examples:* `True`, `False`, `None`, `if`, `else`, `elif`, `for`, `while`, `break`, `continue`, `def`, `class`, `import`, `return`, `and`, `or`, `not`, `try`, `except`.
(Note: All keywords are lowercase except `True`, `False`, and `None`).

#### Identifiers
An identifier is a name given to entities like variables, functions, classes, etc.
*Rules for naming identifiers:*
1.  Must begin with a letter (A-Z, a-z) or an underscore (`_`).
2.  Followed by zero or more letters, underscores, and digits (0-9).
3.  Cannot be a reserved keyword.
4.  No special characters (like `!`, `@`, `#`, `$`, `%`) are allowed.
5.  Case-sensitive (`Age` and `age` are distinct).

### 2.2 Variables and Memory Allocation
A variable is a named memory location used to store data. In Python, variables are essentially **references** or labels attached to objects in memory.
```python
x = 10      # Creates an integer object 10 and binds the label 'x' to it.
y = "Hello" # Creates a string object "Hello" and binds 'y' to it.
```
**Dynamic Typing in Action:**
```python
a = 5       # 'a' is an integer
a = "Test"  # Now 'a' references a string (perfectly legal in Python)
```

### 2.3 Data Types
Python provides several built-in data types. Everything in Python is an object, meaning data types are actually classes.

#### 1. Numeric Types
*   **Integer (`int`):** Whole numbers, positive or negative, without decimals. Python 3 handles arbitrarily large integers.
    *   *Examples:* `10`, `-500`, `9999999999999999`
*   **Floating-Point (`float`):** Real numbers with a decimal point. They can also be written in scientific notation.
    *   *Examples:* `3.14`, `-0.001`, `2.5e2` (which is $2.5 \\times 10^2 = 250.0$)
*   **Complex Numbers (`complex`):** Numbers with a real and an imaginary part, written as `x + yj`.
    *   *Example:* `z = 3 + 4j` (where `z.real` is `3.0` and `z.imag` is `4.0`)

#### 2. Boolean Type (`bool`)
Represents truth values: `True` or `False`. Internally, Python treats `True` as `1` and `False` as `0`.

#### 3. Sequence Types (Basic Introduction)
*   **String (`str`):** A contiguous set of characters represented in quotes.
    *   *Single quotes:* `'Hello'`
    *   *Double quotes:* `"World"`
    *   *Triple quotes (for multiline):* `'''Multi-line string'''`

### 2.4 Literals
Literals are the raw data assigned to variables or constants.
1.  **Numeric Literals:** Immutable numeric values (e.g., `10`, `3.14`). Numbers can be binary (`0b1010`), octal (`0o12`), or hex (`0xA`).
2.  **String Literals:** Text in quotes.
3.  **Boolean Literals:** `True` and `False`.
4.  **Special Literal `None`:** Represents the absence of a value or a null value.

---

## Chapter 3: Operators, Expressions, and I/O

### 3.1 Input and Output Statements
#### Output with `print()`
Used to display information to the standard output device (screen).
**Syntax:** `print(*objects, sep=' ', end='\\n')`
*   `sep`: Defines the separator between multiple objects (default is space).
*   `end`: Defines what is printed at the very end (default is a newline `\\n`).

```python
print("Hello", "World", sep="-", end="***")
# Output: Hello-World***
```

#### Formatting Strings
1.  **f-strings (Formatted String Literals):** (Python 3.6+)
    ```python
    name = "Alice"
    age = 20
    print(f"My name is {name} and I am {age} years old.")
    ```
2.  **`format()` method:**
    ```python
    print("My name is {} and I am {} years old.".format(name, age))
    ```

#### Input with `input()`
Used to read a string from standard input.
```python
user_name = input("Enter your name: ")
```
*Note:* `input()` ALWAYS returns a string. If you need an integer or float, you must explicitly type cast it.
```python
age = int(input("Enter your age: ")) # Type casting string to int
```

### 3.2 Operators
Operators are special symbols that carry out arithmetic or logical computation. The values they operate on are called operands.

#### 1. Arithmetic Operators
*   `+` (Addition): Adds two operands.
*   `-` (Subtraction): Subtracts right operand from left.
*   `*` (Multiplication): Multiplies two operands.
*   `/` (Division): Divides left by right operand (ALWAYS returns a float).
*   `//` (Floor Division): Divides and returns the integer part (rounds towards minus infinity).
*   `%` (Modulus): Returns the remainder of division.
*   `**` (Exponentiation): `x ** y` means x to the power of y.

#### 2. Relational (Comparison) Operators
Compare values and return a Boolean (`True` or `False`).
*   `==` (Equal to)
*   `!=` (Not equal to)
*   `>` (Greater than), `<` (Less than)
*   `>=` (Greater than or equal to), `<=` (Less than or equal to)

#### 3. Logical Operators
Used to combine conditional statements.
*   `and`: Returns `True` if both operands are true.
*   `or`: Returns `True` if at least one operand is true.
*   `not`: Reverses the boolean state of its operand.
*(Note: Python uses Short-Circuit Evaluation. In `A and B`, if A is False, B is not evaluated.)*

#### 4. Assignment Operators
Used to assign values to variables.
*   Simple: `=`
*   Compound: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` (e.g., `x += 5` is equivalent to `x = x + 5`)

#### 5. Bitwise Operators
Operate bit by bit on integers.
*   `&` (Bitwise AND): Sets bit to 1 if both bits are 1.
*   `|` (Bitwise OR): Sets bit to 1 if one of two bits is 1.
*   `^` (Bitwise XOR): Sets bit to 1 if only one of two bits is 1.
*   `~` (Bitwise NOT): Inverts all the bits. Mathematically, `~x` is `-(x+1)`.
*   `<<` (Left Shift): Shifts bits to the left, adding zeros. (Multiplies by 2^n).
*   `>>` (Right Shift): Shifts bits to the right. (Divides by 2^n).

#### 6. Identity and Membership Operators
*   **Identity (`is`, `is not`):** Checks if two variables point to the *exact same object in memory* (same memory address).
    ```python
    x = [1, 2, 3]
    y = [1, 2, 3]
    print(x is y) # False, they are different objects with the same values.
    print(x == y) # True, their values are the same.
    ```
*   **Membership (`in`, `not in`):** Tests for membership in a sequence (string, list, tuple, etc.).
    ```python
    print('a' in 'apple') # True
    ```

### 3.3 Precedence and Associativity
When an expression has multiple operators, precedence determines which operator is evaluated first.
*Highest to Lowest Precedence:*
1.  `()` Parentheses
2.  `**` Exponentiation (Note: Associates Right-to-Left)
3.  `+x, -x, ~x` Unary Plus, Unary Minus, Bitwise NOT
4.  `*, /, //, %` Multiplication, Division, Floor Division, Modulus
5.  `+, -` Addition, Subtraction
6.  `<<, >>` Bitwise Shifts
7.  `&` Bitwise AND
8.  `^` Bitwise XOR
9.  `|` Bitwise OR
10. `==, !=, >, >=, <, <=, is, is not, in, not in` Comparisons, Identity, Membership
11. `not` Logical NOT
12. `and` Logical AND
13. `or` Logical OR

**Associativity:** If operators have the same precedence, associativity determines the order of evaluation. Almost all operators associate **Left-to-Right** (e.g., `10 - 4 - 2` is evaluated as `(10 - 4) - 2 = 4`). The main exception is Exponentiation (`**`), which evaluates **Right-to-Left** (`2 ** 3 ** 2` is `2 ** (3 ** 2) = 2 ** 9 = 512`).

### 3.4 Expressions
An expression is a combination of values, variables, and operators that evaluates to a single value.
*   **Arithmetic Expression:** Evaluates to a number (e.g., `x + y * 5`)
*   **Relational Expression:** Evaluates to a boolean (e.g., `x > y`)
*   **Logical Expression:** Combines multiple boolean expressions (e.g., `x > 5 and x < 10`)

---

## Chapter 4: Control Structures

Control structures determine the flow of execution of a program. By default, code runs sequentially line-by-line.

### 4.1 Conditional Statements
Used for decision making.

#### The `if` Statement
Executes a block of code only if a condition is true. Python uses indentation to define code blocks.
```python
age = 20
if age >= 18:
    print("You are eligible to vote.") # Notice the indentation
```

#### The `if-else` Statement
Provides an alternative block of code if the condition is false.
```python
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

#### The `if-elif-else` Statement
Used for checking multiple conditions sequentially.
```python
marks = 85
if marks >= 90:
    print("Grade: O")
elif marks >= 80:
    print("Grade: E")
elif marks >= 70:
    print("Grade: A")
else:
    print("Grade: B")
```

#### Nested `if`
An `if` statement inside another `if` statement.
```python
num = 15
if num > 0:
    if num % 5 == 0:
        print("Positive and divisible by 5")
```

### 4.2 Looping Statements (Iteration)
Used to execute a block of code multiple times.

#### The `while` Loop
Repeatedly executes a target statement as long as a given condition is `True`.
```python
count = 1
while count <= 5:
    print(f"Iteration {count}")
    count += 1  # Crucial: Update the condition variable to avoid infinite loops
```

#### The `for` Loop
Used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
```python
name = "Python"
for char in name:
    print(char)
```

#### The `range()` Function
Often used with `for` loops to generate a sequence of numbers.
*   `range(stop)`: Generates numbers from `0` to `stop - 1`.
*   `range(start, stop)`: Generates numbers from `start` to `stop - 1`.
*   `range(start, stop, step)`: Generates numbers with a specific increment/decrement.
```python
for i in range(2, 10, 2):
    print(i, end=" ") # Prints: 2 4 6 8
```

### 4.3 Loop Control Statements
Alter the regular execution flow of loops.

#### The `break` Statement
Terminates the loop entirely and transfers execution to the statement immediately following the loop.
```python
for num in range(10):
    if num == 5:
        break # Stops the loop when num is 5
    print(num)
```

#### The `continue` Statement
Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
```python
for num in range(5):
    if num == 2:
        continue # Skips printing 2
    print(num)
```

#### The `pass` Statement
A null operation. Nothing happens when it executes. Used as a placeholder in syntactic blocks where code is eventually going to be added.
```python
for num in range(5):
    if num == 3:
        pass # To do: Add logic for 3 later
    print(num)
```

#### The `else` Clause in Loops
Python loops can have an `else` block. The `else` block executes **only if the loop completes normally** (i.e., it was NOT terminated by a `break` statement).
```python
for i in range(5):
    print(i)
else:
    print("Loop finished successfully without breaking.")
```

---

## 📝 Comprehensive Textbook Exercises and Solutions

### Conceptual Questions

**Q1. Describe the difference between a high-level language and a low-level language. Where does Python fit?**
*Answer:* A low-level language (like Assembly or Machine Code) is closer to the hardware, hard for humans to read, requires memory management, and is machine-dependent. A high-level language (like Python, Java, C++) is closer to human language, abstracts hardware details, provides automatic memory management, and is portable across platforms. Python is a High-Level Language.

**Q2. Explain Python's Dynamic Typing.**
*Answer:* In statically typed languages (like Java), you must declare the variable type before using it (e.g., `int x = 5;`). In Python, you do not declare the type. The interpreter assigns the type at runtime based on the value assigned to it (`x = 5` makes `x` an integer automatically). The type of `x` can even change during execution if reassigned (`x = "Hello"` makes it a string).

**Q3. What is the difference between `/` and `//` operators? Provide an example.**
*Answer:* `/` is True Division and always returns a floating-point number. `//` is Floor Division; it divides the operands and rounds the result down to the nearest integer towards negative infinity.
*Example:* `5 / 2` evaluates to `2.5`. `5 // 2` evaluates to `2`. `-5 // 2` evaluates to `-3`.

**Q4. Define Operator Precedence and Associativity.**
*Answer:* Precedence defines the order in which different operators in an expression are evaluated (e.g., `*` is evaluated before `+`). Associativity defines the order in which operators with the *same* precedence are evaluated. Most operators associate left-to-right, but exponentiation (`**`) associates right-to-left.

**Q5. What is an `identifier`? What are the rules for naming identifiers in Python?**
*Answer:* An identifier is a name used to identify a variable, function, class, module or other object. Rules: Must start with a letter (A-Z, a-z) or underscore `_`; can contain letters, digits, and underscores; cannot be a keyword; cannot contain special characters; is case-sensitive.

### Programming Problems

**P1. Write a Python program to find the roots of a quadratic equation.**
```python
import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = (b**2) - (4*a*c)

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Roots are real and different: {root1} and {root2}")
elif discriminant == 0:
    root1 = -b / (2*a)
    print(f"Roots are real and same: {root1}")
else:
    real_part = -b / (2*a)
    imag_part = math.sqrt(-discriminant) / (2*a)
    print(f"Roots are complex: {real_part} + {imag_part}i and {real_part} - {imag_part}i")
```

**P2. Write a Python program to check if a given year is a leap year.**
*Textbook Note: A year is a leap year if it is divisible by 4. However, if it is a century year (divisible by 100), it is a leap year ONLY if it is also divisible by 400.*
```python
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")
```

**P3. Write a program to print the sum of digits of a given number.**
```python
num = int(input("Enter a positive integer: "))
sum_digits = 0
temp = num

while temp > 0:
    digit = temp % 10          # Extract the last digit
    sum_digits += digit        # Add it to the sum
    temp = temp // 10          # Remove the last digit

print(f"The sum of digits of {num} is {sum_digits}")
```

**P4. Write a program to print all prime numbers between 1 and `N`.**
```python
n = int(input("Enter the upper limit N: "))

print(f"Prime numbers between 1 and {n}:")
for num in range(2, n + 1):
    is_prime = True
    # Only need to check up to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
            
    if is_prime:
        print(num, end=" ")
```

**P5. Evaluate the following Python expression step-by-step.**
Expression: `3 * 2 ** 3 // 4 + 5`
*Step 1:* Exponentiation first: `2 ** 3 = 8`. Expression becomes `3 * 8 // 4 + 5`.
*Step 2:* Multiplication and Floor Division have same precedence, associate left-to-right. `3 * 8 = 24`. Expression becomes `24 // 4 + 5`.
*Step 3:* Floor Division next. `24 // 4 = 6`. Expression becomes `6 + 5`.
*Step 4:* Addition. `6 + 5 = 11`.
*Output:* `11`
