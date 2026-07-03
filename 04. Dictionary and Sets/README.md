# 04. Dictionaries and Sets

This folder contains all my practice work and the portfolio project for the Dictionaries and Sets topic, part of Phase 1 (Foundations) of my AI Engineer roadmap.

## Folder Contents

| File | Description |
|---|---|
| 01_dic.py | Dictionary basics — creating dictionaries, adding keys, accessing values |
| 02_nested_dic.py | Nested dictionaries — dictionaries containing other dictionaries as values |
| 03_dic_methods.py | Built-in dictionary methods (.get(), .keys(), .values(), .items(), .update(), del, etc.) |
| 04_sets.py | Set basics — creating sets, adding/removing elements, uniqueness behavior |
| 05_sets_methods.py | Set methods and operations (union, intersection, difference, symmetric_difference) |
| 06_practice1.py | Practice exercise 1 |
| 07_practice.py | Practice exercise 2 |
| 08_practice.py | Practice exercise 3 |
| 09_practice.py | Practice exercise 4 |
| 10_project.py | Portfolio project — Contact Book (console-based, using nested dictionaries and sets) |

## Topic Overview

This section of my learning covered two core Python data structures:

**Dictionaries** — key-value pair storage, used for representing structured, labeled data. Covered creation, access, safe lookup with .get(), nested dictionaries, and common built-in methods.

**Sets** — unordered collections of unique, immutable elements. Covered creation, uniqueness behavior, and set operations like union, intersection, and difference.

## Portfolio Project: Contact Book

The main project in this folder (10_project.py) is a console-based contact management system.

### Description

Stores contacts using a dictionary where each contact name maps to a nested dictionary of their phone, email, and city. A set tracks all unique cities across contacts.

### Features

- Add new contacts (name, phone, email, city)
- View a specific contact's details safely (no crash if contact doesn't exist)
- Delete a contact
- Display all contacts
- Track and display all unique cities using a set

### Concepts Used

- Dictionaries — storing structured data as key-value pairs
- Nested dictionaries — dict of dicts (contacts["Ali"] = {...})
- .get() method — safe key lookup without raising a KeyError
- Sets — storing unique values (cities.add(...))
- del keyword — removing a dictionary key
- in keyword — checking key existence before deletion
- input() — basic user interaction

## Learning Outcomes

- Understood the difference between = (assignment) and : (key-value separator) in dictionary syntax — this tripped me up multiple times before it clicked.
- Learned that dictionary values can themselves be dictionaries, useful for structured records like contacts.
- Learned that sets cannot contain mutable items like lists, since set elements must be hashable/immutable.
- Practiced defensive coding — checking if a key exists before deleting it, to avoid runtime errors.
- Used .get() to avoid KeyError when looking up something that might not exist.

## How to Run the Project

python 10_project.py

Contacts are currently hardcoded in the script. Dynamic add/delete through user input in a loop will be added once the Loops topic is covered.

## Future Improvements

- Add a menu-driven loop (while True) for continuous add/view/delete without re-running the script
- Prevent duplicate contact names from overwriting existing ones
- Pretty-print contact details instead of raw dictionary output

---
Topic: Dictionaries and Sets — Phase 1 (Foundations)
Status: Complete
