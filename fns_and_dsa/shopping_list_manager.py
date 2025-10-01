# shopping_list_manager.py

# Array for shopping list
shopping_list = []

# Function to display menu
def display_menu():
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Exit")

# Main program loop
while True:
    display_menu()
    try:
        choice = int(input("Enter your choice (1-4): "))  # numeric choice

        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(item + " added.")
        elif choice == 2:
            print("Shopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(str(i) + ". " + item)
        elif choice == 3:
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(item + " removed.")
            else:
                print(item + " not found.")
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1-4.")
    except ValueError:
        print("Invalid input. Please enter a number.")
