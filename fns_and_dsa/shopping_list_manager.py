def display_menu():
    print("1. Add\n2. Remove\n3. View\n4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Choice (1-4): ")
        
        if choice == '1':
            shopping_list.append(input("Add: "))
        elif choice == '2':
            item = input("Remove: ")
            print(f"{item} {'removed' if item in shopping_list and shopping_list.remove(item) else 'not found'}")
        elif choice == '3':
            print('\n'.join(shopping_list) or "Empty")
        elif choice == '4':
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
