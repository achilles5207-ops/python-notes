# 📘 Comprehensive Textbook Guide: Module 3 - Object-Oriented Programming (OOP) & Exception Handling

## Chapter 9: Fundamentals of Object-Oriented Programming

### 9.1 Introduction to OOP
Object-Oriented Programming (OOP) is a programming paradigm that revolves around the concept of "objects" rather than "actions", and "data" rather than "logic". It allows programmers to map real-world entities into code.

#### Key Principles of OOP:
1.  **Encapsulation:** Grouping data and methods into a single unit (class) and restricting access.
2.  **Abstraction:** Hiding complex implementation details and showing only essential features.
3.  **Inheritance:** Reusing code by allowing a new class to inherit properties from an existing one.
4.  **Polymorphism:** Allowing a single interface/method to represent different underlying forms (data types).

### 9.2 Classes and Objects
*   **Class:** A blueprint or template for creating objects. It defines the attributes (data) and methods (behavior) that the objects will have.
*   **Object:** A physical reality or instance of a class. It occupies memory.

#### Defining a Class and Creating an Object
```python
class Dog:
    # Method definition
    def bark(self):
        print("Woof! Woof!")

# Creating an Object (Instance)
my_dog = Dog()
my_dog.bark() # Method call
```

### 9.3 The `self` Keyword and Constructors

#### The `self` Parameter
Inside class methods, `self` represents the instance of the class. By using `self`, we can access the attributes and methods of the class. It MUST be the first parameter of any instance method.

#### Constructors (`__init__`)
A constructor is a special method used to initialize objects. In Python, the constructor is named `__init__()`. It is automatically called when an object is created.
```python
class Student:
    # Parameterized Constructor
    def __init__(self, name, roll_no):
        self.name = name       # Instance variable
        self.roll_no = roll_no # Instance variable

    def display(self):
        print(f"Student Name: {self.name}, Roll No: {self.roll_no}")

s1 = Student("Alice", 101) # __init__ is called automatically here
s1.display()
```

### 9.4 Instance vs. Class Variables
*   **Instance Variables:** Variables attached to `self`. They are unique to each object.
*   **Class Variables:** Variables declared directly inside the class but outside any methods. They are shared across all instances of the class.
```python
class Employee:
    company_name = "TechCorp" # Class Variable

    def __init__(self, name):
        self.name = name      # Instance Variable

emp1 = Employee("John")
emp2 = Employee("Jane")
print(emp1.company_name) # Shared by all: TechCorp
```

---

## Chapter 10: Encapsulation and Polymorphism

### 10.1 Encapsulation and Information Hiding
Encapsulation is the bundling of data and the methods that operate on that data. It restricts direct access to some of an object's components, which is crucial for preventing accidental interference and misuse (Information Hiding).

In Python, access modifiers are implemented via naming conventions:
*   **Public:** Accessible from anywhere. (e.g., `name`)
*   **Protected:** Intended for internal use and by subclasses. Prefixed with a single underscore. (e.g., `_age`)
*   **Private:** Strictly inaccessible from outside the class. Prefixed with a double underscore. (e.g., `__salary`)

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private variable

    def get_balance(self):       # Getter method (Public access point)
        return self.__balance

acc = BankAccount(1000)
# print(acc.__balance)       # AttributeError: 'BankAccount' object has no attribute '__balance'
print(acc.get_balance())     # 1000
```
*Note: Python implements privacy via "Name Mangling". `__balance` becomes `_BankAccount__balance` internally.*

### 10.2 Polymorphism
Polymorphism means "many forms". It allows different objects to respond to the same method call in their own way.

#### 1. Duck Typing
"If it walks like a duck and quacks like a duck, it must be a duck." Python doesn't check the type of the object, only if it has the required methods.

#### 2. Method Overriding
Occurs when a child class provides a specific implementation of a method that is already provided by its parent class.
```python
class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self): # Overriding the parent's method
        print("Meow")

