import pandas as pd
from src_1050 import task_func


def test_task_func():
    # Test case 1: input string with newlines and tabs
    input_string = "Hello\n\tWorld"
    expected_output = pd.DataFrame({"Text": ["Hello World"]})
    assert task_func(input_string).equals(expected_output)

    # Test case 2: input string with multiple newlines and tabs
    input_string = "Hello\n\tWorld\n\n\t\tPython"
    expected_output = pd.DataFrame({"Text": ["Hello World", "Python"]})
    assert task_func(input_string).equals(expected_output)

    # Test case 3: input string with no newlines or tabs
    input_string = "Hello World"
    expected_output = pd.DataFrame({"Text": ["Hello World"]})
    assert task_func(input_string).equals(expected_output)

    # Test case 4: input string with empty lines
    input_string = "Hello\n\n\nWorld"
    expected_output = pd.DataFrame({"Text": ["Hello", "World"]})
    assert task_func(input_string).equals(expected_output)

    # Test case 5: input string with multiple empty lines
    input_string = "Hello\n\n\n\nWorld"
    expected_output = pd.DataFrame({"Text": ["Hello", "World"]})
    assert task_func(input_string).equals(expected_output)