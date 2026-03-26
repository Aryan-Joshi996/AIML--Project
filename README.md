# AIML--Project
# Student Grade Analyzer

A command-line tool to analyze student grade data from a CSV file.  
Built with pure Python — no external libraries required.

---

## What It Does

- Loads student marks from a CSV file
- Calculates percentage and letter grade for every record
- Shows per-student and per-subject summaries
- Displays grade distribution with a simple bar chart
- Highlights failing students (below 50%)
- Ranks top 3 students by overall average
- Lets you search for any student by name
- Shows class-wide statistics (mean, median, std deviation)

---

## Project Structure

```
student_grade_analyzer/
├── grade_analyzer.py   # Main program
├── grades.csv          # Sample data (edit or replace with your own)
└── README.md           # This file
```

---

## Requirements

- Python 3.10 or higher
- No external libraries needed (uses only `csv`, `statistics`, `collections`, `os`)

---

## How to Run

1. Make sure `grade_analyzer.py` and `grades.csv` are in the same folder.

2. Open a terminal in that folder and run:

```bash
python grade_analyzer.py
```

3. When prompted, press **Enter** to use `grades.csv`, or type a custom file path.

4. Use the numbered menu to explore the analysis.

---

## CSV Format

Your CSV file must have exactly these column names:

```
name,subject,marks,max_marks
Aarav Sharma,Mathematics,88,100
Priya Patel,Science,85,100
...
```

| Column      | Description                          |
|-------------|--------------------------------------|
| `name`      | Full name of the student             |
| `subject`   | Subject name                         |
| `marks`     | Marks obtained                       |
| `max_marks` | Maximum marks for that subject       |

---

## Grade Scale

| Grade | Percentage  |
|-------|-------------|
| A+    | 90% and above |
| A     | 80 – 89%    |
| B     | 70 – 79%    |
| C     | 60 – 69%    |
| D     | 50 – 59%    |
| F     | Below 50%   |

---

## Menu Options

```
[1]  View all records
[2]  Student-wise summary
[3]  Subject-wise summary
[4]  Grade distribution
[5]  Top 3 students
[6]  Failing students alert
[7]  Overall class statistics
[8]  Search a student
[0]  Exit
```

## Data Structures Used

| Structure       | Where used                                      |
|-----------------|-------------------------------------------------|
| `list[dict]`    | Storing all student records                     |
| `dict`          | Per-student and per-subject aggregated stats    |
| `defaultdict`   | Grouping records by name/subject                |
| `set`           | Finding unique subjects                         |
| `list of tuples`| Ranked top-student results                      |

---

