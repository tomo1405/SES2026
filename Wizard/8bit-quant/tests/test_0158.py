python
import numpy as np
import pandas as pd
import seaborn as sns
import pytest

from src_0158 import task_func

def test_task_func():
    # Test with valid input
    data = np.random.rand(10, 5)
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.Grid)
    assert df.shape == (10, 6)
    assert 'Average' in df.columns

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(np.random.rand(10))