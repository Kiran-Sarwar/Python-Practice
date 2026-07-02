# Author = Kiran
# Date = 2nd July, 2026
# Description = Understanding the concept of methods of dictionary in python

my_dict = {
    "Name" : "Kiran",
}

my_dict.keys() # Returns a view object that displays a list of all the keys in the dictionary
my_dict.values() # Returns a view object that displays a list of all the values in the dictionary
my_dict.items() # Returns a view object that displays a list of a tuple of all the key-value pairs in the dictionary
my_dict.get("Name") # Returns the value of the key "Name"
my_dict.update({"Age" : 25}) # Updates the dictionary with the key-value pair "Age" : 25

print(len(my_dict)) # Prints the length of the dictionary
my_dict.get("Subjects", "Not Found") # Returns the value of the key "Subjects" if it exists, otherwise returns "Not Found"
my_dict("Subjects") # Returns error because the key "Subjects" does not exist in the dictionary