import pytest
from src_1096 import task_func

def test_task_func():
    text = "This is a test text with $dollar_words and punctuation."
    output_filename = "output.txt"
    expected_output = "dollar_words\n"

    result = task_func(text, output_filename)

    with open(output_filename, 'r') as file:
        actual_output = file.read()

    assert actual_output == expected_output
    os.remove(output_filename)