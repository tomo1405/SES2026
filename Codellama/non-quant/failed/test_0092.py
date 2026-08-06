import pytest
from src_0092 import task_func

def test_task_func():
    data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    column1 = 'A'
    column2 = 'B'

    result, ax = task_func(data, column1, column2)

    assert result[0] == 1.0
    assert result[1] == 0.0
    assert result[2] == 1.0
    assert result[3] == 0.0
    assert result[4] == 0.0

    assert ax.get_xlabel() == 'A'
    assert ax.get_ylabel() == 'B'
    assert ax.get_title() == 'Linear Regression'

    assert len(ax.get_lines()) == 2
    assert ax.get_lines()[0].get_label() == 'original data'
    assert ax.get_lines()[1].get_label() == 'fitted line'