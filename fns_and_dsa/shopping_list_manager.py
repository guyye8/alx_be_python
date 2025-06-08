def display_menu():
    print("Shopping List Manager\n1. Add Item\n2. Remove Item\n3. View List\n4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            shopping_list.append(input("Enter item to add: "))
        elif choice == '2':
            item = input("Enter item to remove: ")
            print("Item removed" if item in shopping_list and shopping_list.remove(item) else "Item not found")
        elif choice == '3':
            print("\n".join(shopping_list) if shopping_list else "List is empty")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()
