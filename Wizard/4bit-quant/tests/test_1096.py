python
import os
import pytest
from src_1096 import task_func

def test_task_func():
    text = "This is a sample text with $100 and $200 dollars."
    output_filename = "output.txt"

    # Test case 1: Valid dollar words are extracted
    valid_dollar_words = ["$100", "$200"]
    expected_output = os.path.abspath(output_filename)
    actual_output = task_func(text, output_filename)
    assert actual_output == expected_output
    with open(output_filename, 'r') as file:
        actual_output_words = file.readlines()
    assert actual_output_words == valid_dollar_words

    # Test case 2: Invalid dollar words are not extracted
    invalid_dollar_words = ["$1000", "$2000"]
    expected_output = os.path.abspath(output_filename)
    actual_output = task_func(text, output_filename)
    assert actual_output == expected_output
    with open(output_filename, 'r') as file:
        actual_output_words = file.readlines()
    assert actual_output_words == valid_dollar_words

    # Test case 3: Output file is created if it doesn't exist
    os.remove(output_filename)
    expected_output = os.path.abspath(output_filename)
    actual_output = task_func(text, output_filename)
    assert actual_output == expected_output
    assert os.path.exists(output_filename)

    # Test case 4: Output file is overwritten if it exists
    with open(output_filename, 'w') as file:
        file.write("This is a sample text with $100 and $200 dollars.")
    expected_output = os.path.abspath(output_filename)
    actual_output = task_func(text, output_filename)
    assert actual_output == expected_output
    with open(output_filename, 'r') as file:
        actual_output_words = file.readlines()
    assert actual_output_words == valid_dollar_words