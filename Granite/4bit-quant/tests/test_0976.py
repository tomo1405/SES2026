import pytest
import numpy as np
import pandas as pd

def task_func(rows, columns=["A", "B", "C", "D", "E"], seed=0) -> pd.DataFrame:
    np.random.seed(seed)
    columns = sorted(list(set(columns)))
    data = np.random.rand(rows, len(columns))
    np.random.shuffle(columns)
    df = pd.DataFrame(data, columns=columns)
    return df

def test_task_func():
    # Test case 1: Default arguments
    df = task_func(10)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (10, 5)
    assert set(df.columns) == set(["A", "B", "C", "D", "E"])

    # Test case 2: Custom arguments
    df = task_func(5, columns=["X", "Y", "Z"], seed=42)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 3)
    assert set(df.columns) == set(["X", "Y", "Z"])

if __name__ == "__main__":
    pytest.main()