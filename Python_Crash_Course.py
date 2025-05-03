

'''
PYTHON CRASH COURSE:

# 🔶- Table of Contents

## Introduction to Python
- Overview of Python
- Key features and advantages
- Common use cases (Web Dev, Data Science, ML, etc.)
- Python history and philosophy

## 1. Variables and Data Types
- Integer (whole numbers)
- Float (decimal numbers)
- String (text)
- Boolean (True/False)
- List (ordered, mutable collection)
- Tuple (ordered, immutable collection)
- Dictionary (key-value pairs)
- Set (unordered, unique elements)

## 2. Basic Operations
- Arithmetic operations (+, -, *, /, etc.)
- String operations (concatenation, methods)
- List operations (append, access elements)

## 3. Control Flow
- Conditional statements (if-elif-else)
- For loops (iteration)
- While loops (conditional repetition)
- List comprehensions

## 4. Lambda Functions
- Anonymous functions
- Practical examples

## 5. Map, Filter, Reduce
- Map function
- Filter function
- Reduce function

## 6. Working with JSON
- Converting dict to JSON
- Parsing JSON to Python objects

## 7. Functions
- Defining functions
- Parameters and arguments
- Return values
- Default parameters

## 8. File I/O Operations
- Writing to files
- Reading from files
- File handling best practices

## 9. Exception Handling
- Try-except blocks
- Handling specific exceptions
- Finally clause

## 10. Classes and OOP
- Class definition
- Attributes and methods
- Object instantiation
- Inheritance basics

## 11. Modules
- Importing modules
- Using standard library modules
- Module aliases

## 12. Working with Dates
- datetime module
- Date formatting
- Timedelta operations

## 13. List Comprehensions
- Basic list comprehensions
- Conditional comprehensions
- Dictionary comprehensions

## And more!


This Module on Python Crash Course covers fundamental Python concepts with examples, comments, and expected outputs.
Run each section sequentially to learn Python basics.

Python is a high-level, interpreted programming language known for its simplicity and readability.
Created by Guido van Rossum in 1991, Python has become one of the most popular languages for:
- Web development (Django, Flask)
- Data science (Pandas, NumPy)
- Machine learning (TensorFlow, PyTorch)
- Automation and scripting
- Scientific computing

Key Features:
- Easy-to-learn syntax
- Cross-platform compatibility
- Large standard library
- Strong community support
- Dynamically typed

'''

# ===========================
# 1. VARIABLES AND DATA TYPES
# ===========================
print("\n=== 1. VARIABLES AND DATA TYPES ===")
print('Variables are containers for storing data values. Python has various data types:')

# Integer - whole numbers without decimals
age = 25
print(f"Age: {age} (type: {type(age)})")  # Output: Age: 25 (type: <class 'int'>)

# Float- numbers with decimals
price = 19.99
print(f"Price: {price} (type: {type(price)})")  # Output: Price: 19.99 (type: <class 'float'>)

# String - sequence of characters (text)
name = "Mary"
print(f"Name: {name} (type: {type(name)})")  # Output: Name: Mary (type: <class 'str'>)

# Boolean - logical values (True/False)
is_student = True
print(f"Is student: {is_student} (type: {type(is_student)})")  # Output: Is student: True (type: <class 'bool'>)

# List - ordered, mutable collection
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits} (type: {type(fruits)})")  # Output: Fruits: ['apple', 'banana', 'cherry'] (type: <class 'list'>)

# Tuple - ordered, immutable collection
coordinates = (10.0, 20.0)
print(f"Coordinates: {coordinates} (type: {type(coordinates)})")  # Output: Coordinates: (10.0, 20.0) (type: <class 'tuple'>)

# Dictionary - key-value pairs
person = {"name": "Bob", "age": 30}
print(f"Person: {person} (type: {type(person)})")  # Output: Person: {'name': 'Bob', 'age': 30} (type: <class 'dict'>)

# Set - unordered, unique elements
unique_numbers = {1, 2, 3, 2, 1}
print(f"Unique numbers: {unique_numbers} (type: {type(unique_numbers)})")  # Output: Unique numbers: {1, 2, 3} (type: <class 'set'>)

