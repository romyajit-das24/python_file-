contacts = {}

while True:
    print("\ncontact book app")
    print("1. create contact")
    print("2. view contact")
    print("3. update contact")
    print("4. delete contact")
    print("5. search contact")
    print("6. count contact")
    print("7. Exit")

    choice = input("Enter your choice = ")
    
    if choice == "1":
        name = input("Enter your name = ")
    if name in contacts:
        print(f"contact name {name} already exists!")
    else:
        age = input("Enter age = ")
        email = input("Enter email = ")
        mobile = input("Enter mobile number = ")
        contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile } 
        print(f"contact name {name} has been created successfully!")

    if choice == "2":
        name = input("Enter your name to view = ")

        if name in contacts:
            contacts = contacts[name]
            print(f"name : {name}, age : {age}, mobile : {mobile}")
        else:
            print("contact not found!")

    if choice == "3":
        name = input("Enter name to update contacts = ")

        if name in contacts:
            age = input("Enter updated age = ")
            email = input("Enter updated email = ")
            mobile = input("Enter updated mobile number = ")
            contacts[name] = {'age':int(age),'email':email,'mobile':mobile }
        else:
            print("contact not found!")
    
    if choice == "4":
        name = input("Enter contact name to delete = ")
        
        if name in contacts:
            del contacts[name]
            print(f"contact name {name} has been deleted successfully!")
        else:
            print("contact not found")

    if choice == "5":
        search_name = input("Enter contact name to  search = ")

        found = False
        for name,contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"found - Name{name},Age{age},Email{email}")
                found = True
            if not found:
                print("No contact  found with that  name")

    if choice == "6":
        print(f"Total  contacts in your book :{len(contacts)}")

    if choice == "7":
        print("Good bye.....close the program") 
        break
    else:
        print("Invalid input")  






 
