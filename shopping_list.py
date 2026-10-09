Python
shopping_list = []

while True:
    action = input("\nChoose an action (add / remove / show / done): ").strip().lower()

    if action == "add":
        item = input("Enter the item to add: ").strip()
        shopping_list.append(item)
        print(f"'{item}' added to your shopping list.")

    elif action == "remove":
        item = input("Enter the item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from your shopping list.")
        else:
            print("That item is not on your list.")

    elif action == "show":
        if shopping_list:
            print("\nYour Shopping List:")
            for item in shopping_list:
                print(item)
        else:
            print("Your shopping list is currently empty.")

    elif action == "done":
        print("Goodbye! Happy shopping!")
        break

    else:
        print("Invalid choice. Please choo
