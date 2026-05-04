# 📘 Comprehensive Textbook Guide: Module 5 - Data Handling, Visualization & GUI

## Chapter 15: Regular Expressions (Regex)

### 15.1 Introduction to Regular Expressions
A Regular Expression (Regex) is a sequence of characters that forms a search pattern. It is incredibly powerful for string searching, text manipulation, and input validation (e.g., checking if an email is valid). Python uses the built-in `re` module.

### 15.2 Metacharacters and Quantifiers
To build patterns, we use special characters:
*   `.` : Matches any single character except newline.
*   `^` : Starts with.
*   `$` : Ends with.
*   `*` : Zero or more occurrences.
*   `+` : One or more occurrences.
*   `?` : Zero or one occurrence.
*   `{n,m}`: Exactly between n and m occurrences.
*   `[]` : A set of characters. e.g., `[a-z]` matches any lowercase letter.
*   `\d` : Matches any digit. Equivalent to `[0-9]`.
*   `\w` : Matches any alphanumeric character. Equivalent to `[a-zA-Z0-9_]`.
*   `\s` : Matches any whitespace character.

### 15.3 The `re` Module Functions
1.  **`re.match(pattern, string)`:** Checks for a match ONLY at the beginning of the string. Returns a Match object if successful, else `None`.
2.  **`re.search(pattern, string)`:** Searches the entire string for the FIRST occurrence of the pattern.
3.  **`re.findall(pattern, string)`:** Returns a list containing all matches in the string.
4.  **`re.sub(pattern, repl, string)`:** Replaces all occurrences of the pattern with the replacement string.

```python
import re

text = "The rain in Spain falls mainly in the plain. Contact: 123-456-7890."

# 1. findall
all_in = re.findall(r"in", text)
print(all_in) # ['in', 'in', 'in', 'in']

# 2. search (extracting phone number)
phone_pattern = r"\d{3}-\d{3}-\d{4}"
match = re.search(phone_pattern, text)
if match:
    print(f"Found phone: {match.group()}") # 123-456-7890

# 3. sub (Replace digits with 'X')
hidden = re.sub(r"\d", "X", text)
print(hidden) # ... Contact: XXX-XXX-XXXX.
```

---

## Chapter 16: Data Science Fundamentals - NumPy & Pandas

### 16.1 Introduction to NumPy
NumPy (Numerical Python) is the core library for scientific computing in Python. It provides a high-performance multidimensional array object (`ndarray`) and tools for working with these arrays. It is significantly faster than standard Python Lists because it stores data contiguously in memory and is written in C.

#### Creating Arrays and Matrices
```python
import numpy as np

# 1D Array from a list
arr_1d = np.array([1, 2, 3, 4, 5])

# 2D Array (Matrix) from list of lists
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Built-in creation functions
zeros = np.zeros((3, 3))        # 3x3 matrix of 0.0s
ones = np.ones((2, 4))          # 2x4 matrix of 1.0s
range_arr = np.arange(0, 10, 2) # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5) # 5 evenly spaced numbers from 0 to 1
```

### 16.2 Introduction to Pandas
Pandas is built on top of NumPy. It provides high-level data structures and manipulation tools tailored for data analysis.
*   **Series:** A 1D labeled array capable of holding any data type (like a single column).
*   **DataFrame:** A 2D labeled data structure with columns of potentially different types (like an Excel spreadsheet or SQL table).

#### Creating DataFrames and Basic Operations
```python
import pandas as pd

# 1. Creating from a Dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NY', 'LA', 'Chicago']
}
df = pd.DataFrame(data)

# 2. Reading from CSV
# df = pd.read_csv('dataset.csv')

# 3. Viewing Data
print(df.head(2)) # Shows first 2 rows
print(df.info())  # Shows column data types and non-null counts
```