c = Cat()
c.speak() # Output: Meow
```

#### 3. Method Overloading
Python does **NOT** support traditional method overloading (having multiple methods with the same name but different parameters). However, we can simulate it using default arguments.
```python
class Calculator:
    def add(self, a, b, c=0): # Simulates overloading
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))    # 5
print(calc.add(2, 3, 4)) # 9
```

#### 4. Operator Overloading
We can give extended meaning to standard operators (like `+`, `-`, `*`) for user-defined classes by overriding special "Magic Methods" or "Dunder (Double Under) Methods".
*   `__add__(self, other)` for `+`
*   `__sub__(self, other)` for `-`
*   `__str__(self)` for `print()` string representation.
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): # Overloading the '+' operator
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):        # Overloading string representation
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2 # Python calls p1.__add__(p2) behind the scenes
print(p3)    # Output: (4, 6)
```

---

## Chapter 11: Inheritance and Abstraction

### 11.1 Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.
*   **Parent Class (Base/Super Class):** The class being inherited from.
*   **Child Class (Derived/Sub Class):** The class that inherits.

#### Types of Inheritance
1.  **Single Inheritance:** One child inherits from one parent.
2.  **Multiple Inheritance:** One child inherits from multiple parents.
    ```python
    class Father: pass
    class Mother: pass
    class Child(Father, Mother): pass # Multiple
    ```
3.  **Multilevel Inheritance:** A child inherits from a parent, and then another child inherits from that child.
4.  **Hierarchical Inheritance:** Multiple children inherit from one parent.
5.  **Hybrid Inheritance:** A combination of the above.

#### The `super()` Function
`super()` returns a temporary object of the superclass that allows you to call its methods. Crucial for accessing the parent's constructor.
```python
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name) # Call parent's constructor
        self.emp_id = emp_id
```

### 11.2 Abstract Classes and Methods
An abstract class is a blueprint for other classes. It cannot be instantiated directly. An abstract method is a method that is declared but contains no implementation. Subclasses MUST override abstract methods.
Python provides the `abc` (Abstract Base Classes) module for this.
```python
from abc import ABC, abstractmethod

class Shape(ABC): # Inherits from ABC to become an Abstract Class
    @abstractmethod
    def area(self):
        pass # No implementation

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self): # MUST implement the abstract method
        return self.l * self.b

# s = Shape() # ERROR: Cannot instantiate abstract class
r = Rectangle(10, 5)
print(r.area())
```

---

## Chapter 12: Exception Handling

### 12.1 Errors vs. Exceptions
*   **Syntax Errors:** Errors caused by not following the proper structure (syntax) of the language. Detected before execution.
*   **Exceptions:** Errors that occur *during runtime* (e.g., dividing by zero, reading a missing file). If unhandled, they crash the program.

### 12.2 Handling Exceptions: `try`, `except`, `else`, `finally`
You can handle exceptions to prevent program crashes.
*   **`try`:** Block of code to be attempted (which might raise an exception).
*   **`except`:** Block of code to handle the exception if one occurs.
*   **`else`:** Executed ONLY IF no exceptions were raised in the try block.
*   **`finally`:** ALWAYS executed, regardless of whether an exception occurred or not. Crucial for cleanup (like closing files/connections).

```python
try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid integers!")
else:
    print(f"Result is {result}") # Runs if no error
finally:
    print("Execution complete. Cleaning up...") # ALWAYS runs
```

### 12.3 The `assert` Statement
Assertions are debugging aids that test a condition. If the condition is True, the program continues. If False, it raises an `AssertionError`.
```python
def calculate_age(year_born):
    age = 2024 - year_born
    assert age >= 0, "Age cannot be negative!" # Triggers if year_born > 2024
    return age
```

---

## 📝 Comprehensive Textbook Exercises and Solutions

### Conceptual Questions

**Q1. Define Encapsulation and explain how Python achieves it.**
*Answer:* Encapsulation is the concept of bundling data (attributes) and methods that operate on that data into a single unit (a class). It also involves hiding the internal state of the object. Python achieves this using naming conventions: prefixing an attribute with an underscore `_` makes it protected (by convention), and a double underscore `__` makes it strictly private via name mangling.

