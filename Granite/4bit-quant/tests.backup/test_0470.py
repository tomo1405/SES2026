import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
def task_func(student_grades, possible_grades=["A", "B", "C", "D", "F"]):
    if not student_grades:
        raise ValueError("student_grades cannot be empty")
    possible_grades = [*dict.fromkeys([g.upper() for g in possible_grades])]
    grade_counts = dict(Counter([g.upper() for g in student_grades]))
    report_data = {grade: grade_counts.get(grade, 0) for grade in possible_grades}
    report_df = pd.DataFrame.from_dict(report_data, orient="index", columns=["Count"])
    report_df.index.name = "Grade"

    ax = report_df.plot(kind="bar", legend=False, title="Grade Distribution")
    ax.set_ylabel("Number of Students")
    ax.set_xlabel("Grade")

    plt.tight_layout()

    return report_df, ax
import pytest

def test_task_func():
    student_grades = ["A", "B", "C", "D", "F", "A", "B", "C", "D", "F", "A", "B", "C", "D", "F"]
    possible_grades = ["A", "B", "C", "D", "F"]
    report_df, ax = task_func(student_grades, possible_grades)
    assert report_df.shape == (5, 1)
    assert report_df.index.name == "Grade"
    assert report_df.columns[0] == "Count"
    assert ax.get_ylabel() == "Number of Students"
    assert ax.get_xlabel() == "Grade"
    assert ax.get_title() == "Grade Distribution"

if __name__ == "__main__":
    pytest.main()