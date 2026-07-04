# Author = Kiran
# Date = 4th July, 2026
"""
Search for a number 25 in the following list using while loop
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(numbers):
    if numbers[i] == 25:
        print("Number found at index:", i)
        break
    i += 1
else:
        print("Number not found in the list.")