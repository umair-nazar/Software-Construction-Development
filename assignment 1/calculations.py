"""Business rules and calculations for student results."""


def calculate_total(marks):
    """Return the sum of all subject marks."""
    return sum(marks)


def calculate_average(marks):
    """Return the average of the supplied marks."""
    if not marks:
        raise ValueError("Marks list cannot be empty.")
    return calculate_total(marks) / len(marks)


def calculate_grade(average):
    """Return a letter grade using the original grading thresholds."""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"
