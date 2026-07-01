String and Conditional Statements

A comprehensive collection of Python practice files covering string manipulation and conditional logic — essential building blocks for any Python developer.


Topics Covered

Part 1: String Operations

Learn how to work with text data in Python, including concatenation, indexing, slicing, and built-in string methods.

Part 2: Conditional Statements

Master decision-making logic using if, elif, and else statements to control program flow based on conditions.


Practice Files

String Manipulation

FileTopicDescription01_Concatenation.pyString ConcatenationJoining strings using + operator and .join() method02_Indexing.pyString IndexingAccessing individual characters using index positions03_Slicing.pyString SlicingExtracting substrings using slice notation [start:end:step]04_String_Function.pyBuilt-in MethodsUsing .upper(), .lower(), .strip(), .split(), .replace(), etc.05_Str_Practice1.pyPractice Exercise 1Combined string operations challenge06_Str_Practice2.pyPractice Exercise 2Advanced string manipulation problems

Conditional Statements

FileTopicDescription07_Conditions.pyIf-Elif-Else LogicDecision-making with conditional statements and logical operators08_Con_Practice1.pyPractice Exercise 1Basic conditional logic challenges09_Cond_Practice2.pyPractice Exercise 2Nested conditions and multiple branches10_Cond_Practice3.pyPractice Exercise 3Complex problem-solving with conditions


Learning Outcomes

After completing this topic, you will be able to:

Concatenate and manipulate strings using various methods

Extract characters and substrings using indexing and slicing

Apply built-in string functions for text processing

Write conditional logic using if, elif, and else

Combine multiple conditions using logical operators (and, or, not)

Debug and test conditional code effectively


Key Concepts

Strings

python# Concatenation
name = "Kiran" + " Sarwar"

# Indexing (0-based)
first_char = name[0]  # 'K'

# Slicing
substring = name[0:5]  # 'Kiran'

# String Methods
uppercase = name.upper()  # 'KIRAN SARWAR'

Conditionals

python# Basic if-else
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Multiple conditions
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'


How to Use This Folder


Read the Apna College lessons on Strings and Conditional Statements
Run each practice file in order to understand the concepts
Modify and experiment with the code — change values, test edge cases
Complete the challenge files (*_Practice*.py) to solidify understanding
Test your knowledge with the quiz below



Mini-Quiz

Test your understanding before moving to the next topic:

Question 1: What will this code output?

pythontext = "Python"
print(text[1:4])

Question 2: What is the correct syntax for an if-else statement?

pythonif condition:
    # code
else:
    # code

Why is the colon (:) and indentation important?

Question 3: What will this output?

pythonx = 10
if x > 5 and x < 15:
    print("Between 5 and 15")
else:
    print("Outside range")

Question 4: Complete the code:

pythonname = "Alice"
if ____:
    print("Name starts with A")

(Hint: Use string indexing)


Resources


Apna College (YouTube): String & Conditional Statements Playlist
Python Docs: String Methods
Python Docs: If Statements



Progress Tracker


 String Concatenation
 Indexing & Slicing
 String Functions
 String Practice Exercises
 Conditional Statements
 Condition Practice Exercises



Next Topic

Once you've completed all files and the quiz, you're ready for:

Phase 1, Topic 3: Loops (for, while)


Author Notes


Always pay attention to colons (:) and indentation in Python — they're crucial!
Test edge cases when working with conditionals (boundary values, negative numbers, etc.)
Use descriptive variable names to make your code readable



Last Updated: June 29, 2026

Repository: Kiran-Sarwar/Python-Practice
