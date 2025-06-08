# shopping_list_manager.py

def display_menu():
    print("\n🛒 Shopping List Manager 🛒")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        try:
            choice = int(input("Choose an option (1-4): ").strip())
            if choice == 1:
                item = input("Add item: ").strip()
                if item:
                    shopping_list.append(item)
                    print(f"✅ '{item}' added.")
                else:
                    print("⚠️ Item name cannot be empty.")
            elif choice == 2:
                item = input("Remove item: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"❌ '{item}' removed.")
                else:
                    print(f"❓ '{item}' not found.")
            elif choice == 3:
                if shopping_list:
                    print("\n📝 Your Shopping List:")
                    for i, item in enumerate(shopping_list, 1):
                        print(f"{i}. {item}")
                else:
                    print("🛒 Your shopping list is empty.")
            elif choice == 4:
                print("👋 Goodbye! Happy shopping!")
                break
            else:
                print("⚠️ Invalid choice. Please enter a number from 1 to 4.")
        except ValueError:
            print("❗ Please enter a valid number.")

if __name__ == "__main__":
    main()
