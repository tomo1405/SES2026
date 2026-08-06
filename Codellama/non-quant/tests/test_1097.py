import csv
import os

from src_1097 import task_func


def test_task_func():
    text = "This is a test text with $dollar_prefixed_words."
    filename = "test_file.csv"
    expected_output = ["$dollar_prefixed_words"]

    output = task_func(text, filename)

    assert os.path.exists(output)
    with open(output, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        assert header == ["Word"]
        for row in reader:
            assert row[0] in expected_output

    os.remove(output)