"""
Student Grade Analyzer
A CLI tool to analyze student grades using Python data structures.
"""
 
import csv
import os
import statistics
from collections import defaultdict
 
#  Data Loading
 
def load_grades(filepath: str) -> list[dict]:
    """Load student grade data from a CSV file."""
    students = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append({
                "name":    row["name"].strip(),
                "subject": row["subject"].strip(),
                "marks":   float(row["marks"]),
                "max":     float(row["max_marks"]),
            })
    return students
 

#  Core Analysis (uses lists, dicts, sets)
 
def compute_percentages(students: list[dict]) -> list[dict]:
    """Add percentage and letter grade to each record."""
    for s in students:
        s["percent"] = round((s["marks"] / s["max"]) * 100, 2)
        s["grade"]   = assign_grade(s["percent"])
    return students
 
 
def assign_grade(percent: float) -> str:
    """Convert percentage to letter grade."""
    if percent >= 90: return "A+"
    if percent >= 80: return "A"
    if percent >= 70: return "B"
    if percent >= 60: return "C"
    if percent >= 50: return "D"
    return "F"
 
 
def student_summary(students: list[dict]) -> dict:
    """Per-student aggregated stats using a dict of lists."""
    by_student: dict[str, list[float]] = defaultdict(list)
    for s in students:
        by_student[s["name"]].append(s["percent"])
 
    summary = {}
    for name, percents in by_student.items():
        summary[name] = {
            "average":  round(statistics.mean(percents), 2),
            "highest":  max(percents),
            "lowest":   min(percents),
            "subjects": len(percents),
        }
    return summary
 
 
def subject_summary(students: list[dict]) -> dict:
    """Per-subject stats."""
    by_subject: dict[str, list[float]] = defaultdict(list)
    for s in students:
        by_subject[s["subject"]].append(s["percent"])
 
    summary = {}
    for subj, percents in by_subject.items():
        summary[subj] = {
            "average": round(statistics.mean(percents), 2),
            "highest": max(percents),
            "lowest":  min(percents),
            "students": len(percents),
        }
    return summary
 
 
def grade_distribution(students: list[dict]) -> dict:
    """Count how many students fall in each grade bucket."""
    dist: dict[str, int] = defaultdict(int)
    for s in students:
        dist[s["grade"]] += 1
    return dict(dist)
 
 
def top_students(students: list[dict], n: int = 3) -> list[tuple]:
    """Return top-n students by average percentage."""
    summary = student_summary(students)
    ranked = sorted(summary.items(), key=lambda x: x[1]["average"], reverse=True)
    return ranked[:n]
 
 
def failing_students(students: list[dict]) -> list[dict]:
    """Return records where the student scored below 50%."""
    return [s for s in students if s["percent"] < 50]
 
 
def unique_subjects(students: list[dict]) -> set:
    """Return a set of all subjects in the dataset."""
    return {s["subject"] for s in students}
  
#  Display Helpers
 
SEP  = "─" * 60
SEP2 = "═" * 60
 
def header(title: str):
    print(f"\n{SEP2}")
    print(f"{title}")
    print(SEP2)
 
def section(title: str):
    print(f"\n{SEP}")
    print(f"{title}")
    print(SEP)
 
 
def print_all_records(students: list[dict]):
    header("ALL STUDENT RECORDS")
    print(f"{'Name':<20} {'Subject':<15} {'Marks':>7} {'Max':>6} {'%':>7} {'Grade':>6}")
    print(SEP)
    for s in students:
        print(f"{s['name']:<20} {s['subject']:<15} {s['marks']:>7.1f} {s['max']:>6.1f} {s['percent']:>7.2f} {s['grade']:>6}")
 
 
def print_student_summary(students: list[dict]):
    section("STUDENT-WISE SUMMARY")
    summary = student_summary(students)
    print(f"{'Student':<20} {'Avg %':>8} {'Highest':>9} {'Lowest':>8} {'Subjects':>9}")
    print(SEP)
    for name, data in sorted(summary.items()):
        print(f"{name:<20} {data['average']:>8.2f} {data['highest']:>9.2f} {data['lowest']:>8.2f} {data['subjects']:>9}")
 
 
def print_subject_summary(students: list[dict]):
    section("SUBJECT-WISE SUMMARY")
    summary = subject_summary(students)
    print(f"{'Subject':<18} {'Avg %':>8} {'Highest':>9} {'Lowest':>8} {'Students':>9}")
    print(SEP)
    for subj, data in sorted(summary.items()):
        print(f"{subj:<18} {data['average']:>8.2f} {data['highest']:>9.2f} {data['lowest']:>8.2f} {data['students']:>9}")
 
 
