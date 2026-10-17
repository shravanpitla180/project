from datetime import date
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = "habits.txt"


def load_habits():
    habits = []

    if not os.path.exists(FILE_NAME):
        return habits

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if "|" in line:
                name, completed_date = line.split("|", 1)
                habits.append({
                    "name": name,
                    "completed_date": completed_date
                })

    return habits


def save_habits(habits):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for habit in habits:
            file.write(f"{habit['name']}|{habit['completed_date']}\n")


def add_habit(habits):
    name = input("Enter habit name: ").strip()

    if not name or "|" in name:
        print("Enter a valid habit name.")
        return

    if any(habit["name"].lower() == name.lower() for habit in habits):
        print("This habit already exists.")
        return

    habits.append({
        "name": name,
        "completed_date": ""
    })

    save_habits(habits)
    print("Habit added successfully!")


def view_habits(habits):
    if not habits:
        print("No habits added yet.")
        return

    today = date.today().isoformat()
    print("\n--- YOUR HABITS ---")

    for i, habit in enumerate(habits, start=1):
        status = (
            "Completed"
            if habit["completed_date"] == today
            else "Pending"
        )
        print(f"{i}. {habit['name']} - {status}")


def complete_habit(habits):
    if not habits:
        print("Add a habit first.")
        return

    view_habits(habits)

    try:
        number = int(input("Enter habit number to complete: "))

        if number < 1 or number > len(habits):
            print("Invalid habit number.")
            return

        habit = habits[number - 1]
        today = date.today().isoformat()

        if habit["completed_date"] == today:
            print("You already completed this habit today.")
        else:
            habit["completed_date"] = today
            save_habits(habits)
            print(f"Great job! '{habit['name']}' completed.")

    except ValueError:
        print("Please enter a valid number.")


def remove_habit(habits):
    if not habits:
        print("No habits to remove.")
        return

    view_habits(habits)

    try:
        number = int(input("Enter habit number to remove: "))

        if number < 1 or number > len(habits):
            print("Invalid habit number.")
            return

        removed = habits.pop(number - 1)
        save_habits(habits)
        print(f"'{removed['name']}' was removed.")

    except ValueError:
        print("Please enter a valid number.")


def show_progress(habits):
    if not habits:
        print("Add some habits to see your progress.")
        return

    # Create a Pandas DataFrame from the habit list
    df = pd.DataFrame(habits)
    today = date.today().isoformat()

    # Use NumPy to determine each habit's status
    df["Status"] = np.where(
        df["completed_date"] == today,
        "Completed",
        "Pending"
    )

    completed = int(np.sum(df["Status"].to_numpy() == "Completed"))
    total = len(df)
    pending = total - completed
    percentage = np.mean(
        df["Status"].to_numpy() == "Completed"
    ) * 100

    print("\n--- TODAY'S PROGRESS ---")
    print(df[["name", "Status"]].to_string(index=False))
    print(f"\nTotal habits     : {total}")
    print(f"Completed        : {completed}")
    print(f"Pending          : {pending}")
    print(f"Completion rate  : {percentage:.1f}%")

    # Draw a pie chart using Matplotlib
    labels = ["Completed", "Pending"]
    values = [completed, pending]

    # Hide categories with zero values
    chart_data = [
        (label, value)
        for label, value in zip(labels, values)
        if value > 0
    ]

    chart_labels = [item[0] for item in chart_data]
    chart_values = [item[1] for item in chart_data]

    plt.figure(figsize=(7, 7))
    plt.pie(
        chart_values,
        labels=chart_labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Daily Habit Progress")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()


def main():
    habits = load_habits()

    while True:
        print("\n=====!!! DAILY HABIT TRACKER !!!=====")
        print("1. Add a habit")
        print("2. View habits")
        print("3. Mark habit as completed")
        print("4. View progress and Pie chart")
        print("5. Remove a habit")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            view_habits(habits)
        elif choice == "3":
            complete_habit(habits)
        elif choice == "4":
            show_progress(habits)
        elif choice == "5":
            remove_habit(habits)
        elif choice == "6":
            print("Keep going, see you tomorrow.")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()