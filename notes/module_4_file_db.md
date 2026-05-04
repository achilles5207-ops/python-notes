# 📘 Comprehensive Textbook Guide: Module 4 - File Handling & Database Connectivity

## Chapter 13: File Handling and Command Line Arguments

### 13.1 Introduction to File Handling
Variables and data structures (lists, dicts) reside in RAM, meaning they are volatile. When the program terminates, the data is lost. To store data permanently (non-volatile storage), we use files on a hard drive.

#### Types of Files
1.  **Text Files:** Store data as plain text strings. Human-readable (e.g., `.txt`, `.py`, `.csv`). Each line ends with an End-Of-Line (EOL) character like `\n`.
2.  **Binary Files:** Store data in machine-readable binary format (0s and 1s). Used for images, audio, video, or serialized Python objects.

### 13.2 File Operations: Open, Read, Write, Close

#### Opening and Closing Files
We use the `open()` function to open a file. It returns a file object. It's crucial to always `close()` the file to free up system resources.
```python
# Syntax: file_obj = open("filename", "mode")
f = open("my_data.txt", "w") # Open for writing
# ... do operations ...
f.close() # Close the file
```

#### The `with` Statement (Context Manager)
The safest and most Pythonic way to handle files. It guarantees that the file is automatically closed when the block ends, even if an exception occurs inside the block.
```python
with open("my_data.txt", "w") as f:
    f.write("Hello World")
# No need to call f.close(), it is done automatically
```

#### File Opening Modes
*   `'r'`: Read (Default). Opens file for reading. Errors if file doesn't exist.
*   `'w'`: Write. Opens file for writing. **Creates a new file or truncates (overwrites) an existing one.**
*   `'a'`: Append. Opens file for writing. **Appends to the end** if it exists, creates it if it doesn't.
*   `'r+'`: Read & Write.
*   `'b'`: Binary mode. Can be combined with others (e.g., `'rb'`, `'wb'`).

### 13.3 Reading and Writing Text Files

#### Writing Data
*   `write(string)`: Writes a single string to the file.
*   `writelines(list_of_strings)`: Writes a list of strings to the file. (Note: It does not add newlines automatically).
```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("data.txt", "w") as f:
    f.writelines(lines)
```

#### Reading Data
*   `read(size)`: Reads the entire file as a single string (or up to `size` bytes).
*   `readline()`: Reads a single line as a string.
*   `readlines()`: Reads all lines and returns them as a List of strings.
```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```

### 13.4 Binary Files and Serialization (Pickling)
To write Python objects (like dictionaries or lists) directly into a file, we must serialize them into a byte stream. This is called Pickling. We use the `pickle` module.
*   `pickle.dump(object, file)`: Serializes object to a file.
*   `pickle.load(file)`: Deserializes the byte stream back into a Python object.
```python
import pickle

my_dict = {"name": "Alice", "score": 95}

# Pickling (Writing Binary)
with open("data.dat", "wb") as f:
    pickle.dump(my_dict, f)

# Unpickling (Reading Binary)
with open("data.dat", "rb") as f:
    loaded_dict = pickle.load(f)
    print(loaded_dict["name"]) # Alice
```

### 13.5 Handling CSV Files
CSV (Comma Separated Values) files are plain text files used to store tabular data. Python provides a built-in `csv` module.
```python
import csv

# Writing to CSV
with open('students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])  # Write Header
    writer.writerow(["Alice", 20])    # Write Row

# Reading from CSV
with open('students.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row) # Prints lists: ['Name', 'Age'], ['Alice', '20']
```

### 13.6 Command Line Arguments
Command-line arguments are passed to your script when executing it from the terminal (e.g., `python script.py arg1 arg2`).
Python stores these arguments in a list called `sys.argv` from the `sys` module.
*   `sys.argv[0]` is ALWAYS the name of the script itself.
*   `sys.argv[1]` and beyond are the actual arguments passed.
*(Note: All arguments are read as Strings).*
```python
import sys
# Run as: python my_script.py Alice 25
if len(sys.argv) == 3:
    print(f"Script Name: {sys.argv[0]}")
    print(f"Name: {sys.argv[1]}")
    print(f"Age: {sys.argv[2]}")
```

---

## Chapter 14: Database Connectivity

### 14.1 Introduction to Database Connectivity
A database is an organized collection of structured data. Python can interact with relational databases (like MySQL, PostgreSQL, SQLite, Oracle) using specific drivers/connectors. 
For this module, we'll use `sqlite3` as it comes built-in with Python and requires no server installation, but the syntax is nearly identical for MySQL (using `mysql-connector-python`).

### 14.2 The Five Steps of Database Connectivity
1.  **Import the module:** e.g., `import sqlite3` or `import mysql.connector`.
2.  **Create a Connection:** Establish a connection to the database file or server. Returns a Connection Object.
3.  **Create a Cursor:** A cursor is an object that allows you to execute SQL queries and fetch results.
4.  **Execute Query:** Use the `execute()` method to run SQL commands (INSERT, UPDATE, DELETE, SELECT).
5.  **Commit and Close:** Save the changes (Transaction Management) and close the connection.

### 14.3 Connection Parameters
If connecting to a standalone server like MySQL, you provide parameters:
```python
# import mysql.connector
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="password123",
#     database="my_database"
# )
```

### 14.4 Executing Queries and Transaction Management

#### Transaction Management (`commit()` and `rollback()`)
Any operation that *modifies* the database (INSERT, UPDATE, DELETE) is a Transaction. It is NOT saved to the database until you explicitly call `conn.commit()`. If something goes wrong, you can undo the transaction using `conn.rollback()`.

