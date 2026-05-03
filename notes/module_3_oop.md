# 📘 The Ultimate Master Guide: Module 3 - Object Oriented Programming (OOP)

---

## 🏛️ Section 1: Classes and Objects

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which contain data (attributes) and code (methods).

### Class and Object
- **Class:** A blueprint or template for creating objects. It defines the state and behavior that the created objects will have.
- **Object:** An instance of a class. It represents a real-world entity occupying memory.

### The `__init__` Constructor and `self`
The constructor is a special method called automatically when an object is instantiated. In Python, it is named `__init__`.
The `self` parameter is a reference to the current instance of the class. It is used to access variables that belong to the class.

```python
class Student:
    # Constructor
    def __init__(self, name, roll_no):
        self.name = name       # Instance variable
        self.roll_no = roll_no # Instance variable

    # Instance Method
    def display_info(self):
        print(f"Student: {self.name}, Roll No: {self.roll_no}")

# Creating objects (Instantiating)
s1 = Student("Alice", 101)
s2 = Student("Bob", 102)

s1.display_info()
```

---

## 🧬 Section 2: Inheritance

Inheritance allows a class (Child/Subclass) to inherit attributes and methods from another class (Parent/Superclass). It promotes **code reusability**.

### Types of Inheritance
1. **Single Inheritance:** One child inherits from one parent.
2. **Multiple Inheritance:** One child inherits from MULTIPLE parents. (Python supports this, Java does not).
3. **Multilevel Inheritance:** Child inherits from Parent, Parent inherits from Grandparent.
4. **Hierarchical Inheritance:** Multiple children inherit from one parent.
5. **Hybrid Inheritance:** A combination of the above.

### Code Example: Multilevel Inheritance
```python
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

class Puppy(Dog):
    def weep(self):
        print("Weeping...")

p = Puppy()
p.eat()  # Inherited from Animal
p.bark() # Inherited from Dog
p.weep() # Its own method
```

### The `super()` Function
`super()` is a built-in function that returns a proxy object that allows you to refer to the parent class. It is crucial for calling the parent's `__init__` constructor from the child class.

```python
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name) # Invokes Person's __init__
        self.salary = salary
```

---

## 🛡️ Section 3: Encapsulation and Information Hiding

Encapsulation is the bundling of data and the methods that act on that data into a single unit (the class). It also involves restricting direct access to some of an object's components (**Information Hiding**).

