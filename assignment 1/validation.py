"""Input validation helpers for student marks."""


def validate_mark(mark):
    """Return True if mark is between 0 and 100 inclusive."""
    return 0 <= mark <= 100
