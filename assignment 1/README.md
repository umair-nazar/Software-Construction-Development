# Student Marks Application — Week 4 Lab

## Run the program
1. Make sure Python 3 is installed.
2. Open a terminal in this folder.
3. Run: `python main.py`

## Modules
- `main.py`: coordinates user input, calculation, grading, and display.
- `validation.py`: checks whether a mark is in the inclusive range 0–100.
- `calculations.py`: calculates total, average, and grade.
- `display.py`: prints the result; it does not calculate anything.

## Dependency diagram
```text
main.py
  |----> validation.py
  |----> calculations.py
  `----> display.py
```

The other three modules do not import `main.py` or each other. `calculations.py` has no dependency on console input/output, and `display.py` does not know how the grade was calculated.

## Important behavior note
The original program accepts numeric marks in the range 0–100 inclusive and uses grade thresholds A >= 80, B >= 70, C >= 60, D >= 50, otherwise F. This version preserves those rules. It additionally handles non-numeric input gracefully.

## Manual test checklist
- Normal marks: 75, 82, 68 → total 225, average 75.0, grade B.
- Boundary marks: test 50, 60, 70, and 80 as averages (for example, enter the same mark three times).
- Invalid marks: -5 and 105 should each show `Invalid marks. Enter 0-100.` and prompt again.
- Second student: enter a different name and marks to verify results are calculated independently.

These are expected outcomes; mark tests as passed only after running the program and checking the actual output.
