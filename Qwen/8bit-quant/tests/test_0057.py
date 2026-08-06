import pandas as pd
from src_0057 import task_func


def test_task_func_no_matches():
    text = "No scores or categories here."
    result = task_func(text)
    assert result.empty

def test_task_func_single_match():
    text = "Score: 100, Category: Math"
    result = task_func(text)
    expected_df = pd.DataFrame({"Score": [100], "Category": ["Math"]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_multiple_matches():
    text = "Score: 85, Category: Science\nScore: 90, Category: History"
    result = task_func(text)
    expected_df = pd.DataFrame({"Score": [85, 90], "Category": ["Science", "History"]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_with_trailing_newline():
    text = "Score: 75, Category: Art\n"
    result = task_func(text)
    expected_df = pd.DataFrame({"Score": [75], "Category": ["Art"]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_with_non_numeric_score():
    text = "Score: abc, Category: Literature"
    result = task_func(text)
    assert result.empty

def test_task_func_with_empty_category():
    text = "Score: 60, Category:"
    result = task_func(text)
    expected_df = pd.DataFrame({"Score": [60], "Category": [None]})
    pd.testing.assert_frame_equal(result, expected_df)