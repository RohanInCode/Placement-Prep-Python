# =========================================================
# 🔹 STUDENT RECORD SYSTEM
# =========================================================

Student = {}

while True:
    print("\n---- Student Record System -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice here: ")

    # Add student
    if choice == "1":
        name = input("Enter Student name: ")
        roll = input("Enter roll no: ")
        course = input("Enter course: ")

        Student[roll] = {
            "name": name,
            "course": course
        }

        print("Student added successfully")

    # View students
    elif choice == "2":
        if Student:
            print("\nAll Students:")
            for roll, info in Student.items():
                print("Roll:", roll)
                print("Name:", info["name"])
                print("Course:", info["course"])
                print()
        else:
            print("No student record found")

    # Search
    elif choice == "3":
        roll = input("Enter roll to search: ")
        if roll in Student:
            print("Name:", Student[roll]["name"])
            print("Course:", Student[roll]["course"])
        else:
            print("Student not found")

    # Delete
    elif choice == "4":
        roll = input("Enter roll to delete: ")
        removed = Student.pop(roll, None)

        if removed:
            print("Student deleted successfully")
        else:
            print("Student not found")

    # Exit
    elif choice == "5":
        print("Thank you for using student record system")
        break

    else:
        print("Invalid choice")





# =========================================================
# 🔹 CONTACT BOOK PROJECT
# =========================================================

contact = {}

while True:
    print("\n---- Contact Book -----")
    print("1. Add contact")
    print("2. View contact")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Enter your choice here: ")

    # Add contact
    if choice == "1":
        name = input("Enter the name: ")
        phone = input("Enter the number: ")
        contact[name] = phone
        print("Contact added successfully")

    # View contacts
    elif choice == "2":
        if contact:
            print("\nSaved contacts:")
            for name, phone in contact.items():
                print(name, ":", phone)
        else:
            print("No contacts found")

    # Search
    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contact:
            print("Phone number:", contact[name])
        else:
            print("Contact not found")

    # Delete
    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contact:
            del contact[name]
            print("Contact deleted")
        else:
            print("Contact not found")

    # Exit
    elif choice == "5":
        print("Thank you for using contact book")
        break

    else:
        print("Invalid choice")
