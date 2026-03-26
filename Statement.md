# Project Statement: Student Grade Analyser

## 1. Project Overview
The **Student Grade Analyser** is a Python-based CLI tool designed to automate the processing and analysis of academic performance data. It serves as a digital solution to replace manual grading systems, aiming to provide error-free calculations and actionable insights for educators.

## 2. Problem Statement
Manual record-keeping in educational institutions is prone to human error, time-consuming, and often fails to provide a clear picture of student progress over time. There is a critical need for a system that can quickly identify "at-risk" students and visualize grade distributions to improve academic outcomes.

## 3. Objectives
* **Automated Computation:** Use Python data structures to calculate GPAs, CGPAs, and subject-wise averages instantly.
* **Trend Visualization:** Create visual representations of performance to track improvement or decline.
* **Early Intervention:** Flag students scoring below 50% to allow for timely academic support.
* **Data Centralization:** Provide a searchable interface to retrieve individual student records and class statistics.

## 4. Scope of Work
* **In-Scope:**
    * Functional modules for data ingestion via CSV files.
    * Statistical analysis including Mean, Median, and Standard Deviation.
    * Interactive menu for searching records and viewing summaries.
    * Generation of grade distribution charts (A+ to F).
* **Out-of-Scope:**
    * Financial or fee management systems.
    * Attendance tracking and behavioral assessment.

## 5. Technical Stack
* **Language:** Python 3.x.
* **Libraries:** `csv` for data handling, `statistics` for mathematical operations, and `collections` (defaultdict) for data grouping.
* **Data Format:** CSV (Comma Separated Values).

## 6. Expected Results
The project delivers a functional tool that accurately ranks the top 3 students, alerts faculty to failing marks, and provides a comprehensive subject-wise performance breakdown. It establishes a foundation for future AI-driven predictive analytics in student grading.
