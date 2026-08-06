python
import re
import pandas as pd

def task_func(input_string: str) -> pd.DataFrame:
    input_string = input_string.replace('\\n', '\n').replace('\\t', ' ')
    # Split the input string into lines and filter out empty lines
    lines = [line for line in input_string.split("\n") if line.strip()]
    # Replace tabs with spaces in each line
    lines = [re.sub("\t", " ", line) for line in lines]
    # Create a DataFrame from the processed lines
    return pd.DataFrame(lines, columns=["Text"])

# Test the function with some sample inputs
def test_task_func():
    # Test case 1
    input_string = "Line 1\t\tLine 2\nLine 3\t\tLine 4\n"
    expected_output = pd.DataFrame(["Line 1 Line 2", "Line 3 Line 4"], columns=["Text"])
    assert task_func(input_string).equals(expected_output)

    # Test case 2
    input_string = "Line 1\t\tLine 2\nLine 3\t\tLine 4\n\n"
    expected_output = pd.DataFrame(["Line 1 Line 2", "Line 3 Line 4"], columns=["Text"])
    assert task_func(input_string).equals(expected_output)

    # Test case 3
    input_string = "Line 1\t\tLine 2\nLine 3\t\tLine 4\n\n\n"
    expected_output = pd.DataFrame(["Line 1 Line 2", "Line 3 Line 4"], columns=["Text"])
    assert task_func(input_string).equals(expected_output)

    # Test case 4
    input_string = "Line 1\t\tLine 2\nLine 3\t\tLine 4\n\n\n\n"
    expected_output = pd.DataFrame(["Line 1 Line 2", "Line 3 Line 4"], columns=["Text"])
    assert task_func(input_string).equals(expected_output)

    # Test case 5
    input_string = "Line 1\t\tLine 2\nLine 3\t\tLine 4\n\n\n\n\n"
    expected_output = pd.DataFrame(["Line 1 Line 2", "Line 3 Line 4"], columns=["Text"])
    assert task_func(input_string).equals(expected_output)

    # Test case 6
    input_string = "Line 1\t\tLine 2\nLine 3\t\tLine 4\n\n\n\n\n\n"
    expected_output = pd.DataFrame(["Line 1 Line 2", "Line 3 Line 4"], columns=["Text"])
    assert task_func(input_string).equals(expected_output)

    # Test case 7
    input_string = "Line 1\t\tLine 2\nLine 3\t\tLine 4\n\n\n\n\n\n\n"
    expected_output = pd.DataFrame(["Line 1 Line 2", "Line 3 Line 4"], columns=["Text"])
    assert task_func(input_string).equals(expected_output)

    # Test case 8
    input_string = "Line 1\t\tLine 2\nLine 3\t\tLine 4\n\n\n\n\n\n\n\n"
    expected_output = pd.DataFrame(["Line 1 Line 2", "Line 3 Line 4"], columns=["Text"])
    assert task_func(input_string).equals(expected_output)

    # Test case 9
    input_string = "Line 1\t\tLine 2\nLine 3\t\tLine 4\n\n\n\n\n\n\n\n\n"
    expected_output = pd.DataFrame(["Line 1 Line 2", "Line 3 Line 4"], columns=["Text"])
    assert task_func(input_string).equals(expected_output)

    # Test case 10
    input_string = "Line 1\t\tLine 2\nLine 3\t\tLine 4\n\n\n\n\n\n\n\n\n\n"
    expected_output = pd.DataFrame(["Line 1 Line 2", "Line 3 Line 4"], columns=["Text"])
    assert task_func(input_string).equals(expected_output)

# Run the tests
test_task_func()