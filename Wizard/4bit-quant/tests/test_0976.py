python
import numpy as np
import pandas as pd
import pytest

def task_func(rows, columns=["A", "B", "C", "D", "E"], seed=0) -> pd.DataFrame:
    np.random.seed(seed)
    columns = sorted(list(set(columns)))
    data = np.random.rand(rows, len(columns))
    np.random.shuffle(columns)
    df = pd.DataFrame(data, columns=columns)
    return df

def test_task_func():
    # Test case 1: Test with default arguments
    df = task_func(10)
    assert df.shape == (10, 5)
    assert df.columns.tolist() == ["A", "B", "C", "D", "E"]
    assert df.notna().all().all()

    # Test case 2: Test with custom arguments
    df = task_func(5, columns=["X", "Y", "Z"], seed=42)
    assert df.shape == (5, 3)
    assert df.columns.tolist() == ["X", "Y", "Z"]
    assert df.notna().all().all()

    # Test case 3: Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(-1)
    with pytest.raises(ValueError):
        task_func(10, columns=["A", "B", "C", "D", "E", "F"])
    with pytest.raises(ValueError):
        task_func(10, columns=["A", "B", "C", "D", "E"], seed=-1)