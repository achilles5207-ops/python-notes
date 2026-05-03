# 📘 The Ultimate Master Guide: Module 4 - File Handling, Exceptions & Databases

---

## 📁 Section 1: File Handling
File handling is an important part of any web application or software. Python has several functions for creating, reading, updating, and deleting files.

### Types of Files
1. **Text Files:** Store data as characters. Examples: `.txt`, `.py`, `.csv`.
2. **Binary Files:** Store data in bytes (0s and 1s). Examples: `.jpg`, `.mp3`, `.exe`.

### Opening and Closing Files
The `open()` function returns a file object. It takes two parameters: filename and mode.
**Modes:**
- `r`: Read (Default). Raises error if file doesn't exist.
- `w`: Write. Overwrites existing file or creates new.
- `a`: Append. Adds to end of file without overwriting.
- `x`: Exclusive Create. Fails if file exists.
- `b`: Binary mode (e.g., `rb`, `wb`).

```python
# Standard way
f = open("demofile.txt", "w")
f.write("Hello World!")
f.close() # CRITICAL: Free up system resources!
```

### The `with` Statement (Context Manager)
The best practice for file handling. It automatically closes the file when the block is exited, even if an exception occurs inside the block.
```python
with open("demofile.txt", "r") as f:
    content = f.read()
    print(content)
# No need to call f.close() here!
```

### Reading Methods
- `read()`: Reads the entire file into a single string.
- `read(n)`: Reads the first `n` characters.
- `readline()`: Reads a single line. Memory efficient for massive files.
- `readlines()`: Reads all lines and returns a list of strings.

---

## 💻 Section 2: Command Line Arguments
Command line arguments are values passed to a Python script when executing it from the terminal: `python script.py arg1 arg2`.
They are accessed using the `sys` module's `argv` list.
- `sys.argv[0]` is ALWAYS the name of the script.
- `sys.argv[1]` is the first argument (always as a string).

```python
import sys
if len(sys.argv) > 1:
    print(f"Hello, {sys.argv[1]}!")
else:
    print("No arguments provided.")
```

---

## ⚠️ Section 3: Exception Handling
An Exception is a runtime error that disrupts the normal flow of the program. Handling them prevents the program from abruptly crashing.

### `try`, `except`, `else`, `finally`
- **`try` block:** Lets you test a block of code for errors.
- **`except` block:** Lets you handle the error.
- **`else` block:** Executes ONLY if there were NO exceptions in the try block.
- **`finally` block:** Executes REGARDLESS of the result. Used for cleanup tasks (closing files, DB connections).

```python
try:
    x = int(input("Enter a denominator: "))
    result = 10 / x
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Input must be an integer!")
else:
    print("Division successful. Result:", result)
finally:
    print("Execution complete. Cleaning up...")
```

### Raising Exceptions and Assertions
- **`raise` keyword:** Used to manually throw an exception.
  ```python
  age = -5
  if age < 0:
      raise ValueError("Age cannot be negative!")
  ```
- **`assert` keyword:** Used for debugging. If the condition is false, it raises an `AssertionError`.
  ```python
  assert age >= 0, "Age is negative!"
  ```

---

## 🗄️ Section 4: Database Connectivity (SQLite)
Python comes with a built-in lightweight SQL database engine called SQLite. We use the `sqlite3` module.

### Core Steps for DB Connectivity
1. **Connect:** Create a connection object linking to the DB file.
2. **Cursor:** Create a cursor object to execute SQL commands.
3. **Execute:** Run SQL queries (`CREATE`, `INSERT`, `SELECT`).
4. **Commit/Transactions:** Save the changes permanently.
5. **Close:** Terminate the connection.

### Complete CRUD Example
```python
import sqlite3

# 1. Connect to database
conn = sqlite3.connect('college.db')
cursor = conn.cursor()

# 2. CREATE Table
cursor.execute('''CREATE TABLE IF NOT EXISTS Students 
                  (id INTEGER PRIMARY KEY, name TEXT, marks REAL)''')

# 3. INSERT (Create)
# Always use '?' parameterized queries to prevent SQL Injection attacks!
cursor.execute("INSERT INTO Students (name, marks) VALUES (?, ?)", ("Alice", 95.5))
cursor.execute("INSERT INTO Students (name, marks) VALUES (?, ?)", ("Bob", 82.0))

# 4. SELECT (Read)
cursor.execute("SELECT * FROM Students")
rows = cursor.fetchall() # Returns a list of tuples
print("All Students:", rows)

# 5. UPDATE
cursor.execute("UPDATE Students SET marks = ? WHERE name = ?", (99.0, "Alice"))

# 6. DELETE
cursor.execute("DELETE FROM Students WHERE name = ?", ("Bob",))

# 7. Commit changes and Close connection
conn.commit()
conn.close()
```

---

## 📝 EXAM QUESTION BANK & SOLUTIONS

**Q1. What is the difference between `read()`, `readline()`, and `readlines()`?**
**Answer:** 
- `read()` returns the entire file content as a single huge string.
- `readline()` returns just one line from the file at a time.
- `readlines()` reads all the lines and returns them as a list of strings, where each string is a line.

**Q2. Write a program to count the number of lines and words in a text file.**
```python
def count_file_stats(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            print(f"Lines: {num_lines}, Words: {num_words}")
    except FileNotFoundError:
        print("File not found!")

# count_file_stats('sample.txt')
```

**Q3. Explain the purpose of the `else` block in a `try...except` construct.**
**Answer:** The `else` block is executed if and only if no exception is raised inside the `try` block. It is useful for code that should only run if the risky operation was successful, keeping the `try` block minimal.

**Q4. Write a program to handle multiple exceptions (`ZeroDivisionError` and `IndexError`) in a single `except` block.**
```python
my_list = [10, 5, 0]
try:
    index = int(input("Enter index to divide 100 by: "))
    result = 100 / my_list[index]
    print(result)
except (ZeroDivisionError, IndexError) as e:
    print(f"An error occurred: {e}")
```

**Q5. What is SQL Injection and how do parameterized queries in Python prevent it?**
**Answer:** SQL Injection is a hacking technique where malicious SQL statements are inserted into entry fields for execution (e.g., dropping tables). Parameterized queries (using `?` placeholders) prevent this by treating user input strictly as data, not executable code. The database engine escapes the input automatically.

**Q6. Write a SQLite program to fetch all students who scored above 90 marks from the `Students` table.**
```python
import sqlite3
def fetch_top_students():
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM Students WHERE marks > 90")
    top_students = cursor.fetchall()
    for student in top_students:
        print(student[0])
    conn.close()
```

**Q7. What is a Database Transaction? Explain `commit()` and `rollback()`.**
**Answer:** A transaction is a sequence of database operations treated as a single unit. `commit()` saves all changes made during the transaction permanently. `rollback()` undoes all changes made during the current transaction, usually called if an error occurs.

**Q8. Write a program that copies the contents of `source.txt` to `destination.txt`.**
```python
try:
    with open('source.txt', 'r') as src, open('destination.txt', 'w') as dest:
        content = src.read()
        dest.write(content)
        print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found.")
```

**Q9. Can a `try` block exist without an `except` block?**
**Answer:** Yes, but it MUST be followed by a `finally` block. `try...finally` is a valid construct used when you don't want to catch the error, but you guarantee that cleanup code (finally) will run before the error crashes the program.

**Q10. What does `sys.argv` contain?**
**Answer:** `sys.argv` is a list in Python, which contains the command-line arguments passed to the script. `sys.argv[0]` is the name of the script.
