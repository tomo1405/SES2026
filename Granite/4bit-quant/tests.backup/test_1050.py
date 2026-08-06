import re
import pandas as pd
import pytest

def task_func(input_string: str) -> pd.DataFrame:
    input_string = input_string.replace('\\n', '\n').replace('\\t', ' ')
    lines = [line for line in input_string.split("\n") if line.strip()]
    lines = [re.sub("\t", " ", line) for line in lines]
    return pd.DataFrame(lines, columns=["Text"])

def test_task_func():
    input_string = "Hello\tWorld\nPython\t rocks"
    expected_output = pd.DataFrame([["Hello World"], ["Python rocks"]], columns=["Text"])
    actual_output = task_func(input_string)
    assert actual_output.equals(expected_output)

if __name__ == "__main__":
    pytest.main()