Python does not have strict access modifiers like `public`, `private`, or `protected`. Instead, it uses naming conventions:
- `public_var`: Public (accessible everywhere).
- `_protected_var`: Protected (convention implies it's internal, but still accessible).
- `__private_var`: Private. Triggers **Name Mangling**. Python changes the variable name to `_ClassName__private_var` to prevent accidental access.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private variable

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

account = BankAccount(1000)
# print(account.__balance) # ERROR: AttributeError
print(account.get_balance()) # Safe access: 1000
```

---

## 🎭 Section 4: Polymorphism

Polymorphism means "many forms". It occurs when we have many classes that are related to each other by inheritance or share a common interface.

### Method Overriding (Run-time Polymorphism)
When a child class provides a specific implementation of a method that is already provided by its parent class.
```python
class Bird:
    def sound(self):
        print("Some bird sound")

class Duck(Bird):
    def sound(self):
        print("Quack Quack") # Overrides parent method

d = Duck()
d.sound() # Output: Quack Quack
```

### Method Overloading (Compile-time Polymorphism)
Python **DOES NOT** natively support method overloading (having multiple methods with the same name but different parameters). If you define a method twice, the latest definition overrides the previous one. We achieve overloading using default arguments or variable-length arguments (`*args`).
```python
class MathOp:
    def add(self, a, b, c=0):
        return a + b + c

m = MathOp()
print(m.add(2, 3))    # Output: 5
print(m.add(2, 3, 4)) # Output: 9
```

### Operator Overloading
Giving extended meaning beyond their predefined operational meaning. For example, `+` adds integers but concatenates strings. We can use Magic/Dunder methods to overload operators for custom classes.
```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
        
    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2 # Calls p1.__add__(p2)
print(f"X: {p3.x}, Y: {p3.y}") # Output: X: 4, Y: 6
```

---

## 🧩 Section 5: Abstract Method and Class

An abstract class is a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class.
Python uses the `abc` (Abstract Base Classes) module for this.
- Abstract classes cannot be instantiated (you cannot create objects from them).
- Abstract methods have no body (`pass`).

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self): # MUST implement this, otherwise Error
        return 3.14 * self.radius * self.radius

# s = Shape() # ERROR: Can't instantiate abstract class
c = Circle(5)
print(c.area())
```

---

## ⚙️ Section 6: Standard Libraries in OOP & Full Operator Overloading (Lab Prerequisites)

### Comprehensive Operator Overloading
Your labs require full mathematical overloading for custom classes like `Fraction` or `Complex`.
- `__add__(self, other)`: Addition `+`
- `__sub__(self, other)`: Subtraction `-`
- `__mul__(self, other)`: Multiplication `*`
- `__truediv__(self, other)`: Division `/`
- `__lt__(self, other)`: Less than `<`
- `__eq__(self, other)`: Equal to `==`

```python
class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
        
    def __mul__(self, other):
        return Fraction(self.num * other.num, self.denom * other.denom)
```

### Using `datetime` and `random` inside Classes
Labs often ask you to calculate ages or random data.
```python
import datetime
import random

# Get today's date
today = datetime.date.today()
print(f"Today is {today.day}/{today.month}/{today.year}")

# Generate random points
random_x = random.randint(1, 100)
```

---

## 📝 EXAM QUESTION BANK & SOLUTIONS

**Q1. What is the difference between Class Variables and Instance Variables?**
**Answer:** Class variables are defined within the class construction but outside any methods, and they are shared among all instances of that class. Instance variables are defined within methods (usually `__init__`) and belong exclusively to a specific object.

**Q2. Does Python support Multiple Inheritance? How does it resolve conflicts if two parents have a method with the same name?**
**Answer:** Yes, Python supports Multiple Inheritance. It resolves method conflicts using Method Resolution Order (MRO) via the C3 Linearization algorithm. It searches the class hierarchy from left to right, depth-first.

**Q3. Write a program to overload the `>` operator to compare two student objects based on their marks.**
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def __gt__(self, other):
        return self.marks > other.marks

s1 = Student("Alice", 90)
s2 = Student("Bob", 85)
print("Alice > Bob:", s1 > s2) # True
```

**Q4. Explain Duck Typing in Python.**
**Answer:** Duck Typing is a concept related to dynamic typing, where the type or class of an object is less important than the methods it defines. "If it walks like a duck and quacks like a duck, it must be a duck." You don't need to check the object's type, just if it has the required method.

**Q5. Write a class `Rectangle` with private attributes `__length` and `__width`. Provide getter and setter methods to access and modify them, and a method to calculate the area.**
```python
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        
    def get_length(self):
        return self.__length
        
    def set_length(self, length):
        if length > 0: self.__length = length
        
    def get_width(self):
        return self.__width
        
    def set_width(self, width):
        if width > 0: self.__width = width
        
    def calculate_area(self):
        return self.__length * self.__width

rect = Rectangle(10, 5)
rect.set_length(15)
print("Area:", rect.calculate_area()) # Area: 75
```

**Q6. What are Magic Methods (Dunder Methods)? Name three.**
**Answer:** Magic methods are special methods with double underscores at the beginning and end of their names. They are invoked internally by Python during certain operations. Examples: `__init__` (initialization), `__str__` (string representation), `__add__` (operator overloading for `+`).

**Q7. Create an Abstract Base Class `Vehicle` with an abstract method `start()`. Inherit a class `Car` from it and implement the method.**
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine starting with a key.")

my_car = Car()
my_car.start()
```

**Q8. Why do we use Name Mangling in Python?**
**Answer:** We use double underscores (`__var`) to trigger name mangling, which changes the internal name of the variable to `_ClassName__var`. This is done to prevent accidental overriding of private attributes by subclasses, acting as a form of encapsulation.

**Q9. What is `self`? Can we use another word instead of `self`?**
**Answer:** `self` represents the instance of the class. By using the "self" keyword, we can access the attributes and methods of the class in python. It binds the attributes with the given arguments. Yes, `self` is not a reserved keyword, you can use any word (like `this`), but `self` is an unbreakable convention.

**Q10. Write a code snippet demonstrating Hierarchical Inheritance.**
```python
class Parent:
    def show_parent(self): print("Parent Class")

class Child1(Parent):
    def show_child1(self): print("Child 1 Class")

class Child2(Parent):
    def show_child2(self): print("Child 2 Class")

c1 = Child1()
c1.show_parent() # Inherits from Parent
c2 = Child2()
c2.show_parent() # Inherits from Parent
```
