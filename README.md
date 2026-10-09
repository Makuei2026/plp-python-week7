# PLP Python Week 7 Assignment: Working with Lists

## File Descriptions
- `list_warmup.py`: Demonstrates basic list operations including index access, appending, removing, and length checking.
- `shopping_list.py`: An interactive console application that uses a loop and conditional checks to safely add, remove, and view items in a shopping list.
- `list_report.py`: Processes a list of items using loops and conditionals to render numbered output, count items over 4 characters long, and manually track the longest string in the list.

## Reflection
It is safer to check if an item is present in a list using the `in` operator before calling `.remove()` because calling `.remove()` on an item that does not exist raises a `ValueError` and crashes the program. Verifying existence beforehand prevents runtime exceptions and keeps interactive applications running smoothly.
