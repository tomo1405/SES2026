import os

import pytest
from src_1096 import task_func


def test_task_func():
    text = "This is a test. It contains $dollar signs and other symbols like % and &."
    output_filename = "test_output.txt"
    expected_output_path = os.path.abspath(output_filename)

    result = task_func(text, output_filename)

    assert result == expected_output_path
    assert os.path.exists(output_filename)

    with open(output_filename, 'r') as file:
        lines = file.readlines()
        assert len(lines) == 1
        assert lines[0].strip() == "$dollar"

    os.remove(output_filename)

if __name__ == "__main__":
    pytest.main()