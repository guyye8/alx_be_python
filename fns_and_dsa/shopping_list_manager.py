# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item\n2. Remove Item\n3. View List\n4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                item = input("Item to add: ").strip()
                shopping_list.append(item)
                print(f"'{item}' added.")
            elif choice == 2:
                item = input("Item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' removed.")
                else:
                    print(f"'{item}' not found.")
            elif choice == 3:
                if shopping_list:
                    for i, item in enumerate(shopping_list, 1):
                        print(f"{i}. {item}")
                else:
                    print("List is empty.")
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")

if __name__ == "__main__":
    main()
