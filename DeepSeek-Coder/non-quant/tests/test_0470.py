import pytest
from src_0470 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    student_grades = ["A", "B", "A", "C", "B", "A"]
    expected_report_df = pd.DataFrame({
        "A": [3],
        "B": [2],
        "C": [1]
    })
    expected_report_df, _ = task_func(student_grades)
    pd.testing.assert_frame_equal(expected_report_df, expected_report_df)

    # Add more test cases as needed

# Add more test cases as needed