import pytest
from src_0880 import task_func

def test_empty_dataframe():
    data = pd.DataFrame()
    col1 = "A"
    col2 = "B"
    with pytest.raises(ValueError):
        task_func(data, col1, col2)

def test_non_existent_columns():
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    col1 = "C"
    col2 = "D"
    with pytest.raises(ValueError):
        task_func(data, col1, col2)

def test_non_categorical_data():
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4.0, 5.0, 6.0]})
    col1 = "A"
    col2 = "B"
    with pytest.raises(TypeError):
        task_func(data, col1, col2)

def test_single_category():
    data = pd.DataFrame({"A": [1, 1, 1], "B": [2, 2, 2]})
    col1 = "A"
    col2 = "B"
    with pytest.raises(ValueError):
        task_func(data, col1, col2)

def test_small_counts():
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    col1 = "A"
    col2 = "B"
    with pytest.raises(ValueError):
        task_func(data, col1, col2)

def test_valid_input():
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    col1 = "A"
    col2 = "B"
    p = task_func(data, col1, col2)
    assert p > 0.05