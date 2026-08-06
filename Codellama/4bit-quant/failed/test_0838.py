import pytest
from src_0838 import task_func

def test_task_func():
    # Test case 1: n_rows = 10, scale_cols = [0, 2], columns = ['A', 'B', 'C', 'D', 'E']
    n_rows = 10
    scale_cols = [0, 2]
    columns = ['A', 'B', 'C', 'D', 'E']
    df = task_func(n_rows, scale_cols, columns)
    assert df.shape == (n_rows, len(columns))
    assert df.columns.tolist() == columns
    assert df.dtypes.tolist() == ['int64', 'int64', 'float64', 'float64', 'float64']
    assert np.allclose(df.iloc[:, 0], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 1], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 2], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 3], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 4], np.random.randint(0, 100, size=(n_rows, 1)))

    # Test case 2: n_rows = 10, scale_cols = [0, 2], columns = ['A', 'B', 'C', 'D', 'E']
    n_rows = 10
    scale_cols = [0, 2]
    columns = ['A', 'B', 'C', 'D', 'E']
    df = task_func(n_rows, scale_cols, columns)
    assert df.shape == (n_rows, len(columns))
    assert df.columns.tolist() == columns
    assert df.dtypes.tolist() == ['int64', 'int64', 'float64', 'float64', 'float64']
    assert np.allclose(df.iloc[:, 0], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 1], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 2], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 3], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 4], np.random.randint(0, 100, size=(n_rows, 1)))

    # Test case 3: n_rows = 10, scale_cols = [0, 2], columns = ['A', 'B', 'C', 'D', 'E']
    n_rows = 10
    scale_cols = [0, 2]
    columns = ['A', 'B', 'C', 'D', 'E']
    df = task_func(n_rows, scale_cols, columns)
    assert df.shape == (n_rows, len(columns))
    assert df.columns.tolist() == columns
    assert df.dtypes.tolist() == ['int64', 'int64', 'float64', 'float64', 'float64']
    assert np.allclose(df.iloc[:, 0], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 1], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 2], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 3], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 4], np.random.randint(0, 100, size=(n_rows, 1)))

    # Test case 4: n_rows = 10, scale_cols = [0, 2], columns = ['A', 'B', 'C', 'D', 'E']
    n_rows = 10
    scale_cols = [0, 2]
    columns = ['A', 'B', 'C', 'D', 'E']
    df = task_func(n_rows, scale_cols, columns)
    assert df.shape == (n_rows, len(columns))
    assert df.columns.tolist() == columns
    assert df.dtypes.tolist() == ['int64', 'int64', 'float64', 'float64', 'float64']
    assert np.allclose(df.iloc[:, 0], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 1], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 2], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 3], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 4], np.random.randint(0, 100, size=(n_rows, 1)))

    # Test case 5: n_rows = 10, scale_cols = [0, 2], columns = ['A', 'B', 'C', 'D', 'E']
    n_rows = 10
    scale_cols = [0, 2]
    columns = ['A', 'B', 'C', 'D', 'E']
    df = task_func(n_rows, scale_cols, columns)
    assert df.shape == (n_rows, len(columns))
    assert df.columns.tolist() == columns
    assert df.dtypes.tolist() == ['int64', 'int64', 'float64', 'float64', 'float64']
    assert np.allclose(df.iloc[:, 0], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 1], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 2], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 3], np.random.randint(0, 100, size=(n_rows, 1)))
    assert np.allclose(df.iloc[:, 4], np.random.randint(0, 100, size=(n_rows, 1)))