import pandas as pd
from src_0865 import task_func


def test_task_func():
    # Test case 1: empty input
    fruit_data = []
    expected_output = pd.DataFrame()
    assert task_func(fruit_data) == expected_output

    # Test case 2: single fruit
    fruit_data = [('apple', 10)]
    expected_output = pd.DataFrame([[10, 10]], index=['apple'], columns=['Total Count', 'Average Count'])
    assert task_func(fruit_data) == expected_output

    # Test case 3: multiple fruits
    fruit_data = [('apple', 10), ('banana', 20), ('orange', 30)]
    expected_output = pd.DataFrame([[10, 10], [20, 20], [30, 30]], index=['apple', 'banana', 'orange'], columns=['Total Count', 'Average Count'])
    assert task_func(fruit_data) == expected_output

    # Test case 4: duplicate fruits
    fruit_data = [('apple', 10), ('banana', 20), ('orange', 30), ('apple', 10)]
    expected_output = pd.DataFrame([[10, 10], [20, 20], [30, 30]], index=['apple', 'banana', 'orange'], columns=['Total Count', 'Average Count'])
    assert task_func(fruit_data) == expected_output

    # Test case 5: invalid input
    fruit_data = [('apple', 10), ('banana', 20), ('orange', 30), ('apple', 10)]
    expected_output = pd.DataFrame([[10, 10], [20, 20], [30, 30]], index=['apple', 'banana', 'orange'], columns=['Total Count', 'Average Count'])
    assert task_func(fruit_data) == expected_output