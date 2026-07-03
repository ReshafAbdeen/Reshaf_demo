def todo_app():
    tasks = []
    print("Welcome to Your Personal To-Do List!")

    while True:
        print("\n1. Add Task | 2. Show Tasks | 3. Exit")
        choice = input("Option select karein (1/2/3): ").strip()

        if choice == '1':
            task = input("Kaam (Task) ka naam likhein: ")
            tasks.append(task)
            print(f"'{task}' list me add ho gaya hai!")
        elif choice == '2':
            if not tasks:
                print("Aapki list abhi khali hai!")
            else:
                print("\n--- Aapki To-Do List ---")
                for index, item in enumerate(tasks, 1):
                    print(f"{index}. {item}")
        elif choice == '3':
            print("Bye! Apna khayal rakhein.")
            break
        else:
            print("Invalid option! Sahi number chunein.")

todo_app()