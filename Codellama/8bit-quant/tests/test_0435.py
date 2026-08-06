import pandas as pd
import pytest
from src_0435 import task_func


def test_task_func_valid_input():
    s = "1234567890\n1234567890\n1234567890\n1234567890\n1234567890"
    seed = 0
    expected_output = pd.DataFrame(
        [
            [1, 10, "A", 100, "Apple", "A description"],
            [2, 20, "B", 200, "Banana", "B description"],
            [3, 30, "C", 300, "Orange", "C description"],
            [4, 40, "D", 400, "Pear", "D description"],
            [5, 50, "E", 500, "Grape", "E description"],
        ],
        columns=["ID", "Quantity", "Code", "Price", "Product", "Description"],
    )
    output = task_func(s, seed)
    assert output.equals(expected_output)


def test_task_func_invalid_input():
    s = "1234567890\n1234567890\n1234567890\n1234567890\n1234567890"
    seed = 0
    with pytest.raises(ValueError):
        task_func(s, seed)