import pytest
from src_0149 import task_func

def test_task_func():
    df = pd.DataFrame({'A': ['a', 'b', 'c', 'd', 'e'],
                   'B': ['f', 'g', 'h', 'i', 'j']})
    column_name = 'A'
    expected_output = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                               'B': ['f', 'g', 'h', 'i', 'j']})
    output = task_func(df, column_name)
    assert output.equals(expected_output)