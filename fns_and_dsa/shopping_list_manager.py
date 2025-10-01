# Shopping List Manager

# Global shopping list
shopping_list = []

def display_menu():
    """Display the shopping list menu options."""
    print("\n--- Shopping List Menu ---")
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Exit")

def add_item():
    """Add an item to the shopping list."""
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"✅ '{item}' has been added to the shopping list.")

def view_list():
    """View all items in the shopping list."""
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("\n--- Shopping List ---")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")

def remove_item():
    """Remove an item from the shopping list."""
    view_list()
    if shopping_list:
        try:
            choice = int(input("Enter the number of the item to remove: "))
            if 1 <= choice <= len(shopping_list):
                removed = shopping_list.pop(choice - 1)
                print(f"❌ '{removed}' has been removed from the shopping list.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main program loop."""
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                add_item()
            elif choice == 2:
                view_list()
            elif choice == 3:
                remove_item()
            elif choice == 4:
                print("👋 Exiting Shopping List Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()

