FILE_NAME = "feedback.txt"

# Function to add feedback
def add_feedback():
    name = input("Enter student name: ")
    feedback = input("Enter feedback: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name}|{feedback}\n")

    print(" Feedback added successfully!")


# Function to add multiple feedbacks
def fill_multiple_feedback():
    n = int(input("How many feedbacks do you want to add? "))
    for _ in range(n):
        add_feedback()

def display_feedback():
    try:
        search_name = input("Enter student name to search: ").lower()
        found = False

        with open(FILE_NAME, "r") as file:
            print("\n--- Feedback for Student ---")
            for line in file:
                name, feedback = line.strip().split("|")

                if name.lower() == search_name:
                    print(f"Name: {name}")
                    print(f"Feedback: {feedback}")
                    print("-" * 30)
                    found = True

        if not found:
            print(" No feedback found for this student.")

    except FileNotFoundError:
        print("No feedback file found!")

# Function to search feedback
def search_feedback():
    keyword = input("Enter keyword to search: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                if keyword.lower() in line.lower():
                    print(line.strip())
                    found = True

        if not found:
            print(" No matching feedback found.")
    except FileNotFoundError:
        print("No feedback file found!")


# Function to analyze feedback
def analyze_feedback():
    positive_words = ["good", "excellent", "great", "nice", "amazing"]
    negative_words = ["bad", "poor", "worst", "terrible"]

    positive = 0
    negative = 0

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                feedback = line.split("|")[1].lower()

                if any(word in feedback for word in positive_words):
                    positive += 1
                elif any(word in feedback for word in negative_words):
                    negative += 1

        print("\nFeedback Analysis")
        print(f"Positive Feedback: {positive}")
        print(f"Negative Feedback: {negative}")

    except FileNotFoundError:
        print("No feedback file found!")


# Main menu
def main():
    while True:
        print("\n--- Student Feedback Management System ---")
        print("1. Add Feedback")
        print("2. Fill Multiple Feedback")
        print("3. Display Feedback")
        print("4. Search Feedback")
        print("5. Analyze Feedback")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_feedback()
        elif choice == "2":
            fill_multiple_feedback()
        elif choice == "3":
            display_feedback()
        elif choice == "4":
            search_feedback()
        elif choice == "5":
            analyze_feedback()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


# Run program
main()