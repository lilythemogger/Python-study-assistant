print("===== PYTHON STUDY ASSISTANT =====")

while True:
    print("\nWhat would you like to do?")
    print("1. Add a subject")
    print("2. Start a study session")
    print("3. View progress")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You chose: Add a subject")

    elif choice == "2":
        print("You chose: Start a study session")

    elif choice == "3":
        print("You chose: View progress")

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please try again.")
