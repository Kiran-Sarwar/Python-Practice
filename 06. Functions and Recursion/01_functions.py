# Author = Kiran
# Date = 7th July, 2026
# Description = Understanding functions in Python

def sum(a, b):
    """
    This function takes two numbers as input and returns their sum.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b

print(sum(5, 10))  # Output: 15
print(sum(3.5, 2.5))  # Output: 6.0

def print_greeting(name):
    """
    This function takes a name as input and prints a greeting message.
    
    Parameters:
    name (str): The name of the person to greet.
    
    Returns:
    None
    """
    print(f"Hello, {name}! Welcome to the world of Python functions.")

print_greeting("Alice")  # Output: Hello, Alice! Welcome to the world of Python functions.

def average_of_three(a, b, c):
    """
    This function takes three numbers as input and returns their average.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    c (int or float): The third number.
    
    Returns:
    float: The average of the three numbers.
    """
    return (a + b + c) / 3

print(average_of_three(10, 20, 30))  # Output: 20.0