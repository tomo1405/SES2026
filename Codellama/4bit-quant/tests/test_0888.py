import pandas as pd
from src_0888 import task_func


def test_task_func():
    T1 = [[1, 2, 3], [4, 5, 6]]
    row_num = 50
    seed = 123
    expected_output = pd.DataFrame(
        [[1, 2, 3], [4, 5, 6]],
        columns=['Col_1', 'Col_2', 'Col_3']
    )
    assert task_func(T1, row_num, seed) == expected_output

def test_task_func_with_different_seed():
    T1 = [[1, 2, 3], [4, 5, 6]]
    row_num = 50
    seed = 456
    expected_output = pd.DataFrame(
        [[1, 2, 3], [4, 5, 6]],
        columns=['Col_1', 'Col_2', 'Col_3']
    )
    assert task_func(T1, row_num, seed) == expected_output

def test_task_func_with_different_row_num():
    T1 = [[1, 2, 3], [4, 5, 6]]
    row_num = 100
    seed = 123
    expected_output = pd.DataFrame(
        [[1, 2, 3], [4, 5, 6]],
        columns=['Col_1', 'Col_2', 'Col_3']
    )
    assert task_func(T1, row_num, seed) == expected_output

def test_task_func_with_different_T1():
    T1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    row_num = 50
    seed = 123
    expected_output = pd.DataFrame(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        columns=['Col_1', 'Col_2', 'Col_3']
    )
    assert task_func(T1, row_num, seed) == expected_output