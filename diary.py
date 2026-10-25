
import json
import os
from datetime import date

FILE_NAME = "diary.json"


def load_entries():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read diary file.")
        return []


def save_entries(entries):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(entries, file, indent=4)


def create_entry(entries):
    today = date.today().isoformat()

    learning = input("What did you learn today? ").strip()
    if not learning:
        print("Please enter something you learned.")
        return

    mood = input("How is your mood? (Happy/Okay/Low): ").strip().capitalize()

    if mood not in ["Happy", "Okay", "Low"]:
        print("Please choose Happy, Okay, or Low.")
        return

    habit = input("Did you complete a positive habit? (yes/no): ")
    habit = habit.strip().lower()

    if habit not in ["yes", "no"]:
        print("Please enter yes or no.")
        return

    score = 5

    if mood == "Happy":
        score += 2
    elif mood == "Okay":
        score += 1

    if habit == "yes":
        score += 3

    entry = {
        "date": today,
        "learning": learning,
        "mood": mood,
        "habit_completed": habit == "yes",
        "growth_score": score
    }

    entries.append(entry)
    save_entries(entries)

    print("\n🌱 Daily entry saved!")
    print(f"Your growth score today: {score}/10")
    print("Every small step matters!")


def view_entries(entries):
    if not entries:
        print("\nNo diary entries yet.")
        return

    print("\n========== YOUR GROWTH DIARY ==========")

    for entry in entries:
        habit = "Yes" if entry["habit_completed"] else "No"

        print(f"\nDate: {entry['date']}")
        print(f"Learning: {entry['learning']}")
        print(f"Mood: {entry['mood']}")
        print(f"Positive habit completed: {habit}")
        print(f"Growth score: {entry['growth_score']}/10")

    print("\n=======================================")


def show_statistics(entries):
    if not entries:
        print("\nAdd your first diary entry to see statistics.")
        return

    total = len(entries)
    average = sum(
        entry["growth_score"] for entry in entries
    ) / total

    habits = sum(
        entry["habit_completed"] for entry in entries
    )

    print("\n======= YOUR STATISTICS =======")
    print(f"Total entries: {total}")
    print(f"Average growth score: {average:.1f}/10")
    print(f"Positive habits completed: {habits}")
    print("===============================")


def main():
    entries = load_entries()

    while True:
        print("\n🌱 DIGITAL FOOTPRINT DIARY")
        print("1. Add today's entry")
        print("2. View diary history")
        print("3. View statistics")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            create_entry(entries)
        elif choice == "2":
            view_entries(entries)
        elif choice == "3":
            show_statistics(entries)
        elif choice == "4":
            print("Keep growing every day! Goodbye 🌿")
            break
        else:
            print("Invalid choice. Choose 1-4.")


if __name__ == "__main__":
    main()
