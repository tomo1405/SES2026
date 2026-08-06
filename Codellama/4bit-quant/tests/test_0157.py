import pytest
from src_0157 import task_func

def test_task_func():
    data = [[1, 2, 3, 4, 5, 6, 7, 8],
            [9, 10, 11, 12, 13, 14, 15, 16],
            [17, 18, 19, 20, 21, 22, 23, 24]]
    df, ax = task_func(data)

    assert df.columns.tolist() == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'Average']
    assert df['Average'].tolist() == [10, 11, 12, 13, 14, 15, 16, 17, 18]
    assert ax.get_title() == 'Average'
    assert ax.get_xlabel() == 'Average'
    assert ax.get_ylabel() == 'Average'