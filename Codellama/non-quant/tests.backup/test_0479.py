import pytest
from src_0479 import task_func

def test_task_func():
    data_list = ["apple, banana, cherry", "orange, pear, grape"]
    seed = 1234
    expected_output = pd.DataFrame([
        ["apple, banana, cherry", "apple, banana, cherry"],
        ["orange, pear, grape", "orange, pear, grape"]
    ], columns=["Original String", "Modified String"])

    output = task_func(data_list, seed)

    assert output.equals(expected_output)