import sqlite3


class ContactBook:

    def __init__(self, db_name="contacts.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS contacts 
                              (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT)"""
        )
        self.conn.commit()

    def add_contact(self, name, phone, email):
        self.cursor.execute(
            "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
            (name, phone, email),
        )
        self.conn.commit()
        print(f"Added: {name}")

    def search_contact(self, name):
        self.cursor.execute(
            "SELECT * FROM contacts WHERE name LIKE ?", (f"%{name}%",)
        )
        return self.cursor.fetchall()

    def display_all(self):
        self.cursor.execute("SELECT * FROM contacts")
        for row in self.cursor.fetchall():
            print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Email: {row[3]}")

    def close(self):
        self.conn.close()


book = ContactBook()
book.add_contact("Alice Smith", "555-0199", "alice@example.com")
book.add_contact("Bob Jones", "555-0142", "bob@example.com")
print("\n--- All Contacts ---")
book.display_all()
print("\n--- Search Result ---")
print(book.search_contact("Alice"))
book.close()