import pytest
from src_0839 import task_func

def test_task_func():
    # Test case 1: input is a string
    input_text = "Hello, World!"
    expected_output = "hello, world!"
    assert task_func(input_text) == expected_output

    # Test case 2: input is a list of strings
    input_text = ["Hello, World!", "Goodbye, World!"]
    expected_output = ["hello, world!", "goodbye, world!"]
    assert task_func(input_text) == expected_output

    # Test case 3: input is a Series
    input_text = pd.Series(["Hello, World!", "Goodbye, World!"])
    expected_output = pd.Series(["hello, world!", "goodbye, world!"])
    assert task_func(input_text) == expected_output

    # Test case 4: input is a DataFrame
    input_text = pd.DataFrame({"text": ["Hello, World!", "Goodbye, World!"]})
    expected_output = pd.DataFrame({"text": ["hello, world!", "goodbye, world!"]})
    assert task_func(input_text) == expected_output

    # Test case 5: input is a Series with non-string values
    input_text = pd.Series([1, 2, 3])
    expected_output = pd.Series([1, 2, 3])
    assert task_func(input_text) == expected_output

    # Test case 6: input is a DataFrame with non-string values
    input_text = pd.DataFrame({"text": [1, 2, 3]})
    expected_output = pd.DataFrame({"text": [1, 2, 3]})
    assert task_func(input_text) == expected_output