def print_grade_distribution(students: list[dict]):
    section("GRADE DISTRIBUTION")
    dist = grade_distribution(students)
    order = ["A+", "A", "B", "C", "D", "F"]
    total = len(students)
    for g in order:
        count = dist.get(g, 0)
        bar   = "█" * count
        print(f"  {g:>3}  {bar:<30}  {count} ({count/total*100:.1f}%)")
 
 
def print_top_students(students: list[dict]):
    section("TOP 3 STUDENTS (by overall average)")
    top = top_students(students)
    for rank, (name, data) in enumerate(top, 1):
        print(f"  #{rank}  {name:<20}  Avg: {data['average']:.2f}%")
 
 
def print_failing_alert(students: list[dict]):
    section(" STUDENTS WITH FAILING MARKS (< 50%)")
    failing = failing_students(students)
    if not failing:
        print("No failing records found.")
    else:
        print(f"{'Name':<20} {'Subject':<15} {'Marks':>7} {'%':>7}")
        print(SEP)
        for s in failing:
            print(f"{s['name']:<20} {s['subject']:<15} {s['marks']:>7.1f} {s['percent']:>7.2f}")
 
 
def print_class_stats(students: list[dict]):
    section("OVERALL CLASS STATISTICS")
    all_pct = [s["percent"] for s in students]
    print(f"  Total records  : {len(students)}")
    print(f"  Unique students: {len(student_summary(students))}")
    print(f"  Unique subjects: {len(unique_subjects(students))}")
    print(f"  Class average  : {statistics.mean(all_pct):.2f}%")
    print(f"  Median         : {statistics.median(all_pct):.2f}%")
    print(f"  Std deviation  : {statistics.stdev(all_pct):.2f}%")
    print(f"  Highest score  : {max(all_pct):.2f}%")
    print(f"  Lowest score   : {min(all_pct):.2f}%")
 
#  Interactive Menu
 
def search_student(students: list[dict]):
    name = input("\n  Enter student name to search: ").strip().lower()
    results = [s for s in students if s["name"].lower() == name]
    if not results:
        print(f"  No records found for '{name}'.")
        return
    print(f"\n  Results for: {results[0]['name']}")
    print(f"  {'Subject':<15} {'Marks':>7} {'Max':>6} {'%':>7} {'Grade':>6}")
    print("  " + "─" * 45)
    for s in results:
        print(f"  {s['subject']:<15} {s['marks']:>7.1f} {s['max']:>6.1f} {s['percent']:>7.2f} {s['grade']:>6}")
    avg = statistics.mean([s["percent"] for s in results])
    print(f"\n  Overall average: {avg:.2f}%")
 
 
def menu(students: list[dict]):
    options = {
        "1": ("View all records",        lambda: print_all_records(students)),
        "2": ("Student-wise summary",    lambda: print_student_summary(students)),
        "3": ("Subject-wise summary",    lambda: print_subject_summary(students)),
        "4": ("Grade distribution",      lambda: print_grade_distribution(students)),
        "5": ("Top 3 students",          lambda: print_top_students(students)),
        "6": ("Failing students alert",  lambda: print_failing_alert(students)),
        "7": ("Overall class statistics",lambda: print_class_stats(students)),
        "8": ("Search a student",        lambda: search_student(students)),
        "0": ("Exit",                    None),
    }
 
    while True:
        print(f"\n{'═'*40}")
        print("   STUDENT GRADE ANALYZER — MENU")
        print(f"{'═'*40}")
        for key, (label, _) in options.items():
            print(f"[{key}]  {label}")
        choice = input("\n  Choose an option: ").strip()
        if choice == "0":
            print("\n  Goodbye!\n")
            break
        elif choice in options:
            options[choice][1]()
        else:
            print("  Invalid choice. Please try again.")
 
 
#  Entry Point

 
def main():
    print("\n" + "═" * 60)
    print("STUDENT GRADE ANALYZER")
    print("Python & Data Structures")
    print("═" * 60)
 
    default_file = "grades.csv"
    filepath = input(f"\n  Enter CSV file path [{default_file}]: ").strip()
    if not filepath:
        filepath = default_file
 
    if not os.path.exists(filepath):
        print(f"\n  ✗ File not found: '{filepath}'")
        print(" Make sure grades.csv is in the same folder.\n")
        return
 
    students = load_grades(filepath)
    students = compute_percentages(students)
    print(f"\n  ✓ Loaded {len(students)} records from '{filepath}'")
    menu(students)
 
 
if __name__ == "__main__":
    main()
