import pytest
from src_1096 import task_func

def test_task_func():
    text = "This is a test text with $dollar_prefixed_words and punctuation."
    output_filename = "test_output.txt"
    expected_output = ["$dollar_prefixed_words"]

    result = task_func(text, output_filename)

    with open(output_filename, 'r') as file:
        actual_output = file.read().splitlines()

    assert actual_output == expected_output
    os.remove(output_filename)