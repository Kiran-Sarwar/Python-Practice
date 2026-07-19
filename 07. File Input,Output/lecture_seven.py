# Author = Kiran
# Date = 19th July, 2026
# ==========================================
# FILE HANDLING IN PYTHON
# ==========================================

# Opening a file
f = open("demo.txt", "r")      # If the file is in another folder, use its full path.

data = f.read()
print(data)
print(type(data))

f.close()


# ==========================================
# FILE MODES
# ==========================================

"""
r  = Read mode (Default)
     - Opens file for reading.
     - Gives an error if file doesn't exist.

w  = Write mode
     - Overwrites (truncates) the entire file first.
     - Creates the file if it doesn't exist.

x  = Create mode
     - Creates a new file.
     - Gives an error if the file already exists.

a  = Append mode
     - Adds data at the end of the file.
     - Doesn't overwrite existing data.
     - Creates the file if it doesn't exist.

b  = Binary mode

t  = Text mode (Default)

+  = Update mode
     - Allows both reading and writing.
"""


# ==========================================
# READING A FILE
# ==========================================

f = open("demo.txt", "r")

# Read the entire file
data = f.read()
print(data)

# Read only first 5 characters
f.seek(0)          # Move cursor back to the beginning
data = f.read(5)
print(data)

# Read one line at a time
f.seek(0)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

"""
Important:

Suppose you print the whole file using f.read().

After that, if you try:

line = f.readline()

It will print an empty string because the cursor is already
at the end of the file.

The main thing to understand in file handling is the
cursor (or file pointer).

Use f.seek(0) to move the cursor back to the beginning.
"""


# ==========================================
# WRITING TO A FILE
# ==========================================

# Write mode (Overwrites everything)

f = open("demo.txt", "w")
f.write("I want to learn JavaScript.")
f.close()


# Append mode (Adds data at the end)

f = open("demo.txt", "a")
f.write("\nThen I will move to React JS.")
f.close()


# ==========================================
# DIFFERENCE BETWEEN r+, w+, AND a+
# ==========================================

"""
r+ = Read + Write
     - Does NOT truncate the file.
     - Cursor starts at the beginning.

w+ = Read + Write
     - Truncates (overwrites) the file first.

a+ = Read + Append
     - Does NOT truncate.
     - Cursor starts at the end.

Main thing to understand:
Where is the cursor (pointer)?
"""


# ==========================================
# WITH SYNTAX (Best Practice)
# ==========================================

"""
Using 'with' automatically closes the file.
No need to call f.close().
"""

with open("demo.txt", "a") as f:
    f.write("\nLearning Python File Handling.")


# ==========================================
# DELETING A FILE
# ==========================================

"""
Using the os module.

Module:
A module is like a code library written by another programmer.
It contains useful functions that we can use.
"""

import os

os.remove("sample.txt")