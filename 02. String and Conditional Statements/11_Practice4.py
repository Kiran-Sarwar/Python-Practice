# Author: Kiran Sarwar
# Date: 1st July, 2026
"""
# Description: F-String Question:
Given:
python
name = "Kiran"
cgpa = 3.79
Write an f-string that prints:
Kiran's CGPA is 3.79 out of 4.00
Requirements:

Use f-string formatting only (no .format() or %)
cgpa must show exactly 2 decimal places, even if trailing zeros need to be added
"""

name = "Kiran"
cgpa = 3.79
print(f"{name}'s CGPA is {cgpa:.2f} out of 4.00")