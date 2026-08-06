import pytest
from src_0470 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def test_task_func_empty_input():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_valid_input():
    student_grades = ["A", "B", "C", "A", "B", "A"]
    report_df, ax = task_func(student_grades)
    
    # Check DataFrame content
    expected_data = {"Count": [3, 2, 1, 0, 0]}
    expected_df = pd.DataFrame(expected_data, index=["A", "B", "C", "D", "F"])
    expected_df.index.name = "Grade"
    pd.testing.assert_frame_equal(report_df, expected_df)
    
    # Check plot properties
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Grade Distribution"
    assert ax.get_ylabel() == "Number of Students"
    assert ax.get_xlabel() == "Grade"

def test_task_func_with_custom_possible_grades():
    student_grades = ["A", "B", "C", "A", "B", "A"]
    possible_grades = ["A", "B", "C", "E"]
    report_df, ax = task_func(student_grades, possible_grades=possible_grades)
    
    # Check DataFrame content
    expected_data = {"Count": [3, 2, 1, 0]}
    expected_df = pd.DataFrame(expected_data, index=["A", "B", "C", "E"])
    expected_df.index.name = "Grade"
    pd.testing.assert_frame_equal(report_df, expected_df)
    
    # Check plot properties
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Grade Distribution"
    assert ax.get_ylabel() == "Number of Students"
    assert ax.get_xlabel() == "Grade"

def test_task_func_case_insensitivity():
    student_grades = ["a", "b", "c", "A", "B", "a"]
    report_df, ax = task_func(student_grades)
    
    # Check DataFrame content
    expected_data = {"Count": [3, 2, 1, 0, 0]}
    expected_df = pd.DataFrame(expected_data, index=["A", "B", "C", "D", "F"])
    expected_df.index.name = "Grade"
    pd.testing.assert_frame_equal(report_df, expected_df)
    
    # Check plot properties
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Grade Distribution"
    assert ax.get_ylabel() == "Number of Students"
    assert ax.get_xlabel() == "Grade"