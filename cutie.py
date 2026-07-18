# Simple Login & Registration System


users_db = {"admin": "pass123", "user1": "python99"}
def register():
    username = input("New Username: ").strip()
    if username in users_db:
        print("Username already exists!")
    else:
        password = input("New Password: ").strip()
        users_db[username] = password
        print(f"User '{username}' registered successfully!")
def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    if users_db.get(username) == password:
        print(f"Login successful! Welcome, {username}.")
    else:
        print("Invalid credentials! Try again.")
print("--- Simple Auth System ---")
while True:
    print("\n1. Register  2. Login  3. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Exiting Auth System...")
        break
    else:
        print("Invalid choice!")
print("Thank you for using the system.")