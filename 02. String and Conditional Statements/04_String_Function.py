# Author: Kiran Sarwar
# Date: 29th June 2026
# Description: This program demonstrates various string functions in Python.

str = " I am a student of Python programming language. "
print(str.endswith("ge. "))  # Output: True
print(str.startswith(" I am"))  # Output: True
print(str.capitalize())  # Output: ' I am a student of python programming language. '
print(str.replace("Python", "Java"))  # Output: ' I am a student of Java programming language. '
print(str.find("student"))  # Output: 8
print(str.count("a"))  # Output: 5
