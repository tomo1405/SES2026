import pandas as pd
from src_0865 import task_func


def test_task_func_empty_input():
    assert task_func([]) == pd.DataFrame()

def test_task_func_single_fruit():
    fruit_data = [('apple', 10), ('apple', 20)]
    expected_output = pd.DataFrame({'Total Count': [30], 'Average Count': [15]}, index=['apple'])
    assert task_func(fruit_data) == expected_output

def test_task_func_multiple_fruits():
    fruit_data = [('apple', 10), ('banana', 20), ('orange', 30)]
    expected_output = pd.DataFrame({'Total Count': [10, 20, 30], 'Average Count': [10, 20, 30]}, index=['apple', 'banana', 'orange'])
    assert task_func(fruit_data) == expected_output

def test_task_func_duplicate_fruits():
    fruit_data = [('apple', 10), ('apple', 20), ('orange', 30), ('orange', 40)]
    expected_output = pd.DataFrame({'Total Count': [30, 40], 'Average Count': [15, 30]}, index=['apple', 'orange'])
    assert task_func(fruit_data) == expected_output