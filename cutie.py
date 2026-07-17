# Simple Contact Bookcontacts = {}
def display_menu():
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")
while True:
    display_menu()
    choice = input("Enter choice (1-4): ")
    if choice == '1':
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        contacts[name] = phone
        print(f"Contact '{name}' added!")
    elif choice == '2':
        print("\nSaved Contacts:")
        if not contacts:
            print("No contacts found.")
        for n, p in contacts.items():
            print(f"Name: {n} | Phone: {p}")
    elif choice == '3':
        name = input("Name to delete: ").strip()
        if contacts.pop(name, None):
            print(f"Contact '{name}' deleted!")
        else:
            print("Contact not found.")
    elif choice == '4':
        print("Exiting Contact Book...")
        break