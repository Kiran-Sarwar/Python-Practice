# Author = Kiran
# Date = 2nd July, 2026
# Description = Understanding the concept of nested dictionary in python

student = {
    "Name" : "Kiran",
    "Age" : 25,
    "Sujects" : {
        "Maths" : 90,
        "Science" : 85,
        "English" : 95
    },
}

print(student) # Prints the whole dictionary
print(type(student)) # Prints the type of the dictionary
print(student["Sujects"]) # Prints the value of the key "Sujects"
print(student["Sujects"]["Maths"]) # Prints the value of the key "Maths" in the nested dictionary