# =======================================
# 2. BASIC OPERATIONS - Working with Data
# =======================================
print("\n=== 2. BASIC OPERATIONS ===")

# Arithmetic operations
a, b = 10, 3
print(f"{a} + {b} = {a + b}")  # Output: 10 + 3 = 13
print(f"{a} - {b} = {a - b}")  # Output: 10 - 3 = 7
print(f"{a} * {b} = {a * b}")  # Output: 10 * 3 = 30
print(f"{a} / {b} = {a / b}")  # Output: 10 / 3 = 3.333...
print(f"{a} // {b} = {a // b}")  # Output: 10 // 3 = 3 (floor division)
print(f"{a} % {b} = {a % b}")  # Output: 10 % 3 = 1 (modulus)
print(f"{a} ** {b} = {a ** b}")  # Output: 10 ** 3 = 1000 (exponent)

# String operations
greeting = "Hello"
name = "Grace"
print(greeting + " " + name)  # Output: Hello Grace
print(f"{greeting.lower()} {name.upper()}")  # Output: hello GRACE
print(f"Length of '{greeting}': {len(greeting)}")  # Output: Length of 'Hello': 5

# List operations
numbers = [1, 2, 3]
numbers.append(4)
print(f"Appended list: {numbers}")  # Output: Appended list: [1, 2, 3, 4]
print(f"Second element: {numbers[1]}")  # Output: Second element: 2
print(f"Last element: {numbers[-1]}")  # Output: Last element: 4

# ==================================
# 3. CONTROL FLOW - Making Decisions
# ==================================
print("\n=== 3. CONTROL FLOW ===")
print('Control flow structures determine the order in which code executes:')

# If-elif-else - conditional execution
temperature = 22
print("Weather report:")
if temperature > 30:
    print("It's hot!")
elif 20 <= temperature <= 30:
    print("It's pleasant.")  # This will execute
else:
    print("It's cold!")
# Output: Weather report: It's pleasant.

# For loop - iteration over a sequence
print("\nCounting to 5:")
for i in range(1, 6):
    print(i, end=" ")  # Output: 1 2 3 4 5


# Example 2:
for i in range(1, 4):
    print("Counting:", i)
# Output:
# Counting: 1
# Counting: 2
# Counting: 3

# While loop - repeated execution while condition is true
print("\n\nCountdown:")
count = 5
while count > 0:
    print(count, end=" ") #Values will be printed horizontally
    count -= 1  # Output: 5 4 3 2 1

# Example 2:
count = 0
while count < 2:
    print("While loop count:", count) #Values will be printed vertically
    count += 1
# Output:
# While loop count: 0
# While loop count: 1    

# List comprehension - concise way to create lists
squares = [x**2 for x in range(1, 6)] # Each value of 1-5 gets squared
print(f"\n\nSquares: {squares}")  # Output: Squares: [1, 4, 9, 16, 25]

#=================================
# 4. ----- LAMBDA FUNCTIONS -----
#=================================

double = lambda x: x * 2
print("Double 5:", double(5))
# Output: Double 5: 10


#==================================
#5. ----- MAP, FILTER, REDUCE -----
#==================================

nums = [1, 2, 3, 4, 5]

#======
#a. Map
#======

doubled = list(map(lambda x: x * 2, nums))
print("Doubled:", doubled)
# Output: Doubled: [2, 4, 6, 8, 10]

#=========
# b.Filter
#=========

even = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", even)
# Output: Even numbers: [2, 4]


#==========
# c. Reduce
#==========

from functools import reduce
total = reduce(lambda x, y: x + y, nums)
print("Sum using reduce:", total)
# Output: Sum using reduce: 15


#================================
# 6.----- WORKING WITH JSON -----
#================================

import json

data = {
    "name": "Harry",
    "skills": ["Python", "R", "SQL"]
}

# Convert dict to JSON string
json_data = json.dumps(data)
print("JSON String:", json_data)
# Output: JSON String: {"name": "Harry", "skills": ["Python", "R", "SQL"]}

# Convert JSON string back to dict
parsed = json.loads(json_data)
print("Parsed JSON:", parsed["skills"])
# Output: Parsed JSON: ['Python', 'R', 'SQL']

# ============
# 7. FUNCTIONS
# ============
print("\n=== 4. FUNCTIONS ===")

# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Harry"))  # Output: Hello, Harry!

# Function with default argument
def power(base, exponent=2):
    return base ** exponent

print(f"5 squared: {power(5)}")  # Output: 5 squared: 25
print(f"2 cubed: {power(2, 3)}")  # Output: 2 cubed: 8

# Example 2:
def power(base, exponent=2):
    return base ** exponent

print("Power:", power(6))
# Output: Power: 36
print("Power with exponent:", power(6, 6))
# Output: Power with exponent: 36


# ===========
# 8. FILE I/O
# ===========
print("\n=== 5. FILE I/O ===")

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, Python!\nThis is a test file.")

# Reading from a file
print("File contents:")
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
# Output:
# File contents:
# Hello, Python!
# This is a test file.


# Example 2:
# Write to file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a test.\n")

# Read from file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:", content)
# Output: File content: Hello, this is a tes



# =====================
# 9. EXCEPTION HANDLING
# =====================
print("\n=== 6. EXCEPTION HANDLING ===")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Output: Cannot divide by zero!
else:
    print(f"Result: {result}")
finally:
    print("This always executes")  # Output: This always executes


# Example 2:

try:
    num = int("abc")  # Invalid conversion
except ValueError as e:
    print("Caught an error:", e)
# Output: Caught an error: invalid literal for int() with base 10: 'abc'


# ==================
# 10. CLASSES AND OOP
# ==================
print("\n=== 7. CLASSES AND OOP ===")

class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    # Initializer
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Create instances
buddy = Dog("Buddy", 5)
milo = Dog("Milo", 3)

print(buddy.description())  # Output: Buddy is 5 years old
print(milo.speak("Woof!"))  # Output: Milo says Woof!
print(f"All dogs are {Dog.species}")  # Output: All dogs are Canis familiaris

# ==========
# 11. MODULES
# ==========
print("\n=== 8. MODULES ===")

# Importing math module
import math

print(f"Square root of 16: {math.sqrt(16)}")  # Output: Square root of 16: 4.0
print(f"Pi constant: {math.pi:.2f}")  # Output: Pi constant: 3.14

# Import with alias
import random as rnd
print(f"Random number: {rnd.randint(1, 100)}")  # Output: Random number: [random between 1-100]

# =====================
# 12. WORKING WITH DATES
# =====================
print("\n=== 9. WORKING WITH DATES ===")

from datetime import datetime, timedelta

now = datetime.now()
print(f"Current datetime: {now}")  # Output: Current datetime: [current datetime]

tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow.date()}")  # Output: Tomorrow: [current date + 1 day]

# Formatting
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted: {formatted}")  # Output: Formatted: [YYYY-MM-DD HH:MM:SS]

# ==========================
# 13. LIST OF COMPREHENSIONS
# ==========================
print("\n=== 10. LIST COMPREHENSIONS ===")

# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squared = [n**2 for n in numbers]
print(f"Squared numbers: {squared}")  # Output: Squared numbers: [1, 4, 9, 16, 25]

# Example 2:
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)
# Output: Squares: [1, 4, 9, 16, 25]

# With condition
evens = [n for n in numbers if n % 2 == 0]
print(f"Even numbers: {evens}")  # Output: Even numbers: [2, 4]

# Dictionary comprehension
square_dict = {n: n**2 for n in numbers}
print(f"Square dictionary: {square_dict}")  # Output: Square dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#============================
# 14. ----- BASIC REGEX -----
#============================

import re

text = "Email me at harry@example.com"
match = re.search(r'\b[\w.-]+@[\w.-]+\.\w{2,4}\b', text)
if match:
    print("Found email:", match.group())
# Output: Found email: harry@example.com


#====================================
# 15. ----- BASIC NUMPY EXAMPLE -----
#====================================

import numpy as np

arr = np.array([[1, 2], [3, 4]])
print("Numpy array:\n", arr)
# Output:
# Numpy array:
# [[1 2]
#  [3 4]]
print("Array mean:", arr.mean())
# Output: Array mean: 2.5

#========================================
#16. ----- BASIC MATPLOTLIB EXAMPLE -----
#========================================

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Simple Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
# Output: Opens a line chart in a separate window

print("\nPython Crash Course Complete!")



