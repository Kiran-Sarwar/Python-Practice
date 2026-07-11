# Author = Kiran
# Date = 11th July, 2026
# Description = Understanding Recursion in Python

def show(n):
    if n > 0:
        print(n)
        show(n - 1)

show(5)  # Output: 5 4 3 2 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120