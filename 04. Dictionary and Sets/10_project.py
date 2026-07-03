# Author = Kiran
# Date = 3rd July, 2026
"""
Project: Contact Book (console-based)
Build a simple contact management system using a dictionary where:

Keys = contact names
Values = dict of {"phone": ..., "email": ...}

Minimum features:

Add a new contact
View a contact's details (use .get() for safe lookup — you already know this!)
Delete a contact
Show all contacts
Bonus: use a set somewhere logically (e.g., tracking unique cities contacts live in)
"""

# Contact Book

# Dictionary to store contacts
contacts = {}

# Set to store unique cities
cities = set()

# -----------------------------
# 1. Add Contacts
# -----------------------------

contacts["Ali"] = {
    "phone": "03001234567",
    "email": "ali@gmail.com",
    "city": "Lahore"
}
cities.add("Lahore")

contacts["Sara"] = {
    "phone": "03111234567",
    "email": "sara@gmail.com",
    "city": "Karachi"
}
cities.add("Karachi")

print("Contacts added successfully!\n")

# -----------------------------
# 2. View Contact
# -----------------------------

name = input("Enter contact name to view: ")

contact = contacts.get(name)

if contact:
    print("\nContact Found")
    print("Phone:", contact["phone"])
    print("Email:", contact["email"])
    print("City:", contact["city"])
else:
    print("\nContact not found!")

# -----------------------------
# 3. Show All Contacts
# -----------------------------

print("\nAll Contacts:")
print(contacts)

# -----------------------------
# 4. Delete Contact
# -----------------------------

name = input("\nEnter contact name to delete: ")

if name in contacts:
    del contacts[name]
    print("Contact deleted successfully!")
else:
    print("Contact not found!")

# -----------------------------
# 5. Show Remaining Contacts
# -----------------------------

print("\nRemaining Contacts:")
print(contacts)

# -----------------------------
# 6. Show Unique Cities
# -----------------------------

print("\nUnique Cities:")
print(cities)