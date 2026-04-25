from connect import get_connection
def add_contact(name, phone_number):
    if not phone_number.isdigit():
        print("Invalid input format, cancelling operation ...")
        return

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone_number)
    )
    conn.commit()
    cur.close()
    conn.close()
    print(f"Phone number of {name} is inserted into the phonebook")
def find_contact(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT phone FROM phonebook WHERE name ILIKE %s",
        ('%' + name + '%',)
    )
    result = cur.fetchall()
    cur.close()
    conn.close()

    if result:
        for row in result:
            print(row[0])
    else:
        print(f"Couldn't find phone number of {name}")

def delete_contact(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM phonebook WHERE name = %s",
        (name,)
    )
    if cur.rowcount > 0:
        print(f"{name} is deleted from the phonebook")
    else:
        print(f"Couldn't find {name} in the phonebook")
    conn.commit()
    cur.close()
    conn.close()
def main():
    print("Welcome to the phonebook application")
    while True:
        print("\n1. Find phone number")
        print("2. Insert a phone number")
        print("3. Delete a person from the phonebook")
        print("4. Terminate")

        choice = input("Select operation (1/2/3/4): ")

        if choice == '1':
            name = input("Find the phone number of: ")
            find_contact(name)
        elif choice == '2':
            name = input("Insert name of the person: ")
            phone_number = input("Insert phone number: ")
            add_contact(name, phone_number)
        elif choice == '3':
            name = input("Whom to delete: ")
            delete_contact(name)
        elif choice == '4':
            print("Exiting Phonebook")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()