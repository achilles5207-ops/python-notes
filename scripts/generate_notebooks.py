import nbformat as nbf
import os

def create_nb(filename, content_blocks):
    nb = nbf.v4.new_notebook()
    for cell_type, content in content_blocks:
        if cell_type == "md":
            nb.cells.append(nbf.v4.new_markdown_cell(content))
        elif cell_type == "code":
            nb.cells.append(nbf.v4.new_code_cell(content))
    
    filepath = f"/workspaces/python-notes/notebooks/{filename}.ipynb"
    with open(filepath, "w") as f:
        nbf.write(nb, f)

# Module 1
m1 = [
    ("md", "# 📘 Module 1: Introduction to Python & Control Structures - Practice Notebook\nWelcome to Module 1! Here you'll practice basic Python concepts, variables, data types, and control flow. Read the tips, answer the questions, and run the code blocks to test your solutions."),
    ("md", "## 💡 Tip: The `print()` Function\nAlways remember that the `print()` function takes `sep` and `end` arguments. By default, `sep=' '` and `end='\\n'`."),
    ("md", "### Question 1: Basic Input/Output\nWrite a program that takes a user's name and age, and prints a greeting message. Calculate the year they will turn 100."),
    ("code", "name = 'TestUser' # input('Enter name: ')\nage = 20 # int(input('Enter age: '))\ncurrent_year = 2024\nyear_100 = current_year + (100 - age)\nprint(f'Hello {name}, you will turn 100 in the year {year_100}.')"),
    ("md", "### Question 2: Conditionals\nWrite a program to check if a given number is positive, negative, or zero."),
    ("code", "num = 15\nif num > 0:\n    print('Positive')\nelif num < 0:\n    print('Negative')\nelse:\n    print('Zero')"),
    ("md", "### Question 3: Looping\nWrite a Python program to print the Fibonacci sequence up to $N$ terms."),
    ("code", "n = 10\na, b = 0, 1\nfor _ in range(n):\n    print(a, end=' ')\n    a, b = b, a + b\nprint()"),
    ("md", "## 🚀 Pro-Tip: The `else` clause in Loops\nIn Python, you can use `else` with a `for` or `while` loop. The `else` block executes ONLY if the loop finishes without hitting a `break` statement."),
    ("md", "### Question 4: Prime Number Check\nUse a `for-else` loop to check if a number is prime."),
    ("code", "num = 29\nfor i in range(2, int(num**0.5) + 1):\n    if num % i == 0:\n        print(f'{num} is not prime.')\n        break\nelse:\n    print(f'{num} is a prime number!')")
]

# Module 2
m2 = [
    ("md", "# 📘 Module 2: Data Structures, Functions & Modules - Practice Notebook\nPractice Lists, Tuples, Sets, Dictionaries, and writing robust functions."),
    ("md", "## 💡 Tip: List Comprehensions\nList comprehensions are faster than regular `for` loops for creating lists because they are optimized in C underlying Python."),
    ("md", "### Question 1: List Comprehension\nCreate a list of squares for all even numbers from 1 to 20."),
    ("code", "even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]\nprint(even_squares)"),
    ("md", "### Question 2: Dictionary Manipulation\nGiven a string, count the frequency of each character using a dictionary."),
    ("code", "text = 'hello python'\nfreq = {}\nfor char in text:\n    freq[char] = freq.get(char, 0) + 1\nprint(freq)"),
    ("md", "## 🚀 Pro-Tip: The Default Mutable Argument Trap\nNever use a mutable object (like `[]` or `{}`) as a default argument in a function. Use `None` instead. Otherwise, the object is shared across all function calls."),
    ("md", "### Question 3: Functions and `*args`\nWrite a function that accepts any number of numeric arguments and returns their product."),
    ("code", "def multiply_all(*args):\n    result = 1\n    for num in args:\n        result *= num\n    return result\n\nprint(f'Product of 2,3,4,5 is: {multiply_all(2, 3, 4, 5)}')"),
    ("md", "### Question 4: Lambda Functions\nSort a list of tuples `[(name, age), ...]` based on age in descending order using a lambda function."),
    ("code", "people = [('Alice', 25), ('Bob', 30), ('Charlie', 22)]\npeople.sort(key=lambda x: x[1], reverse=True)\nprint(people)")
]

# Module 3
m3 = [
    ("md", "# 📘 Module 3: Object-Oriented Programming & Exceptions - Practice Notebook\nMaster Classes, Objects, Inheritance, and handling runtime errors."),
    ("md", "## 💡 Tip: `self` is Mandatory\nAlways remember to include `self` as the first parameter in instance methods!"),
    ("md", "### Question 1: Creating Classes\nCreate a `Rectangle` class with `length` and `width` attributes, and a method `area()`."),
    ("code", "class Rectangle:\n    def __init__(self, length, width):\n        self.length = length\n        self.width = width\n    \n    def area(self):\n        return self.length * self.width\n\nrect = Rectangle(10, 5)\nprint(f'Area: {rect.area()}')"),
    ("md", "### Question 2: Inheritance & Overriding\nCreate a parent class `Animal` with a method `speak()`. Create a child class `Dog` that overrides `speak()`."),
    ("code", "class Animal:\n    def speak(self):\n        print('Generic sound')\n\nclass Dog(Animal):\n    def speak(self):\n        print('Woof!')\n\nd = Dog()\nd.speak()"),
    ("md", "## 🚀 Pro-Tip: Multiple `except` blocks\nYou can handle different exceptions differently by providing multiple `except` blocks. Place the most specific exceptions first and generic `Exception` at the end."),
    ("md", "### Question 3: Exception Handling\nWrite a program that safely divides two numbers, handling both `ZeroDivisionError` and `ValueError`."),
    ("code", "def safe_divide(a, b):\n    try:\n        return float(a) / float(b)\n    except ZeroDivisionError:\n        return 'Cannot divide by zero!'\n    except ValueError:\n        return 'Invalid input, must be numbers.'\n\nprint(safe_divide(10, 2))\nprint(safe_divide(10, 0))\nprint(safe_divide('a', 'b'))")
]

