# Author = Kiran
# Date = 2nd July, 2026
# Description = Understanding the concept of set in python

set1 = {1, 2, 3, 4, 5} # Creates a set with integer values
set2 = {1, 2, 3, 3, 3} # repeated elements will store onlt once, so it is resolved to {1, 2, 3}

# Can store tuple in set but not list and dictionary because they are mutable
set3 = {(1, 2), (3, 4), (5, 6)} # Creates a set with tuple values

null_set = set() # Creates an empty set

collection = {1, 2, "World", "Hello"} # Order of the elements in the set is not guaranteed, so it can be printed in any order. Evertime to print the set the order will be different.

print(len(collection)) # total number of elements in the set
