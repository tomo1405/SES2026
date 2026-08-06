import pytest
from src_0885 import task_func

def test_task_func_valid_input():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    columns = ['A', 'B', 'C']
    larger = 50
    equal = 900
    p_value = task_func(df, columns, larger, equal)
    assert p_value > 0.05

def test_task_func_invalid_input_columns():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    columns = ['A', 'B', 'D']
    larger = 50
    equal = 900
    with pytest.raises(ValueError):
        task_func(df, columns, larger, equal)

def test_task_func_invalid_input_larger():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    columns = ['A', 'B', 'C']
    larger = 100
    equal = 900
    with pytest.raises(ValueError):
        task_func(df, columns, larger, equal)

def test_task_func_invalid_input_equal():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    columns = ['A', 'B', 'C']
    larger = 50
    equal = 1000
    with pytest.raises(ValueError):
        task_func(df, columns, larger, equal)

def test_task_func_empty_data():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    columns = ['A', 'B', 'C']
    larger = 50
    equal = 900
    df = df[df['A'] > 100]
    with pytest.raises(ValueError):
        task_func(df, columns, larger, equal)