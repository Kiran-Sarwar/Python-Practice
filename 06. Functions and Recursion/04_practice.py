# Author = Kiran
# Date = 7th July, 2026
"""
WAF to find the factorial of n.
"""

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
# Example usage
number = 5
print(f"Factorial of {number} is: {factorial(number)}")  # Output: Factorial of 5 is: 120