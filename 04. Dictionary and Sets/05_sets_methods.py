# Author = Kiran
# Date = 2nd July, 2026
# Description = Understanding the concept of methods in sets

set1 = {1, 2, 3, 4, 5}

set1.add(6) # Adds the element 6 to the set
set1.remove(3) # Removes the element 3 from the set, if it exists. If it does not exist, it will raise a KeyError.
set1.clear() # Removes all the elements from the set
set1.pop() # Removes and returns an arbitrary element from the set. If the set is empty, it will raise a KeyError.
set2 = {1, 2, 3, 4, 5}
set1.union(set2) # Returns a new set that contains all the elements from both sets
set1.intersection(set2) # Returns a new set that contains only the elements that are common to both sets