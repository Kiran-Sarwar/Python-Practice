# Author = Kiran
# Date = 7th July, 2026
"""
WAF to print the elements of list in a single line.
"""

def print_list_elements(lst):
    for element in lst:
        print(element, end=' ')
    print()  # For a new line after printing all elements

# Example usage
my_list = [1, 2, 3, 4, 5]
print_list_elements(my_list)  # Output: 1 2 3 4 5