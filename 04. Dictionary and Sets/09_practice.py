# Author = Kiran
# Date = 2nd July, 2026
"""
Figure out a way to store 9 and 9.0 as seperate values in a set. (You can take help of built in datatypes).
"""

set = {(9, "int"), (9.0, "float")} # Storing 9 and 9.0 as tuple with their datatype as string to differentiate them
set = {9, "9.0"} # Storing 9 and 9.0 as separate values in a set, but they will be considered the same because they are equal in value
print(set) # Prints the set with 9 and 9.0 as separate values