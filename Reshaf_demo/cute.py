import sys

def show_menu():
    print("\n--- My Task Tracker ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def main():
    tasks = []
    
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ")

        if choice == '1':
            print("\nYOUR TASKS:")
            if not tasks:
                print("Abhi koi task nahi hai!")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == '2':
            new_task = input("Naya task likhiye: ")
            tasks.append(new_task)
            print("Task add ho gaya!")

        elif choice == '3':
            if not tasks:
                print("Delete karne ke liye kuch nahi hai.")
                continue
            
            try:
                task_num = int(input("Kaunsa task number delete karna hai? "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Sirf number type karein!")

        elif choice == '4':
            print("Goodbye!")
            sys.exit()
        
        else:
            print("Galat option! Dubara try karein.")

if __name__ == "_main_":
    main()