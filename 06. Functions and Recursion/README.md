# 06. Functions and Recursion

This folder covers functions and recursion in Python — how to define and call functions, the difference between parameters and arguments, return values, variable scope, and how recursion works with base cases and recursive cases.

## Concepts Covered

| Concept | Description |
|---|---|
| Parameters vs Arguments | Parameters are placeholders in a function definition; arguments are the actual values passed in when calling it |
| Return vs Print | `return` sends a value back to the caller so it can be stored or reused; `print` only displays it on screen |
| Default Parameters | Function parameters can have default values, used when no argument is provided for them |
| Keyword Arguments | Arguments can be passed by name, letting you skip over defaults selectively |
| Scope | Variables defined inside a function are local to that function and don't affect variables outside it, unless declared `global` |
| The `UnboundLocalError` trap | If a variable is assigned anywhere inside a function, Python treats it as local for the whole function — even before the assignment line runs |
| Recursion | A function calling itself to solve a smaller version of the same problem |
| Base Case | The condition that stops recursion; without it, the function calls itself forever until Python raises a `RecursionError` |
| Recursive Case | The part of the function where it calls itself with a simpler or smaller input |
| Mutable Default Argument Trap | Default arguments (like `[]`) are created once at function definition time, not on every call — using a mutable default can cause values to persist across calls unexpectedly |

## Files in This Folder

| File | Purpose |
|---|---|
| `01_functions.py` | Basics of defining and calling functions |
| `02.practice.py` – `05.practice.py` | Practice exercises on parameters, arguments, return values, and scope |
| `06_recursion.py` | Introduction to recursion, base cases, and recursive cases |
| `07_practice.py`, `08_practice.py` | Practice exercises applying recursion (factorial, digit sum, power, palindrome check) |

## Portfolio Project: Recursive Countdown/Sum Toolkit
 
A console menu-based application where every core operation is solved recursively, with no loops used for the actual logic.
 
### Features
 
- **Countdown** — recursively counts down from a given number to 0, ending with a "Liftoff!" message
- **Sum of Natural Numbers** — recursively calculates `1 + 2 + ... + n`
- **Sum of Digits** — recursively adds up the digits of a number
- **Factorial** — recursively calculates `n!`
- **Menu system** — loop-based interface letting the user pick an operation, run it, and exit cleanly
### Edge Cases Handled
 
- `sum_natural` uses a base case of `n <= 0` to safely handle zero or accidental negative input, avoiding infinite recursion
- Menu loop has a proper exit condition (`choice == "5"`) that breaks out cleanly instead of falling through to an invalid-choice message
## Learning Outcomes
 
By the end of this topic, I can:
 
- Write functions with required and default parameters
- Explain and demonstrate the difference between `return` and `print`
- Predict variable scope behavior, including the `UnboundLocalError` trap
- Write recursive functions with correct base and recursive cases
- Identify and avoid the mutable default argument trap
- Design a menu-driven console application that routes user input to the correct recursive function
- Identify and fix recursion edge cases, such as missing base cases and unhandled exit conditions
## Status
 
Complete. Concept work, quiz, and portfolio project all finished.