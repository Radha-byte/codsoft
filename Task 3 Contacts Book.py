contacts = []

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Added!")

def view_contacts():
    for c in contacts:
        print(f"{c['name']} - {c['phone']}")

def search_contact():
    term = input("Search: ")
    for c in contacts:
        if term in c['name'] or term in c['phone']:
            print(f"{c['name']} - {c['phone']}")

def update_contact():
    name = input("Update contact name: ")
    for c in contacts:
        if c['name'] == name:
            c['phone'] = input("New phone: ")
            c['email'] = input("New email: ")
            c['address'] = input("New address: ")
            print("Updated!")

def delete_contact():
    name = input("Delete contact name: ")
    global contacts
    contacts = [c for c in contacts if c['name'] != name]
    print("Deleted!")

while True:
    print("\n1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Exit")
    option = input("Choose: ")
    if option == '1':
        add_contact()
    elif option == '2':
        view_contacts()
    elif option == '3':
        search_contact()
    elif option == '4':
        update_contact()
    elif option == '5':
        delete_contact()
    elif option == '6':
        break
