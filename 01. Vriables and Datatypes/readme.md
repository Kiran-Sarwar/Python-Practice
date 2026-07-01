# 01 Variables and Datatypes

##  Overview
This folder contains foundational Python concepts covering variables, data types, operators, and user input. These are essential building blocks for any Python programmer.

##  Learning Objectives
By completing this section, I learned:
-  How to declare and use variables
-  Understanding Python's data types (int, float, str, bool)
-  Type conversion between different data types
-  Using the print() function for output
-  Taking user input with input()
-  Arithmetic, comparison, and logical operators
-  Proper whitespace and indentation in Python

##  Files in This Folder

| File | Description |
|------|-------------|
| `01_First_program.py` | First Python program - basic print and syntax |
| `02_Variables.py` | Variable declaration and naming conventions |
| `03_Datatypes.py` | Exploring int, float, str, bool data types |
| `04_PrintSum.py` | Print function fundamentals and arithmetic operations |
| `05_Operators.py` | Arithmetic, comparison, and logical operators |
| `06_TypeConversion.py` | Converting between int, float, str, bool types |
| `07_input.py` | Taking user input and processing it |
| `08_Practice1.py` | Practice exercises combining basic concepts |
| `09_Practice2.py` | Advanced practice problems and applications |

##  Key Concepts

### Variables
Variables are containers for storing data values. Python uses dynamic typing.
```python
age = 25
name = "Kiran"
height = 5.9
is_student = True
```

### Data Types
- **int** - Whole numbers (-5, 0, 100)
- **float** - Decimal numbers (3.14, 2.5)
- **str** - Text ("Hello", 'World')
- **bool** - True or False

### Type Conversion
```python
x = int("10")        # String to int
y = str(25)          # Int to string
z = float("3.14")    # String to float
```

### Operators
```python
# Arithmetic: +, -, *, /, //, %, **
10 + 5, 10 - 5, 10 * 5, 10 / 5

# Comparison: ==, !=, >, <, >=, <=
10 == 5, 10 > 5, 10 <= 5

# Logical: and, or, not
True and False, True or False, not True
```

##  How to Run
```bash
python 01_First_program.py
python 02_Variables.py
python 03_Datatypes.py
python 04_PrintSum.py
python 05_Operators.py
python 06_TypeConversion.py
python 07_input.py
python 08_Practice1.py
python 09_Practice2.py
```

##  What I Learned
- Variables must be declared before use
- Python uses **dynamic typing** — you don't specify data types upfront
- Whitespace and indentation matter — they're part of Python syntax
- The `input()` function always returns a **string** — convert with int()/float() if needed
- Understanding operators is crucial for conditionals and loops
- ASCII vs Unicode: ASCII is limited (0-127), Unicode covers all languages and emojis

##  Challenges & Solutions
- Challenge: Understanding why `input()` returns strings
- Solution: Always convert input to appropriate type using int(), float()

- Challenge: Whitespace errors in Python
- Solution: Use 4 spaces for indentation consistently

##  Resources Used
- Apna College (YouTube) - Python Full Course
- Python Official Documentation

##  Next Steps
-  Complete Variables and Datatypes fundamentals
-  Master Conditional Statements (if/elif/else)
-  Learn about String Operations
-  Build a console-based project combining all these topics

---
Status:  Completed | Date: June 28, 2026 | Time Spent: ~1-2 hours