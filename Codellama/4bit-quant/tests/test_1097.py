import csv
import os

from src_1097 import task_func


def test_task_func():
    text = "This is a test text with $dollar-prefixed words."
    filename = "test_output.csv"
    expected_output = ["$dollar-prefixed", "words"]

    result = task_func(text, filename)

    assert result == os.path.abspath(filename)

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        assert header == ["Word"]

        for row in reader:
            assert row[0] in expected_output

    os.remove(filename)