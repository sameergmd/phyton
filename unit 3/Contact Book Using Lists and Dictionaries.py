contacts = {}

n = int(input("Enter number of contacts: "))

for i in range(n):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone

print("\nContact Book:")
for name, phone in contacts.items():
    print(name, ":", phone)

search = input("\nEnter name to search: ")

if search in contacts:
    print("Phone number:", contacts[search])
else:
    print("Contact not found")
