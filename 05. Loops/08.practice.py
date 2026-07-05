# Author = Kiran
# Date = 5th July, 2026
"""
Search for a number 25 in the following tuple using for loop
"""

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

for i in nums:
    if i == 25:
        print("Number found:", i)
        break
    print("finding number:")