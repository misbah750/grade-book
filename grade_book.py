# grade_book.py
# A simple command-line grade book.

students = {}  # name -> list of marks


def show_menu():
    print("\n=== Grade Book ===")
    print("1. Add student")
    print("2. Show grades")
    print("0. Exit")


def calculate_grade(average):
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 55:
        return "C"
    elif average >= 40:
        return "D"
    return "F"


def show_grades():
    if not students:
        print("No students yet.")
        return
    for name, marks in students.items():
        average = sum(marks) / len(marks)
        print(f"{name}: average {average:.1f}, grade {calculate_grade(average)}")

    
    print("0. Exit")


def add_student():
    name = input("Student name: ")
    marks = input("Marks separated by spaces: ")
    try:
        students[name] = [int(m) for m in marks.split()]
    except ValueError:
        print("Marks must be whole numbers. Student not added.")
        return
    print(f"Added {name}.")



def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":

            show_grades()

            add_student()

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()