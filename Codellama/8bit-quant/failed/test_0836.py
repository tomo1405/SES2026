import pytest
from src_0836 import task_func

def test_task_func_returns_dataframe():
    n_rows = 10
    remove_cols = [0, 2]
    columns = ['A', 'B', 'C', 'D', 'E']
    random_seed = 42

    df = task_func(n_rows, remove_cols, columns, random_seed)

    assert isinstance(df, pd.DataFrame)

def test_task_func_returns_correct_shape():
    n_rows = 10
    remove_cols = [0, 2]
    columns = ['A', 'B', 'C', 'D', 'E']
    random_seed = 42

    df = task_func(n_rows, remove_cols, columns, random_seed)

    assert df.shape == (n_rows, len(columns) - len(remove_cols))

def test_task_func_returns_correct_columns():
    n_rows = 10
    remove_cols = [0, 2]
    columns = ['A', 'B', 'C', 'D', 'E']
    random_seed = 42

    df = task_func(n_rows, remove_cols, columns, random_seed)

    assert list(df.columns) == [columns[i] for i in range(len(columns)) if i not in remove_cols]

def test_task_func_returns_correct_data():
    n_rows = 10
    remove_cols = [0, 2]
    columns = ['A', 'B', 'C', 'D', 'E']
    random_seed = 42

    df = task_func(n_rows, remove_cols, columns, random_seed)

    assert all(df.iloc[:, 0] >= 0) and all(df.iloc[:, 0] <= 100)
    assert all(df.iloc[:, 1] >= 0) and all(df.iloc[:, 1] <= 100)
    assert all(df.iloc[:, 2] >= 0) and all(df.iloc[:, 2] <= 100)
    assert all(df.iloc[:, 3] >= 0) and all(df.iloc[:, 3] <= 100)
    assert all(df.iloc[:, 4] >= 0) and all(df.iloc[:, 4] <= 100)