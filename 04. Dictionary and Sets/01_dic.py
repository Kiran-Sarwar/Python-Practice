# Author = Kiran
# Date = 2nd July, 2026
# Description = Understanding the concept of dictionary in python

info = {
    "Key" : "Value",
    "Name" : "Kiran",
    "Age" : 25,
    "isAdult" : True,
    "topics" : ("Python", "Java", "C++"), # Can also make a tuple as a value in dictionary
    "Subjects" : ["Maths", "Science", "English"], # Can also make a list as a value in dictionary
}
# key can be int and float as well, but it can not be a tuple because it is immutable, but it can be a list because it is mutable

print(info) # Prints the whole dictionary
print(type(info)) # Prints the type of the dictionary
# dictionary are unordered, mutable and indexed. It is a collection of key-value pairs. Each key is unique and can be used to access the corresponding value. key cannot be duplicated, but values can be duplicated. Dictionary is defined by using curly braces {} and key-value pairs are separated by a colon (:). Each key-value pair is separated by a comma (,).

print(info["Name"]) # Prints the value of the key "Name"
print(info["Age"]) # Prints the value of the key "Age"
print(info["isAdult"]) # Prints the value of the key "isAdult"
print(info["topics"]) # Prints the value of the key "topics"
print(info["Subjects"]) # Prints the value of the key "Subjects"

info["Age"] = 26 # Updates the value of the key "Age"
print(info["Age"]) # Prints the updated value of the key "Age"

null_dict = {} # Creates an empty dictionary
null_dict["Name"] = "Kiran" # Adds a key-value pair to the empty dictionary
print(null_dict) # Prints the dictionary with the added key-value pair