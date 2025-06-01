# daily_reminder.py
def daily_reminder():
    print("Welcome to your Daily Reminder!")
    
    while True:
        # Get user input
        task = input("\nEnter your task: ").strip()
        if not task:
            print("Task cannot be empty. Please try again.")
            continue
            
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority not in ['high', 'medium', 'low']:
            print("Invalid priority. Please enter high, medium, or low.")
            continue
            
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound not in ['yes', 'no']:
            print("Please answer with yes or no.")
            continue
            
        # Process and display reminder
        match priority:
            case 'high':
                if time_bound == 'yes':
                    print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
                else:
                    print(f"\nReminder: '{task}' is a high priority task. Please address it soon.")
                    
            case 'medium':
                if time_bound == 'yes':
                    print(f"\nReminder: '{task}' is a medium priority task that should be completed today.")
                else:
                    print(f"\nNote: '{task}' is a medium priority task. Schedule it for this week.")
                    
            case 'low':
                if time_bound == 'yes':
                    print(f"\nReminder: '{task}' is a low priority task with a time constraint. Try to complete it today if possible.")
                else:
                    print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
        
        # Ask if user wants to add another task (but still only reminds about one at a time)
        another = input("\nWould you like to set another reminder? (yes/no): ").strip().lower()
        if another != 'yes':
            print("\nHave a productive day!")
            break

if __name__ == "__main__":
    daily_reminder()
