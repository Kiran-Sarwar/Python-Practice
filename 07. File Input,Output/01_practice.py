# Author = Kiran
# Date = 20th July, 2026
"""
Create a new file "practice.txt" using Python. Add the following data in it:
Hi everyone
We are learning File I/O
using Java
I like programming in Java.

WAF that replace all occurrences of "java" with "python" in above file. 

Search the if the word "learning" exists in the file.
"""

with open("practice.txt","w") as f:
    f.write("Hi everyone\n")
    f.write("We are learning File I/O\n")
    f.write("using Java\n")
    f.write("I like programming in Java.\n")

def replace_words():
    with open("practice.txt","r") as f:
        data = f.read()
    new_data = data.replace("Java", "Python")
    print(new_data)
    with open("practice.txt","w") as f:
        f.write(new_data)

def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")

replace_words()
check_for_word()