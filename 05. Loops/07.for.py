# Author = Kiran
# Date = 5th July, 2026
# Description = This program demonstrates the use of a for loop

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for val in nums:
    print(val)

str = "Hello, World!"

for char in str:
    print(char)
else:
    print("End of string reached.")
# why used else in for loop? The `else` clause in a `for` loop is executed after the loop has completed all iterations, but only if the loop was not terminated by a `break` statement. In this case, the `else` block will execute after the loop has finished iterating through all characters in the string "Hello, World!" and will print "End of string reached."

# for example
str = "Python"

for char in str:
    if char == 'o':
        print("Character 'o' found, breaking the loop.")
        break
    print(char)
else:
    print("End of string reached.")