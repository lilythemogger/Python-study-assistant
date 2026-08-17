import json

PLANNER_FILE = "planner.json"


def load_planner():
    try:
        with open(PLANNER_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_planner(planner):
    with open(PLANNER_FILE, "w") as file:
        json.dump(planner, file, indent=4)


def add_session(planner):
    day = input("Enter the day (e.g. Monday): ").capitalize()
    subject = input("Enter the subject: ")
    start_time = input("Enter start time (e.g. 09:00): ")
    end_time = input("Enter end time (e.g. 10:00): ")

    if day not in planner:
        planner[day] = []

    session = {
        "subject": subject,
        "start": start_time,
        "end": end_time,
        "completed": False
    }

    planner[day].append(session)
    save_planner(planner)

    print(f"\n✅ {subject} has been added to your {day} plan!")


def view_day(planner):
    day = input("Enter the day you want to view: ").capitalize()

    if day not in planner or len(planner[day]) == 0:
        print(f"\nNo study sessions planned for {day}.")
        return

    print(f"\n===== {day.upper()} PLAN =====")

    for number, session in enumerate(planner[day], start=1):
        status = "✅ Done" if session["completed"] else "⏳ Not completed"

        print(
            f"{number}. "
            f"{session['start']} - {session['end']} | "
            f"{session['subject']} | {status}"
        )


def view_week(planner):
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    print("\n===== WEEKLY STUDY PLAN =====")

    for day in days:
        print(f"\n📅 {day}")

        if day not in planner or len(planner[day]) == 0:
            print("   No sessions planned.")
            continue

        for session in planner[day]:
            status = "✅" if session["completed"] else "⏳"

            print(
                f"   {status} "
                f"{session['start']} - {session['end']} | "
                f"{session['subject']}"
            )
