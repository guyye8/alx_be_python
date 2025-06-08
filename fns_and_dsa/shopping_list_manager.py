def display_menu():
    print("1. Add Item\n2. Remove Item\n3. View List\n4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter choice (1-4): ")
        
        if choice == '1':
            shopping_list.append(input("Item to add: "))
        elif choice == '2':
            item = input("Item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item not found")
        elif choice == '3':
            print(*shopping_list, sep='\n') if shopping_list else print("Empty list")
        elif choice == '4':
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
