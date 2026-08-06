import pytest
from src_0701 import task_func

def test_task_func_with_positive_correlation():
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    cols = ['A', 'B', 'C']
    result = task_func(data, cols)
    assert result.loc['A', 'B'] == 1.0
    assert result.loc['B', 'A'] == 1.0

def test_task_func_with_negative_correlation():
    data = [
        [1, 3, 5],
        [2, 2, 4],
        [3, 1, 3]
    ]
    cols = ['A', 'B', 'C']
    result = task_func(data, cols)
    assert result.loc['A', 'B'] == -1.0
    assert result.loc['B', 'A'] == -1.0

def test_task_func_with_no_correlation():
    data = [
        [1, 2, 3],
        [4, 1, 6],
        [7, 8, 1]
    ]
    cols = ['A', 'B', 'C']
    result = task_func(data, cols)
    assert np.isclose(result.loc['A', 'B'], 0.0)
    assert np.isclose(result.loc['B', 'A'], 0.0)

def test_task_func_with_single_column():
    data = [
        [1],
        [2],
        [3]
    ]
    cols = ['A']
    result = task_func(data, cols)
    assert result.loc['A', 'A'] == 1.0

def test_task_func_with_empty_data():
    data = []
    cols = ['A', 'B', 'C']
    result = task_func(data, cols)
    assert result.empty

def test_task_func_with_one_row():
    data = [
        [1, 2, 3]
    ]
    cols = ['A', 'B', 'C']
    result = task_func(data, cols)
    assert result.isnull().values.all()

def test_task_func_with_non_numeric_data():
    data = [
        [1, 'a', 3],
        [4, 'b', 6],
        [7, 'c', 9]
    ]
    cols = ['A', 'B', 'C']
    with pytest.raises(ValueError):
        task_func(data, cols)