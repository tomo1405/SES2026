import pandas as pd
import pytest
from src_0481 import task_func


def test_task_func():
    data_list = ["apple, banana, cherry", "orange, grapes, mango"]
    expected_output = pd.DataFrame({"Original String": data_list, "Shuffled String": ["banana, apple, cherry", "orange, mango, grapes"]})
    assert task_func(data_list) == expected_output

def test_task_func_with_seed():
    data_list = ["apple, banana, cherry", "orange, grapes, mango"]
    expected_output = pd.DataFrame({"Original String": data_list, "Shuffled String": ["banana, apple, cherry", "orange, mango, grapes"]})
    assert task_func(data_list, seed=42) == expected_output

def test_task_func_with_invalid_input():
    data_list = ["apple, banana, cherry", "orange, grapes, mango"]
    with pytest.raises(ValueError):
        task_func(data_list, seed="invalid_seed")