import pytest
from src_0057 import task_func

def test_task_func():
    text = """
    Here are some matches:
    Score: 10, Category: Example
    Score: 20, Category: Another Example
    Score: 30, Category: Yet Another Example
    """
    expected_df = pd.DataFrame({
        "Score": [10, 20, 30],
        "Category": ["Example", "Another Example", "Yet Another Example"]
    })
    actual_df = task_func(text)
    pd.testing.assert_frame_equal(actual_df, expected_df)

def test_task_func_with_no_matches():
    text = "No matches found."
    expected_df = pd.DataFrame(columns=["Score", "Category"])
    actual_df = task_func(text)
    pd.testing.assert_frame_equal(actual_df, expected_df)