# Author = Kiran
# Date: 16th July, 2026
"""
Project: Recursive Countdown/Sum Toolkit
A console menu-based tool where the user picks an operation, and each one is solved recursively (no loops for the core logic).
Core Features (required)

Countdown — takes a number, recursively prints it counting down to 0 (or 1), with a "Liftoff!" style message at the end
Sum of N natural numbers — recursively calculates 1 + 2 + 3 + ... + n
Sum of digits — recursively adds up digits of a number (you already wrote this one — reuse it)
Menu system — loop that lets the user pick an option, run it, and either continue or exit

Stretch Goals (optional, up to you)

Add factorial as a 4th menu option (you already wrote this too)
Input validation — handle bad input (like letters instead of numbers) without crashing
A "countdown by custom step" (e.g., count down by 2s or 3s) — this pushes your recursive case a bit further

Structure Suggestion

Each operation = its own function, recursion inside it
Main menu loop handles user interaction and calls the right function
Keep print for user-facing output, but the recursive functions themselves should return values where it makes sense (e.g., sum functions return the total, countdown can just print inside itself since there's no value to hand back)
"""


def countdown(n):
    if n == 0:
        print("Liftoff! 🚀")
        return

    print(n)
    countdown(n - 1)

def sum_natural(n):
    if n <= 0:
        return 0
    return n + sum_natural(n - 1)

def sum_digits(num):
    if num == 0:
        return 0

    return num % 10 + sum_digits(num // 10)

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

def menu():
    print("\n===== Recursive Toolkit =====")
    print("1. Countdown")
    print("2. Sum of Natural Numbers")
    print("3. Sum of Digits")
    print("4. Factorial")
    print("5. Exit")

def main():

    while True:

        menu()

        choice = input("Enter your choice: ")
        if choice == "1":

            number = int(input("Enter a number: "))

            countdown(number)
        elif choice == "2":

            number = int(input("Enter a number: "))

            print("Sum =", sum_natural(number))
        elif choice == "3":

            number = int(input("Enter a number: "))

            print("Sum of digits =", sum_digits(number))
        elif choice == "4":

            number = int(input("Enter a number: "))

            print("Factorial =", factorial(number))
        elif choice == "5":
            print("Thank you for using the Recursive Toolkit!")
            break
        else:
            print("Invalid choice.")

main()