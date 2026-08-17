import json
import time

# Load saved subjects
try:
    with open("subjects.json", "r") as file:
        subjects = json.load(file)
except FileNotFoundError:
    subjects = []

print("===== PYTHON STUDY ASSISTANT =====")

while True:
    print("\nWhat would you like to do?")
    print("1. Add a subject")
    print("2. Start a study session")
    print("3. View subjects")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        subject = input("Enter the subject name: ")

        subjects.append(subject)

        with open("subjects.json", "w") as file:
            json.dump(subjects, file)

        print(f"{subject} has been added!")

    elif choice == "2":
        if len(subjects) == 0:
            print("Please add a subject first.")
            continue

        print("\nChoose a subject:")

        for number, subject in enumerate(subjects, start=1):
            print(f"{number}. {subject}")

        try:
            subject_number = int(input("Enter the subject number: "))
            subject = subjects[subject_number - 1]

            minutes = int(input("How many minutes do you want to study? "))

            print(f"\nStudying {subject} for {minutes} minutes... 📚")
            print("Your timer has started! ⏱️")

            for remaining in range(minutes * 60, 0, -1):
                mins = remaining // 60
                secs = remaining % 60

                print(f"\rTime remaining: {mins:02d}:{secs:02d}", end="")
                time.sleep(1)

            print("\n🎉 Study session complete!")

        except (ValueError, IndexError):
            print("Invalid input. Please try again.")

    elif choice == "3":
        print("\nYour subjects:")

        if len(subjects) == 0:
            print("No subjects added yet.")
        else:
            for number, subject in enumerate(subjects, start=1):
                print(f"{number}. {subject}")

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please try again.")
