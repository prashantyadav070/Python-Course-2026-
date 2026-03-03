# 📞 Smart Contact Manager  

import json

contacts = []

# 🔹 Load contacts from file (if exists)
try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except:
    contacts = []

print("📞🔥 Welcome to Smart Contact Manager 🔥📞")

# 🔹 Save contacts to file
def saveContacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)
    print("✅ Contacts saved successfully!")

# 🔹 Add Contact
def addContact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    saveContacts()
    print("🎉 Contact Added Successfully!")

# 🔹 View Contacts
def viewContacts():
    if len(contacts) == 0:
        print("❌ No Contacts Found!")
    else:
        print("\n📋 Your Contacts:")
        for index, contact in enumerate(contacts):
            print(f"{index+1}. {contact['name']} | {contact['phone']} | {contact['email']}")

# 🔹 Search Contact
def searchContact():
    searchName = input("Enter name to search: ").lower()
    found = False

    for contact in contacts:
        if searchName in contact["name"].lower():
            print(f"🔍 Found: {contact['name']} | {contact['phone']} | {contact['email']}")
            found = True

    if not found:
        print("❌ Contact Not Found!")

# 🔹 Delete Contact
def deleteContact():
    viewContacts()
    try:
        choice = int(input("Enter contact number to delete: "))
        removed = contacts.pop(choice - 1)
        saveContacts()
        print(f"🗑 Deleted: {removed['name']}")
    except:
        print("❌ Invalid Choice!")

# 🔹 Main Menu Loop
while True:
    print("\n📌 MENU")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addContact()
    elif choice == "2":
        viewContacts()
    elif choice == "3":
        searchContact()
    elif choice == "4":
        deleteContact()
    elif choice == "5":
        print("👋 Thank you for using Contact Manager!")  
        break
    else:
        print("❌ Invalid Choice!")
