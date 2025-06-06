#This is a function that simply prints the menu. Every time you call display_menu(), the user sees the menu options.
# Function to display menu options to the user
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main logic can go below

# Main function where the logic happens
def main():
    shopping_list = []  # This list will store all the shopping items

    while True:  # Keep the program running until the user chooses to exit
        display_menu()  # Show the menu
        choice = input("Enter your choice (1-4): ").strip()  # Get user's choice

        if choice == '1':
            # Add an item to the shopping list
            item = input("Enter the item to add: ").strip()
            if item:  # Make sure it's not empty
                shopping_list.append(item)
                print(f"✅ '{item}' has been added to your shopping list.")
            else:
                print("⚠️ Item name cannot be empty.")

        elif choice == '2':
            # Remove an item from the shopping list
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"🗑️ '{item}' has been removed from your shopping list.")
            else:
                print(f"⚠️ '{item}' is not in your shopping list.")

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\n🛒 Your Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("🛍️ Your shopping list is currently empty.")

        elif choice == '4':
            # Exit the program
            print("👋 Goodbye! Thanks for using the Shopping List Manager.")
            break

        else:
            # Handle invalid menu choices
            print("❌ Invalid choice. Please enter a number between 1 and 4.")

# Only run the main function if this script is run directly
if __name__ == "__main__":
    main()
