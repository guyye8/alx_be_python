def display_menu():
    print("Shopping List Manager\n1. Add Item\n2. Remove Item\n3. View List\n4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter choice: ")
        
        if choice == '1':
            shopping_list.append(input("Item to add: "))
        elif choice == '2':
            item = input("Item to remove: ")
            print(f"{item} {'removed' if item in shopping_list and shopping_list.remove(item) else 'not found'}")
        elif choice == '3':
            print("Current List:" if shopping_list else "Empty list")
            print("\n".join(f"{i+1}. {item}" for i, item in enumerate(shopping_list)))
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
