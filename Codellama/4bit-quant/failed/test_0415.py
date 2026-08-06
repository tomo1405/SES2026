import pytest
from src_0415 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Test case 1: No column specified
    data = [1, 2, 3, 4, 5]
    df, ax = task_func(data)
    assert df.equals(pd.DataFrame(data))
    assert ax is None

    # Test case 2: Column specified
    data = [1, 2, 3, 4, 5]
    df, ax = task_func(data, column="c")
    assert df.equals(pd.DataFrame(data))
    assert ax is None

    # Test case 3: No numeric data
    data = [1, 2, 3, 4, 5]
    df, ax = task_func(data, column="c")
    assert df.equals(pd.DataFrame(data))
    assert ax is None

    # Test case 4: Numeric data
    data = [1, 2, 3, 4, 5]
    df, ax = task_func(data, column="c")
    assert df.equals(pd.DataFrame(data))
    assert ax is not None

if __name__ == "__main__":
    pytest.main()