shopping_list = []


def display_menu():
    print(f"Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")


while True:
    display_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        item = input("Enter the item to add:")
        shopping_list.append(item)
        print(f"{item} has been added to your list.")

    elif choice == "2":
        item = input("What item do you want to remove? ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from your list.")
        else:
            print(f"{item} was not found in your list.")

    elif choice == "3":
        print("Your Shopping List:")
        if shopping_list:
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        else:
            print("Your list is empty.")

    elif choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
