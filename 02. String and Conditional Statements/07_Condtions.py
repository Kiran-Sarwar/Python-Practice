# Author: Kiran Sarwar
# Date: 29th June 2026
# Description: This program demonstrates the use of conditional statements in Python.

age = 21

if age >= 18:
    print("You are eligible to vote.")
elif age < 18:
    print("You are not eligible to vote.")

print("Thank you for using the voting eligibility checker.")

#nesting of if-else statements

if age >= 18:
    if age >= 21:
        print("You are eligible to vote and drink alcohol.")
    else:
        print("You are eligible to vote but not to drink alcohol.")
elif age < 18:
    print("You are not eligible to vote or drink alcohol.")

print("Thank you for using the voting and drinking eligibility checker.")