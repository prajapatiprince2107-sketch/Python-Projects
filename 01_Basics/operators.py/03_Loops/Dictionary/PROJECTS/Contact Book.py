contacts = {}

n = int(input("Enter number of contacts: "))

for i in range(n):

    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

print("\n========== CONTACTS ==========")

for name, details in contacts.items():

    print("Name:", name)
    print("Phone:", details["phone"])
    print("Email:", details["email"])
    print("-------------------------")

search = input("\nEnter name to search: ")

if search in contacts:
    print("Phone:", contacts[search]["phone"])
    print("Email:", contacts[search]["email"])
else:
    print("Contact not found!")