import pandas as pd
from src_0057 import task_func


def test_task_func_no_matches():
    text = "No scores or categories here."
    result = task_func(text)
    assert result.empty

def test_task_func_single_match():
    text = "Score: 10, Category: Math"
    result = task_func(text)
    expected_df = pd.DataFrame({"Score": [10], "Category": ["Math"]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_multiple_matches():
    text = "Score: 10, Category: Math\nScore: 20, Category: Science"
    result = task_func(text)
    expected_df = pd.DataFrame({"Score": [10, 20], "Category": ["Math", "Science"]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_trailing_newline():
    text = "Score: 10, Category: Math\n"
    result = task_func(text)
    expected_df = pd.DataFrame({"Score": [10], "Category": ["Math"]})
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_invalid_format():
    text = "Score: 10, Category: Math\nInvalid line"
    result = task_func(text)
    expected_df = pd.DataFrame({"Score": [10], "Category": ["Math"]})
    pd.testing.assert_frame_equal(result, expected_df)