# Contact Book (Dictionary & Set Based)

A simple console-based contact management system built in Python to practice working with dictionaries and sets.

## Description

This project lets you store, view, and delete contacts. Each contact is stored as a nested dictionary containing their phone number, email, and city. A separate set is used to track all unique cities across contacts, demonstrating how sets automatically handle duplicate values.

## Features

- Add new contacts (name, phone, email, city)
- View a specific contact's details safely (no crash if contact doesn't exist)
- Delete a contact
- Display all contacts
- Track and display all unique cities using a set

## Concepts Used

- Dictionaries — storing structured data as key-value pairs
- Nested dictionaries — dict of dicts (contacts["Ali"] = {...})
- .get() method — safe key lookup without raising a KeyError
- Sets — storing unique values (cities.add(...))
- del keyword — removing a dictionary key
- in keyword — checking key existence before deletion
- input() — basic user interaction

## Learning Outcomes

- Understood the difference between = (assignment) vs : (key-value separator) in dict syntax — made this mistake multiple times before it clicked.
- Learned that dict values can themselves be dictionaries, which is useful for structured records like contacts.
- Learned that sets can't contain mutable items like lists, since their elements must be hashable/immutable.
- Practiced defensive coding — checking if name in contacts before deleting, to avoid errors.
- Used .get() to avoid KeyError when looking up a contact that might not exist.

## How to Run

python contact_book.py

You'll be prompted to view and delete a contact by name (contacts are currently hardcoded — dynamic add/delete via loop coming once the Loops topic is covered).

## Future Improvements

- Add a menu-driven loop (while True) for continuous add/view/delete without re-running the script
- Prevent duplicate contact names from overwriting existing ones
- Pretty-print contact details instead of raw dict output

---
Topic: Dictionaries & Sets — Phase 1 (Foundations)
Status: Complete