import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0470 import task_func


def test_task_func_empty_input():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_valid_input():
    student_grades = ["A", "b", "c", "A", "D", "f", "B", "a", "C"]
    possible_grades = ["A", "B", "C", "D", "F"]
    report_df, ax = task_func(student_grades, possible_grades)
    
    expected_data = {
        "Grade": ["A", "B", "C", "D", "F"],
        "Count": [3, 1, 2, 1, 1]
    }
    expected_df = pd.DataFrame(expected_data).set_index("Grade")
    
    pd.testing.assert_frame_equal(report_df, expected_df)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_missing_grades():
    student_grades = ["A", "b", "c", "A", "D", "f", "B", "a", "C"]
    possible_grades = ["A", "B", "C", "D", "E", "F"]
    report_df, ax = task_func(student_grades, possible_grades)
    
    expected_data = {
        "Grade": ["A", "B", "C", "D", "E", "F"],
        "Count": [3, 1, 2, 1, 0, 1]
    }
    expected_df = pd.DataFrame(expected_data).set_index("Grade")
    
    pd.testing.assert_frame_equal(report_df, expected_df)
    assert isinstance(ax, plt.Axes)

def test_task_func_case_insensitivity():
    student_grades = ["a", "B", "c", "A", "d", "F", "b", "A", "C"]
    possible_grades = ["a", "b", "c", "d", "e", "f"]
    report_df, ax = task_func(student_grades, possible_grades)
    
    expected_data = {
        "Grade": ["A", "B", "C", "D", "E", "F"],
        "Count": [3, 2, 2, 1, 0, 1]
    }
    expected_df = pd.DataFrame(expected_data).set_index("Grade")
    
    pd.testing.assert_frame_equal(report_df, expected_df)
    assert isinstance(ax, plt.Axes)