**Q2. What is Method Overriding? Give a real-world analogy.**
*Answer:* Method overriding is a polymorphism concept where a subclass provides its own specific implementation of a method that is already defined in its superclass. *Analogy:* A `Vehicle` parent class might have a generic `start_engine()` method. A `ElectricCar` subclass inherits `Vehicle` but overrides `start_engine()` because starting an electric motor is fundamentally different from a combustion engine.

**Q3. Differentiate between `Exception` and `Syntax Error`.**
*Answer:* A Syntax Error happens during the parsing phase before execution, caused by invalid code structure (like a missing colon). An Exception occurs during runtime when syntactically correct code fails due to invalid operations (like dividing by zero or accessing an out-of-bounds index).

**Q4. Why is the `finally` block useful?**
*Answer:* The `finally` block guarantees execution regardless of whether a `try` block succeeds, fails, or even has a `return` statement inside it. It is essential for releasing external resources, such as closing open files, closing database connections, or releasing network sockets, preventing memory/resource leaks.

**Q5. Explain Multiple Inheritance and the Diamond Problem.**
*Answer:* Multiple inheritance is when a class inherits from more than one parent class. The Diamond Problem occurs when two parent classes inherit from the same grandparent class, and the child class inherits from both parents. If the grandparent has a method that both parents override, Python needs to decide which parent's method to use in the child. Python solves this using Method Resolution Order (MRO).

### Programming Problems

**P1. Create a class `Complex` that overloads the `+` operator to add two complex numbers.**
```python
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        # Adds corresponding real and imaginary parts
        return Complex(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        # Format for printing
        return f"{self.real} + {self.imag}i"

c1 = Complex(2, 3)
c2 = Complex(4, 5)
c3 = c1 + c2 # Calls c1.__add__(c2)
print(f"Sum is: {c3}") # Output: 6 + 8i
```

**P2. Implement a simple class hierarchy demonstrating Multilevel Inheritance and the `super()` keyword.**
```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name) # Initialize parent's name
        self.student_id = student_id

class GraduateStudent(Student):
    def __init__(self, name, student_id, thesis_topic):
        super().__init__(name, student_id) # Initialize parent's variables
        self.thesis_topic = thesis_topic

    def display(self):
        print(f"Name: {self.name}, ID: {self.student_id}, Thesis: {self.thesis_topic}")

g = GraduateStudent("Alice", "S101", "Quantum Computing")
g.display()
```

**P3. Write a program that asks the user to input a file name. Use exception handling to catch the error if the file does not exist.**
```python
filename = input("Enter filename to open: ")
try:
    file = open(filename, 'r')
    content = file.read()
    print("File content read successfully.")
    file.close()
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found in the directory.")
except Exception as e:
    # A generic catch block for any other unforeseen errors
    print(f"An unexpected error occurred: {e}")
```

**P4. Write a Python program using an Abstract Base Class `Employee` with an abstract method `calculate_salary()`. Implement it in subclasses `FullTimeEmployee` and `PartTimeEmployee`.**
```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

ft = FullTimeEmployee("Alice", 5000)
pt = PartTimeEmployee("Bob", 80, 20)

print(f"{ft.name}'s Salary: ${ft.calculate_salary()}")
print(f"{pt.name}'s Salary: ${pt.calculate_salary()}")
```

**P5. Write a custom exception class `NegativeAgeError` and raise it if a user enters a negative age.**
```python
# Defining a Custom Exception
class NegativeAgeError(Exception):
    def __init__(self, message="Age cannot be negative"):
        self.message = message
        super().__init__(self.message)

def set_age(age):
    if age < 0:
        raise NegativeAgeError(f"Provided age {age} is invalid.")
    print(f"Age is set to {age}")

try:
    set_age(-5)
except NegativeAgeError as e:
    print(f"Caught an exception: {e}")
```
