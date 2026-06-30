# Author = Kiran
# Date = 30th June 2026
# Description = This file contains the code for tuple operations in Python.

tup=() # Valid tuple
print(tup)
print(type(tup))

tup1=(1,) # , is used to define a single element tuple otherwise it will be considered as an integer
print(tup1)
print(type(tup1))

tup2=(1,2,3,4,5) # Multiple element mein last par , na lagaye tu phir bhi tuple consider ho ga
print(tup2)
print(type(tup2))

# Tuple is immutable, so we cannot change the values of tuple after creation

# Tuple Slicing
tup3=(1,2,3,4,5,6,7,8,9,10)
print(tup3[0:5]) # Slicing from index 0 to 4
print(tup3[2:7]) # Slicing from index 2 to 6
print(tup3[5:10]) # Slicing from index 5 to 9
