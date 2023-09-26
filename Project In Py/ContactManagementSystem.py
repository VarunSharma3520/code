
contacts = []
def create(contacts):
    contactName = input("Enter your name")
    contactNumber = input("Enter your number")
    contacts.append([contactName,contactNumber])
    print("you number added successfully...\n")
    return contacts

def read(contacts):
    search = False
    while True:
        print("""Press 1 for seacrch by name
Press 2 for search by number
Press 0 for main menu""")
        searchChoice = int(input("Enter your choice..."))
        if searchChoice == 1:
            searchTerm = input("Enter your search term...")
            for i in range(len(contacts)):
                if searchTerm in contacts[i][0]:
                    print(contacts[i])
                    search = True
        elif searchChoice == 2:
            searchTerm = input("Enter your search term...")
            for i in range(len(contacts)):
                if searchTerm in contacts[i][1]:
                    print(contacts[i])
                    search = True
        elif searchChoice == 0:
            break
        else:
            print("You entered wrong choice")
            print("You May Try Again")
    if search == False:
            print("No contacts found....")

def delete(contacts):
    listy = []
    delete = False
    while True:
        print("""Press 1 for delete by name
Press 2 for delete by number
Press 0 for main menu""")
        deleteChoice = eval(input("Enter your choice..."))
        if deleteChoice == 1:
            deleteTerm = input("Enter your search term...")
            for i in range(len(contacts)):
                if deleteTerm in contacts[i][0]:
                    delete = True
                    continue
                else:
                    listy.append(contacts[i])
        elif deleteChoice == 2:
            deleteTerm = input("Enter your search term...")
            for i in range(len(contacts)):
                if deleteTerm in contacts[i][1]:
                    delete = True
                    continue
                else:
                    listy.append(contacts[i])
        elif deleteChoice == 0:
            break
        else:
            print("You entered wrong choice")
            print("You May Try Again")
    if delete == False:
        print("No contacts found....")
    else:
        return listy

def update(contacts):
    delete(contacts)
    create(contacts)
def showAll(contacts):
    print(["Name","Number"])
    for i in contacts:
        print(i)
while True:
    print("""
    Press 1 for add new contact
    Press 2 for find contact
    Press 3 for Update contact
    Press 4 for delete contact
    Press 5 for show all contact
    Press 0 to terminate program
    """)
    user_choice = eval(input("Enter your choice here..."))
    if user_choice == 0:
        print("\n\nProgram Terminated Successfully..")
        print("Thank You!")
        break
    elif user_choice == 1:
        contacts = create(contacts)
    elif user_choice == 2:
        contacts = read(contacts)
    elif user_choice == 3:
        contacts = update(contacts)
    elif user_choice == 4:
        contacts = delete(contacts)
    elif user_choice == 5:
        contacts = showAll(contacts)
    else:
        print("you entered wrong input")
        print("Try Again...")