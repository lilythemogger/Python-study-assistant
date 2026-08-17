import json
import time

# Load saved data
try:
    with open("study_data.json", "r") as file:
        study_data = json.load(file)
except FileNotFoundError:
    study_data = {
        "subjects": [],
        "study_time": {}
    }

subjects = study_data["subjects"]
study_time = study_data["study_time"]

print("===== PYTHON STUDY ASSISTANT =====")

while True:
    print("\nWhat would you like to do?")
    print("1. Add a subject")
    print("2. Start a study session")
    print("3. View subjects")
    print("4. View study progress")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add subject
    if choice == "1":
        subject = input("Enter the subject name: ")

        if subject not in subjects:
            subjects.append(subject)
            study_time[subject] = 0

            print(f"{subject} has been added!")
        else:
            print("That subject already exists.")

    # Study session
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

            if minutes <= 0:
                print("Please enter a positive number.")
                continue

            print(f"\nStudying {subject} for {minutes} minutes... 📚")
            print("Your timer has started! ⏱️")

            for remaining in range(minutes * 60, 0, -1):
                mins = remaining // 60
                secs = remaining % 60

                print(
                    f"\rTime remaining: {mins:02d}:{secs:02d}",
                    end=""
                )

                time.sleep(1)

            print("\n🎉 Study session complete!")

            study_time[subject] += minutes

        except (ValueError, IndexError):
            print("Invalid input. Please try again.")

    # View subjects
    elif choice == "3":
        print("\nYour subjects:")

        if len(subjects) == 0:
            print("No subjects added yet.")
        else:
            for number, subject in enumerate(subjects, start=1):
                print(f"{number}. {subject}")

    # View progress
    elif choice == "4":
        print("\n===== STUDY PROGRESS =====")

        if len(subjects) == 0:
            print("No study data yet.")
        else:
            total = 0

            for subject in subjects:
                minutes = study_time.get(subject, 0)
                print(f"{subject}: {minutes} minutes")
                total += minutes

            print(f"\nTotal study time: {total} minutes")

    # Exit
    elif choice == "5":
        # Save data before exiting
        with open("study_data.json", "w") as file:
            json.dump(study_data, file, indent=4)

        print("Your progress has been saved! 💾")
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please try again.")
