import pytest
from src_1097 import task_func

def test_task_func():
    text = "This is a test text with $dollar_prefixed_words."
    filename = "test_file.csv"
    expected_output = "Word\n$dollar_prefixed_words\n"

    output = task_func(text, filename)

    with open(output, 'r') as f:
        reader = csv.reader(f)
        actual_output = [row for row in reader]

    assert actual_output == expected_output