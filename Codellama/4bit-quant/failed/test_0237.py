import pytest
from src_0237 import task_func

def test_task_func_with_valid_input():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [20, 25, 30], 'Score': [80, 90, 70], 'Category': ['A', 'B', 'C']})
    test_size = 0.2
    random_state = 42
    accuracy = task_func(df, test_size, random_state)
    assert isinstance(accuracy, float)
    assert accuracy > 0

def test_task_func_with_invalid_input():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [20, 25, 30], 'Score': [80, 90, 70], 'Category': ['A', 'B', 'C']})
    test_size = 0.2
    random_state = 42
    with pytest.raises(ValueError):
        task_func(df, test_size, random_state, invalid_param=True)