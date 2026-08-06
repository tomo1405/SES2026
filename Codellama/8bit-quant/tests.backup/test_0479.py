import pytest
from src_0479 import task_func

def test_task_func_with_seed():
    data_list = ["apple, banana, cherry", "orange, pear, grape"]
    seed = 1234
    expected_output = pd.DataFrame([
        ["apple, banana, cherry", "orange, pear, grape"],
        ["apple, banana, cherry", "orange, pear, grape"]
    ], columns=["Original String", "Modified String"])

    output = task_func(data_list, seed=seed)

    assert output.equals(expected_output)

def test_task_func_without_seed():
    data_list = ["apple, banana, cherry", "orange, pear, grape"]
    expected_output = pd.DataFrame([
        ["apple, banana, cherry", "orange, pear, grape"],
        ["apple, banana, cherry", "orange, pear, grape"]
    ], columns=["Original String", "Modified String"])

    output = task_func(data_list)

    assert output.equals(expected_output)