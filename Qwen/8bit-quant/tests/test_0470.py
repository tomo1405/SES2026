import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0470 import task_func


def test_task_func_empty_input():
    with pytest.raises(ValueError, match="student_grades cannot be empty"):
        task_func([])

def test_task_func_valid_input():
    student_grades = ["A", "b", "C", "d", "F", "a", "B"]
    report_df, ax = task_func(student_grades)
    
    expected_data = {
        "A": 2,
        "B": 2,
        "C": 1,
        "D": 1,
        "F": 1
    }
    expected_df = pd.DataFrame.from_dict(expected_data, orient="index", columns=["Count"])
    expected_df.index.name = "Grade"
    
    pd.testing.assert_frame_equal(report_df, expected_df)
    assert isinstance(ax, plt.Axes)

def test_task_func_custom_possible_grades():
    student_grades = ["A", "B", "C", "D", "E", "F"]
    possible_grades = ["A", "B", "C", "D", "E", "F", "G"]
    report_df, ax = task_func(student_grades, possible_grades)
    
    expected_data = {
        "A": 1,
        "B": 1,
        "C": 1,
        "D": 1,
        "E": 0,
        "F": 1,
        "G": 0
    }
    expected_df = pd.DataFrame.from_dict(expected_data, orient="index", columns=["Count"])
    expected_df.index.name = "Grade"
    
    pd.testing.assert_frame_equal(report_df, expected_df)
    assert isinstance(ax, plt.Axes)

def test_task_func_case_insensitivity():
    student_grades = ["a", "B", "c", "D", "f"]
    report_df, ax = task_func(student_grades)
    
    expected_data = {
        "A": 1,
        "B": 1,
        "C": 1,
        "D": 1,
        "F": 1
    }
    expected_df = pd.DataFrame.from_dict(expected_data, orient="index", columns=["Count"])
    expected_df.index.name = "Grade"
    
    pd.testing.assert_frame_equal(report_df, expected_df)
    assert isinstance(ax, plt.Axes)