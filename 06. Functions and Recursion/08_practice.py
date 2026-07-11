# Author = Kiran
# Date = 11th July, 2026
"""
WARF to print all elements in a list.
Hint" use list and indexes as parameters
"""

def element_of_lists(list, idx=0):
    if (idx == len(list)): 
         return
    print (list[idx])
    element_of_lists(list, idx+1)

fruits  = ["Apple", "Banana", "Orange"]
element_of_lists(fruits)