### 16.3 Data Manipulation and Aggregation
Pandas makes querying and cleaning data easy.
```python
# Selection / Indexing
names = df['Name']             # Selects single column (Returns a Series)
older_than_28 = df[df['Age'] > 28] # Filtering rows

# Handling Missing Data
# df.dropna()       # Drops any row with a NaN value
# df.fillna(0)      # Replaces NaN values with 0

# Aggregation and Grouping
data2 = {'Department': ['HR', 'IT', 'HR', 'IT'], 'Salary': [50, 80, 60, 90]}
df2 = pd.DataFrame(data2)

# Group by Department and find mean salary
avg_salary = df2.groupby('Department').mean()
print(avg_salary)
```

#### Reshaping DataFrames
*   **Merge (Joins):** Combines DataFrames based on a common column (like SQL Joins).
*   **Concat:** Glues DataFrames together vertically (adding rows) or horizontally (adding columns).
```python
df_a = pd.DataFrame({'ID': [1, 2], 'Val': ['A', 'B']})
df_b = pd.DataFrame({'ID': [1, 2], 'Val': ['C', 'D']})
vertical_concat = pd.concat([df_a, df_b])
```

---

## Chapter 17: Data Visualization - Matplotlib

### 17.1 Introduction to Matplotlib
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations. The `matplotlib.pyplot` module provides a MATLAB-like interface for simple plotting.

### 17.2 Creating Basic Plots and Customizing
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = x ** 2

# 1. Line Plot
plt.plot(x, y, marker='o', color='red', linestyle='--')
plt.title("Line Plot Example")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()

# 2. Scatter Plot (Shows relationship between two numerical variables)
plt.scatter(x, y, color='blue')
plt.show()

# 3. Bar Chart (Categorical data)
categories = ['A', 'B', 'C']
values = [10, 25, 15]
plt.bar(categories, values, color='green')
plt.show()

# 4. Histogram (Shows distribution of numerical data)
data = np.random.randn(1000) # 1000 standard normal random numbers
plt.hist(data, bins=30, edgecolor='black')
plt.show()
```

---

## Chapter 18: Graphical User Interface (GUI) - Tkinter

### 18.1 Introduction to GUI Toolkits
A GUI allows users to interact with software using visual elements like buttons and text boxes instead of text-based command lines. Python offers several toolkits (PyQt, wxPython), but **Tkinter** is the standard, built-in GUI library.

### 18.2 Creating the Main Window
Every Tkinter app requires a root window and an infinite loop (`mainloop()`) to listen for events (like mouse clicks).
```python
import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("400x300") # Width x Height

# ... Add widgets here ...

root.mainloop() # Keeps the window open
```

### 18.3 Layout Management
Tkinter offers three geometry managers to position widgets:
1.  **`pack()`:** Packs widgets vertically or horizontally. Simplest but least precise.
2.  **`grid()`:** Places widgets in a 2D table (rows and columns). Most commonly used.
3.  **`place()`:** Places widgets at exact X, Y coordinates.

### 18.4 Basic Widgets (Label, Button, Entry)
```python
import tkinter as tk
from tkinter import messagebox

def on_click():
    name = entry.get()
    # Dialog box
    messagebox.showinfo("Greeting", f"Hello, {name}!")

root = tk.Tk()

# Label
lbl = tk.Label(root, text="Enter Name:", font=("Arial", 14))
lbl.grid(row=0, column=0, padx=10, pady=10)

# Entry (Text Input)
entry = tk.Entry(root, font=("Arial", 14))
entry.grid(row=0, column=1)

# Button
btn = tk.Button(root, text="Submit", command=on_click, bg="lightblue")
btn.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
```

### 18.5 Checkboxes and Radio Buttons
*   **Checkboxes (`Checkbutton`):** Used for multiple selections.
*   **Radio Buttons (`Radiobutton`):** Used when only ONE option can be selected from a group.
```python
import tkinter as tk
root = tk.Tk()

# Radio Buttons (Require a shared control variable)
radio_var = tk.StringVar(value="Option 1")
r1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
r2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
r1.pack(); r2.pack()

# Checkboxes (Require individual control variables)
check_var = tk.IntVar()
cb = tk.Checkbutton(root, text="I agree to terms", variable=check_var)
cb.pack()

