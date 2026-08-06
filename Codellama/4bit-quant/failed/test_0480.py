import pytest
from src_0480 import task_func

def test_task_func():
    data_list = ["hello, world", "goodbye, world", ""]
    seed = 0
    expected_output = pd.DataFrame(
        {
            "Original String": ["hello, world", "goodbye, world", ""],
            "Modified String": ["hello, world", "goodbye, world", ""],
        }
    )
    output = task_func(data_list, seed)
    assert output.equals(expected_output)

def test_task_func_with_seed():
    data_list = ["hello, world", "goodbye, world", ""]
    seed = 1234
    expected_output = pd.DataFrame(
        {
            "Original String": ["hello, world", "goodbye, world", ""],
            "Modified String": ["hello, world", "goodbye, world", ""],
        }
    )
    output = task_func(data_list, seed)
    assert output.equals(expected_output)

def test_task_func_with_empty_list():
    data_list = []
    seed = 0
    expected_output = pd.DataFrame(
        {
            "Original String": [],
            "Modified String": [],
        }
    )
    output = task_func(data_list, seed)
    assert output.equals(expected_output)

def test_task_func_with_single_element_list():
    data_list = ["hello, world"]
    seed = 0
    expected_output = pd.DataFrame(
        {
            "Original String": ["hello, world"],
            "Modified String": ["hello, world"],
        }
    )
    output = task_func(data_list, seed)
    assert output.equals(expected_output)

def test_task_func_with_multiple_elements_list():
    data_list = ["hello, world", "goodbye, world", ""]
    seed = 0
    expected_output = pd.DataFrame(
        {
            "Original String": ["hello, world", "goodbye, world", ""],
            "Modified String": ["hello, world", "goodbye, world", ""],
        }
    )
    output = task_func(data_list, seed)
    assert output.equals(expected_output)

def test_task_func_with_different_seed():
    data_list = ["hello, world", "goodbye, world", ""]
    seed = 1234
    expected_output = pd.DataFrame(
        {
            "Original String": ["hello, world", "goodbye, world", ""],
            "Modified String": ["hello, world", "goodbye, world", ""],
        }
    )
    output = task_func(data_list, seed)
    assert output.equals(expected_output)