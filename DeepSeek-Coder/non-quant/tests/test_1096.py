import pytest
from src_1096 import task_func

def test_task_func():
    # Test case 1: Basic functionality test
    text = "This is a test $word1 and $word2."
    output_filename = "test_output.txt"
    expected_output = os.path.abspath(output_filename)
    result = task_func(text, output_filename)
    assert result == expected_output
    with open(output_filename, 'r') as file:
        content = file.read().strip()
        assert content == "word1"

    # Add more test cases as needed