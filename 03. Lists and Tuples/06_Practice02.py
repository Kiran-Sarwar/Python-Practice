# Author = Kiran
# Date = 30th June 2026
# Description = WAP to check if a list contains a palindrome of elements.

list = [2, 3, 4, 5, 4, 3, 2] # Example list
# Check if the list is a palindrome
list1 = list.copy()
list1.reverse()
if list == list1:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")
