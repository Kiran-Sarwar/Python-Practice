# Author = Kiran
# Date = 5th July, 2026
"""
WAP to find the factorial of first n  numbers using for loop.
"""

n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("The factorial of first n numbers is:", factorial)