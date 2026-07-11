# Author = Kiran
# Date = 11th July, 2026
"""
WARF to calculate the sum of first n natural numbers using recursion
"""

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
    
sum(10) # Output: 55