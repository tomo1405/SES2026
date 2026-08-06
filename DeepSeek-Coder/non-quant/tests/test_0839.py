import pytest
from src_0839 import task_func

# Test cases
def test_task_func():
    # Test case 1
    text_series = pd.Series(["Hello World!", "This is a test."])
    expected_output = pd.Series(["hello world", "this is a test"])
    assert task_func(text_series) == expected_output

    # Add more test cases as needed