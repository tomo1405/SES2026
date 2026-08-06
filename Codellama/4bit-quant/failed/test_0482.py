import pytest
from src_0482 import task_func

def test_task_func():
    data_list = ["apple, banana, cherry", "orange, grapes, mango"]
    expected_output = pd.DataFrame({"Original String": data_list, "Randomized String": ["banana, apple, cherry", "orange, mango, grapes"]})
    output = task_func(data_list)
    assert output.equals(expected_output)

def test_task_func_with_seed():
    data_list = ["apple, banana, cherry", "orange, grapes, mango"]
    expected_output = pd.DataFrame({"Original String": data_list, "Randomized String": ["banana, apple, cherry", "orange, mango, grapes"]})
    output = task_func(data_list, seed=42)
    assert output.equals(expected_output)

def test_task_func_with_different_seed():
    data_list = ["apple, banana, cherry", "orange, grapes, mango"]
    expected_output = pd.DataFrame({"Original String": data_list, "Randomized String": ["banana, apple, cherry", "orange, mango, grapes"]})
    output = task_func(data_list, seed=1337)
    assert output.equals(expected_output)