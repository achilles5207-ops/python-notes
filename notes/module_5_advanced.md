# 📘 The Ultimate Master Guide: Module 5 - Data Handling, Visualization & GUI

---

## 🔍 Section 1: Regular Expressions (RegEx)
Regular Expressions are a powerful sequence of characters that form a search pattern, used for string matching and manipulation. Python uses the `re` module.

### Key Functions
- `re.match(pattern, string)`: Checks for a match ONLY at the **beginning** of the string.
- `re.search(pattern, string)`: Searches the **entire** string, returns the FIRST match.
- `re.findall(pattern, string)`: Returns a **list of all** non-overlapping matches.
- `re.sub(pattern, repl, string)`: **Replaces** the matches with a replacement string.

### Metacharacters & Quantifiers
- `.` : Any character except newline.
- `\d` : Digit (0-9).
- `\w` : Word character (a-z, A-Z, 0-9, _).
- `\s` : Whitespace.
- `*` : 0 or more occurrences.
- `+` : 1 or more occurrences.
- `?` : 0 or 1 occurrence (Also makes quantifiers "lazy" or non-greedy).
- `^` : Starts with.
- `$` : Ends with.

```python
import re
text = "The price is $100 and $250."
matches = re.findall(r"\$\d+", text)
print(matches) # Output: ['$100', '$250']
```

---

## 🔢 Section 2: NumPy (Numerical Python)
NumPy is the core library for scientific computing in Python. It provides a high-performance multidimensional array object (`ndarray`).

### Why NumPy over Lists?
NumPy arrays use continuous memory blocks (C-style), making them up to 50x faster than standard Python lists. They also support **Vectorization** (performing operations on entire arrays without loops).

### Array Creation & Operations
```python
import numpy as np

# Creating Arrays
arr = np.array([1, 2, 3])
matrix = np.array([[1, 2], [3, 4]])
zeros = np.zeros((2, 2)) # 2x2 matrix of zeros
range_arr = np.arange(0, 10, 2) # [0, 2, 4, 6, 8]

# Vectorized Math
print(arr * 10) # Output: [10 20 30]

# Shape and Reshape
print(matrix.shape) # Output: (2, 2)
flat = matrix.reshape(-1) # Flattens to 1D: [1, 2, 3, 4]
```

---

## 🐼 Section 3: Pandas
Pandas is built on top of NumPy and provides easy-to-use data structures for data analysis.

### Core Data Structures
1. **Series:** 1D labeled array (like a column in Excel).
2. **DataFrame:** 2D labeled data structure with columns of potentially different types (like a full Excel spreadsheet).

### DataFrame Operations
```python
import pandas as pd

# 1. Creation
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, np.nan], # np.nan = Missing data
    'Salary': [50000, 60000, 70000]
}
df = pd.DataFrame(data)

# 2. Data Manipulation
# Handling missing data
df['Age'] = df['Age'].fillna(df['Age'].mean()) # Fills NaN with mean age

# Selection and Filtering
high_earners = df[df['Salary'] > 55000]

# 3. Aggregation & GroupBy
df['Dept'] = ['IT', 'HR', 'IT']
avg_salary = df.groupby('Dept')['Salary'].mean()
print(avg_salary)
```

---

## 📊 Section 4: Matplotlib
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. The `pyplot` module is most commonly used.

### Basic Plot Types
- **Line Plot:** Shows trends over time. `plt.plot(x, y)`
- **Scatter Plot:** Shows relationships/correlations between two variables. `plt.scatter(x, y)`
- **Bar Chart:** Compares categorical data. `plt.bar(x, y)`
- **Histogram:** Shows frequency distribution of continuous data. `plt.hist(data)`

### Customizing Plots
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y, color='red', linestyle='--', marker='o', label='Growth')
plt.title("Company Growth")
plt.xlabel("Years")
plt.ylabel("Revenue")
plt.legend()
plt.grid(True)
# plt.show() # Renders the graph
```

---

## 🪟 Section 5: Graphical User Interface (GUI) with Tkinter
Tkinter is Python's standard GUI library. It relies on an event-driven architecture.

### GUI Basics & Widgets
1. **Window:** The main application container (`root = tk.Tk()`).
2. **Widgets:** Elements like Buttons, Labels, Checkboxes.
3. **Layout Managers:** Place widgets on the screen.
   - `pack()`: Organizes widgets in blocks (top to bottom).
   - `grid()`: Organizes widgets in a 2D table-like structure (rows, columns).
4. **Mainloop:** `root.mainloop()` enters an infinite loop waiting for events.

### Complete Tkinter Application Example
```python
import tkinter as tk
from tkinter import messagebox