# Module 4
m4 = [
    ("md", "# 📘 Module 4: File Handling & Database Connectivity - Practice Notebook\nLearn how to persist data using files and SQL databases."),
    ("md", "## 💡 Tip: The `with` statement\nAlways use the `with` context manager when opening files. It ensures the file is closed automatically, even if an exception occurs."),
    ("md", "### Question 1: Reading and Writing Files\nWrite a list of strings to a file, then read the file line by line and print them."),
    ("code", "lines = ['Python is fun\\n', 'Data Science is cool\\n']\nwith open('sample.txt', 'w') as f:\n    f.writelines(lines)\n\nwith open('sample.txt', 'r') as f:\n    for line in f:\n        print(line.strip())\n\nimport os\nos.remove('sample.txt') # clean up"),
    ("md", "### Question 2: Pickling (Binary Serialization)\nPickle a dictionary to a binary file, and then load it back."),
    ("code", "import pickle\nimport os\ndata = {'user': 'Alice', 'score': 99}\n\n# Save\nwith open('data.pkl', 'wb') as f:\n    pickle.dump(data, f)\n\n# Load\nwith open('data.pkl', 'rb') as f:\n    loaded = pickle.load(f)\nprint(loaded)\nos.remove('data.pkl') # clean up"),
    ("md", "## 🚀 Pro-Tip: Commit Transactions\nIn database programming, DML queries (INSERT, UPDATE, DELETE) are not permanently saved until you call `connection.commit()`."),
    ("md", "### Question 3: SQLite Database Operations\nCreate an in-memory SQLite database, create a table `Books`, insert one book, and fetch it."),
    ("code", "import sqlite3\n\nconn = sqlite3.connect(':memory:') # Using in-memory DB for practice\ncursor = conn.cursor()\n\ncursor.execute('''CREATE TABLE Books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)''')\ncursor.execute(\"INSERT INTO Books (title, author) VALUES ('1984', 'George Orwell')\")\nconn.commit()\n\ncursor.execute(\"SELECT * FROM Books\")\nprint(cursor.fetchall())\nconn.close()")
]

# Module 5
m5 = [
    ("md", "# 📘 Module 5: Advanced Data Handling, Visualization & GUI - Practice Notebook\nExplore Regex, Pandas, Matplotlib, and Tkinter."),
    ("md", "## 💡 Tip: Regex Raw Strings\nAlways use raw strings (`r'pattern'`) for Regular Expressions in Python to avoid conflicts with escape characters."),
    ("md", "### Question 1: Regular Expressions\nExtract all email addresses from a given text using `re`."),
    ("code", "import re\ntext = 'Contact us at support@example.com or admin@domain.org'\npattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}'\nemails = re.findall(pattern, text)\nprint(emails)"),
    ("md", "### Question 2: Pandas DataFrames\nCreate a Pandas DataFrame from a dictionary and calculate the average age."),
    ("code", "import pandas as pd\ndata = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}\ndf = pd.DataFrame(data)\nprint('DataFrame:\\n', df)\nprint(f'\\nAverage Age: {df[\"Age\"].mean()}')"),
    ("md", "## 🚀 Pro-Tip: Matplotlib Customizations\nYou can enhance your plots significantly using `plt.title()`, `plt.xlabel()`, `plt.grid()`, and adding markers like `marker='o'`."),
    ("md", "### Question 3: Matplotlib Line Plot\nPlot the function $y = x^2$ for $x$ from -5 to 5."),
    ("code", "import matplotlib.pyplot as plt\nimport numpy as np\n\nx = np.linspace(-5, 5, 20)\ny = x**2\n\nplt.plot(x, y, marker='o', color='red')\nplt.title('y = x^2')\nplt.xlabel('x')\nplt.ylabel('y')\nplt.grid(True)\nplt.show()"),
    ("md", "### Question 4: Basic Tkinter (Informational)\nTkinter apps require a `mainloop()` to keep the window open. Since Jupyter Notebooks run in the browser and Tkinter creates desktop windows, they can sometimes clash. It is recommended to run Tkinter code in a standard `.py` script."),
    ("code", "\"\"\"\nimport tkinter as tk\n\nroot = tk.Tk()\nroot.title('Hello App')\n\nlabel = tk.Label(root, text='Welcome to GUI Programming!')\nlabel.pack(pady=20)\n\nroot.mainloop()\n\"\"\"\nprint('Run the Tkinter code in a standard python script (.py) for best results.')")
]

create_nb('Module_1_Practice', m1)
create_nb('Module_2_Practice', m2)
create_nb('Module_3_Practice', m3)
create_nb('Module_4_Practice', m4)
create_nb('Module_5_Practice', m5)
print("All notebooks created successfully!")
