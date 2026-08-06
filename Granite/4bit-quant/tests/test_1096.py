import os

import pytest
from src_1096 import task_func


def test_task_func():
    text = "This is a test. $word and another $word? $word, $word!"
    output_filename = "test_output.txt"
    expected_output = os.path.abspath(output_filename)

    result = task_func(text, output_filename)

    assert result == expected_output
    assert os.path.exists(output_filename)
    with open(output_filename, 'r') as file:
        lines = file.readlines()
        assert lines == ["word\n", "word\n", "word\n", "word\n"]

    os.remove(output_filename)

if __name__ == "__main__":
    pytest.main()