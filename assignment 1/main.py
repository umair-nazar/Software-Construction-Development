"""Application entry point: coordinates input, logic, and output."""

from validation import validate_mark
from calculations import calculate_total, calculate_average, calculate_grade
from display import display_result


def read_valid_mark(subject_number):
    """Read a mark until a valid value from 0 to 100 is entered."""
    while True:
        try:
            mark = float(input(f"Enter marks for subject {subject_number}: "))
        except ValueError:
            print("Invalid input. Enter a number from 0 to 100.")
            continue

        if validate_mark(mark):
            return mark

        print("Invalid marks. Enter 0-100.")


def main():
    name = input("Enter student name: ")
    marks = []

    for i in range(3):
        marks.append(read_valid_mark(i + 1))

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    display_result(name, total, average, grade)


if __name__ == "__main__":
    main()
