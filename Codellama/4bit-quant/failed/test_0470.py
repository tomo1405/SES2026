import pytest
from src_0470 import task_func

def test_task_func():
    student_grades = ["A", "B", "C", "D", "F"]
    possible_grades = ["A", "B", "C", "D", "F"]
    report_df, ax = task_func(student_grades, possible_grades)
    assert report_df.equals(pd.DataFrame({"A": 1, "B": 1, "C": 1, "D": 1, "F": 1}, index=["A", "B", "C", "D", "F"]))
    assert ax.get_title() == "Grade Distribution"
    assert ax.get_ylabel() == "Number of Students"
    assert ax.get_xlabel() == "Grade"
    assert ax.get_legend() == False
    assert ax.get_tight_layout() == True