root.mainloop()
```

---

## 📝 Comprehensive Textbook Exercises and Solutions

### Conceptual Questions

**Q1. Differentiate between `re.match()` and `re.search()`.**
*Answer:* `re.match()` attempts to match the pattern *only at the very beginning* of the string. If the pattern is found later in the string, it fails. `re.search()` scans the *entire string* and returns the first location where the pattern produces a match.

**Q2. Why is NumPy faster than standard Python lists for numerical operations?**
*Answer:* Python lists are arrays of pointers to objects spread across memory, causing overhead. NumPy arrays are homogeneous (contain only one data type) and are stored in contiguous blocks of memory. Furthermore, NumPy operations are implemented in optimized C code, avoiding the Python interpreter loop overhead (Vectorization).

**Q3. Describe the difference between a Pandas Series and a DataFrame.**
*Answer:* A Series is a 1-Dimensional array capable of holding data of any type, with an index. It is essentially a single column. A DataFrame is a 2-Dimensional table containing data with both row and column indices. A DataFrame can be thought of as a dictionary of Series objects.

**Q4. What is the purpose of `plt.show()` in Matplotlib?**
*Answer:* Matplotlib builds the plot in memory as you call functions like `plt.plot()` or `plt.title()`. `plt.show()` tells the backend rendering engine to take the completed figure from memory and display it in a GUI window on the screen.

**Q5. Explain the role of `mainloop()` in a Tkinter application.**
*Answer:* `mainloop()` is an infinite loop that waits for events to occur in the GUI window (such as button clicks, key presses, or mouse movements). It blocks the execution of any code written after it until the window is closed. It processes these events and updates the GUI accordingly.

### Programming Problems

**P1. Write a Python program using Regex to validate if an inputted string is a valid email address.**
```python
import re

def is_valid_email(email):
    # Pattern: characters @ characters . characters
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return True
    else:
        return False

print(is_valid_email("test.user@example.com")) # True
print(is_valid_email("invalid_email@.com"))    # False
```

**P2. Create a 3x3 NumPy matrix containing numbers from 1 to 9. Multiply the entire matrix by 10.**
```python
import numpy as np

# arange generates 1 to 9, reshape converts it to 3x3
matrix = np.arange(1, 10).reshape(3, 3)
print("Original Matrix:")
print(matrix)

# Vectorized operation: multiplies every element by 10
result = matrix * 10
print("\nMultiplied by 10:")
print(result)
```

**P3. Given a dictionary of data, create a Pandas DataFrame. Group the data by 'Category' and calculate the sum of 'Values'.**
```python
import pandas as pd

data = {
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Food'],
    'Values': [500, 50, 700, 100, 20]
}

df = pd.DataFrame(data)

# GroupBy and Sum
grouped_sum = df.groupby('Category')['Values'].sum()

print("Total Sales by Category:")
print(grouped_sum)
# Output:
# Category
# Clothing       150
# Electronics   1200
# Food            20
```

**P4. Write a Matplotlib script to draw a Line Plot with custom X and Y axis labels, a title, and a grid.**
```python
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [250, 300, 150, 400]

plt.plot(months, sales, color='purple', marker='s', linewidth=2)
plt.title("Monthly Sales Report")
plt.xlabel("Month")
plt.ylabel("Sales in USD")
plt.grid(True) # Adds a grid
plt.show()
```

**P5. Create a simple Tkinter GUI with a Label, an Entry widget to input a temperature in Celsius, and a Button that converts it to Fahrenheit and updates the Label.**
```python
import tkinter as tk

def convert():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        # Update the result label text
        result_lbl.config(text=f"Result: {fahrenheit} °F")
    except ValueError:
        result_lbl.config(text="Result: Invalid Input!")

# Setup main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x150")

# Widgets
tk.Label(root, text="Enter Celsius:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Convert to Fahrenheit", command=convert).pack(pady=5)

result_lbl = tk.Label(root, text="Result: ")
result_lbl.pack(pady=5)

# Start application
root.mainloop()
```