# 1. Initialize Window
root = tk.Tk()
root.title("My App")
root.geometry("300x200")

# 2. Function for Button Click Event
def submit_action():
    name = entry.get()
    messagebox.showinfo("Greeting", f"Hello {name}!")

# 3. Create Widgets
label = tk.Label(root, text="Enter Name:")
entry = tk.Entry(root)
btn = tk.Button(root, text="Submit", command=submit_action)

# Checkbox
var = tk.IntVar()
check = tk.Checkbutton(root, text="Agree to Terms", variable=var)

# 4. Create Layout (using pack)
label.pack(pady=5)
entry.pack(pady=5)
check.pack(pady=5)
btn.pack(pady=10)

# 5. Start Event Loop
# root.mainloop()
```

---

## 📐 Section 6: Advanced Linear Algebra & Matrix Slicing in NumPy (Lab Prerequisites)
Your lab assignments heavily feature matrix manipulation and linear algebra algorithms.

### Advanced Slicing
```python
import numpy as np
matrix = np.arange(1, 37).reshape(6, 6) # 6x6 matrix (1 to 36)

# Extract top-left 3x3 submatrix
top_left = matrix[:3, :3]

# Extract the last two rows
last_two_rows = matrix[-2:, :]

# Extract every alternate column
alt_cols = matrix[:, ::2]

# Update last column to 100
matrix[:, -1] = 100
```

### Linear Algebra (`numpy.linalg`)
NumPy handles complex matrix mathematics natively:
```python
mat = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])

# Trace (sum of main diagonal elements)
print("Trace:", np.trace(mat))

# Determinant
print("Determinant:", np.linalg.det(mat))

# Inverse
print("Inverse:", np.linalg.inv(mat))

# Rank
print("Rank:", np.linalg.matrix_rank(mat))
```

---

## 📝 EXAM QUESTION BANK & SOLUTIONS

**Q1. Extract all email addresses from a text using RegEx.**
```python
import re
text = "Contact admin@corp.com or support@help.org for assistance."
pattern = r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern, text)
print(emails) # ['admin@corp.com', 'support@help.org']
```

**Q2. What is the difference between `re.match()` and `re.search()`?**
**Answer:** `re.match()` only checks for a match at the very beginning of the string. If the pattern is in the middle of the string, it returns `None`. `re.search()` scans through the entire string looking for the first location where the pattern matches.

**Q3. Create a 3x3 NumPy matrix filled with numbers from 1 to 9.**
```python
import numpy as np
arr = np.arange(1, 10)     # Creates 1D array: [1...9]
matrix = arr.reshape(3, 3) # Reshapes to 3x3
print(matrix)
```

**Q4. Differentiate between `loc` and `iloc` in Pandas.**
**Answer:** Both are used for data selection. `loc` is label-based, meaning you specify the name of the row/column index (e.g., `df.loc['row1', 'colA']`). `iloc` is integer-position based, meaning you specify the numeric physical index (e.g., `df.iloc[0, 1]`).

**Q5. Write a Pandas script to drop rows with missing values and then save the DataFrame to a CSV.**
```python
import pandas as pd
# Assuming df is a pre-existing DataFrame
clean_df = df.dropna()
clean_df.to_csv("clean_data.csv", index=False)
```

**Q6. How do you create multiple plots in a single figure in Matplotlib?**
```python
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=1, ncols=2) # 1 row, 2 columns of plots
axes[0].plot([1, 2], [1, 4]) # First plot
axes[1].bar(["A", "B"], [5, 10]) # Second plot
# plt.show()
```

**Q7. Explain the `pack()`, `grid()`, and `place()` layout managers in Tkinter.**
**Answer:** 
- `pack()` stacks widgets vertically or horizontally in a block.
- `grid()` aligns widgets in a 2D table grid defined by rows and columns.
- `place()` allows you to place widgets at exact absolute x and y coordinates (not recommended for responsive design).

**Q8. Write a Tkinter script to create two Radio Buttons allowing the user to select gender.**
```python
import tkinter as tk
root = tk.Tk()
gender_var = tk.StringVar(value="Male")

r1 = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
r2 = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")

r1.pack()
r2.pack()
# root.mainloop()
```

**Q9. What is Broadcasting in NumPy?**
**Answer:** Broadcasting is a powerful mechanism that allows NumPy to perform arithmetic operations on arrays of different shapes. The smaller array is "broadcast" (virtually stretched) across the larger array so that they have compatible shapes.

**Q10. Explain the concept of Vectorization.**
**Answer:** Vectorization is the process of executing operations on entire arrays (like addition or multiplication) simultaneously, rather than using a Python `for` loop to iterate over individual elements. This pushes the loop into optimized, pre-compiled C code, making it drastically faster.