#### Step-by-Step Example (SQLite)
```python
import sqlite3

# Step 1: Connect (Creates 'school.db' file if it doesn't exist)
conn = sqlite3.connect('school.db')

# Step 2: Create a Cursor
cursor = conn.cursor()

# Step 3: Execute Queries
# Create Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        marks REAL
    )
''')

# Insert Data
cursor.execute("INSERT INTO Students (name, marks) VALUES ('Alice', 95.5)")
cursor.execute("INSERT INTO Students (name, marks) VALUES ('Bob', 80.0)")

# Step 4: Commit changes to the database
conn.commit()

# Step 5: Close connection
conn.close()
```

### 14.5 Fetching Data (SELECT queries)
When you run a `SELECT` query, you don't modify data, so you don't need to `commit()`. Instead, you fetch the results.
*   `fetchone()`: Retrieves the next row of a query result set as a tuple. Returns `None` if no more rows are available.
*   `fetchall()`: Fetches all remaining rows and returns them as a List of Tuples.
```python
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM Students WHERE marks > 85")

# Fetch all matching records
records = cursor.fetchall()

for row in records:
    print(f"ID: {row[0]}, Name: {row[1]}, Marks: {row[2]}")

conn.close()
```

---

## 📝 Comprehensive Textbook Exercises and Solutions

### Conceptual Questions

**Q1. What is the difference between `'w'` and `'a'` modes when opening a text file?**
*Answer:* Both open a file for writing. However, the `'w'` (write) mode will completely overwrite any existing content in the file (it truncates it to zero length). The `'a'` (append) mode will leave the existing content intact and place the file pointer at the end of the file, meaning any new writes will be added after the existing data.

**Q2. Explain Pickling and Unpickling in Python.**
*Answer:* Pickling is the process of converting a Python object hierarchy (like a complex dictionary or a custom class object) into a byte stream (serialization) so it can be written to a binary file. Unpickling is the inverse process of reading a byte stream from a binary file and reconstructing the original Python object (deserialization).

**Q3. Why is the `with` statement preferred over explicitly calling `open()` and `close()`?**
*Answer:* The `with` statement creates a context manager. It guarantees that the file is properly closed immediately after the block of code inside the `with` statement completes, *even if an exception (error) occurs* within that block. This prevents resource leaks and file corruption.

**Q4. What is a Database Cursor?**
*Answer:* A cursor is a database object used to traverse the records in a database. In Python, the Cursor object acts as an intermediary that allows you to execute SQL commands line-by-line and fetch the result sets returned by `SELECT` queries.

**Q5. What is the role of `commit()` in database connectivity?**
*Answer:* The `commit()` method confirms the current transaction. Any changes made to the database (via INSERT, UPDATE, or DELETE commands) remain temporary and hidden from other database connections until `commit()` is called to permanently save them to the database.

### Programming Problems

**P1. Write a program to read a text file `poem.txt` and count the number of words in it.**
```python
try:
    with open('poem.txt', 'r') as file:
        content = file.read()
        # split() without arguments splits by whitespace, effectively extracting words
        words = content.split()
        print(f"Total number of words: {len(words)}")
except FileNotFoundError:
    print("Error: poem.txt does not exist.")
```

**P2. Write a program to write a dictionary containing employee data into a binary file `emp.dat` using pickle, and then read it back.**
```python
import pickle

employee_data = {"emp_id": 101, "name": "John Doe", "salary": 75000}

# Write to binary file
with open('emp.dat', 'wb') as f:
    pickle.dump(employee_data, f)
    print("Data serialized to emp.dat")

# Read from binary file
with open('emp.dat', 'rb') as f:
    loaded_data = pickle.load(f)
    print("Data deserialized:")
    print(loaded_data)
```

**P3. Write a Python script that takes two numbers as Command Line Arguments, adds them, and prints the result.**
```python
import sys

# Remember sys.argv[0] is the script name
if len(sys.argv) != 3:
    print("Usage: python script.py <num1> <num2>")
else:
    try:
        # Arguments are strings, so cast to float
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        result = num1 + num2
        print(f"The sum is: {result}")
    except ValueError:
        print("Error: Please provide valid numbers.")
```

**P4. Write a program to connect to an SQLite database `inventory.db`, create a table `Products`, and insert two records.**
```python
import sqlite3

def setup_database():
    try:
        # 1. Connect
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()

        # 2. Create Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL
            )
        ''')

        # 3. Insert Records
        # Using parameterized queries (?) prevents SQL Injection attacks
        cursor.execute("INSERT INTO Products (name, price) VALUES (?, ?)", ("Laptop", 999.99))
        cursor.execute("INSERT INTO Products (name, price) VALUES (?, ?)", ("Mouse", 25.50))

        # 4. Commit changes
        conn.commit()
        print("Table created and records inserted successfully.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        # 5. Close connection
        if conn:
            conn.close()

setup_database()
```

**P5. Write a program to fetch and display all products from the `inventory.db` database where the price is greater than 100.**
```python
import sqlite3

try:
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # Parameterized SELECT query
    cursor.execute("SELECT * FROM Products WHERE price > ?", (100,))
    
    # Fetch all matching results
    records = cursor.fetchall()
    
    if len(records) == 0:
        print("No products found over $100.")
    else:
        print("Products over $100:")
        for row in records:
            print(f"ID: {row[0]}, Name: {row[1]}, Price: ${row[2]}")

except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
```
