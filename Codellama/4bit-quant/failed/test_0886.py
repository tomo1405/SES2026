import pytest
from src_0886 import task_func

def test_task_func_valid_input():
    # Arrange
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    col_a = 'A'
    col_b = 'B'
    col_c = 'C'
    seed = 42

    # Act
    predictions, model = task_func(df, col_a, col_b, col_c, seed)

    # Assert
    assert predictions is not None
    assert model is not None

def test_task_func_invalid_input():
    # Arrange
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    col_a = 'A'
    col_b = 'B'
    col_c = 'C'
    seed = 42

    # Act
    predictions, model = task_func(df, col_a, col_b, col_c, seed)

    # Assert
    assert predictions is None
    assert model is None

def test_task_func_non_numeric_data():
    # Arrange
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    col_a = 'A'
    col_b = 'B'
    col_c = 'C'
    seed = 42

    # Act
    predictions, model = task_func(df, col_a, col_b, col_c, seed)

    # Assert
    assert predictions is None
    assert model is None

def test_task_func_empty_dataframe():
    # Arrange
    df = pd.DataFrame()
    col_a = 'A'
    col_b = 'B'
    col_c = 'C'
    seed = 42

    # Act
    predictions, model = task_func(df, col_a, col_b, col_c, seed)

    # Assert
    assert predictions is None
    assert model is None

def test_task_func_invalid_column_names():
    # Arrange
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]})
    col_a = 'A'
    col_b = 'B'
    col_c = 'C'
    seed = 42

    # Act
    predictions, model = task_func(df, col_a, col_b, col_c, seed)

    # Assert
    assert predictions is None
    assert model is None