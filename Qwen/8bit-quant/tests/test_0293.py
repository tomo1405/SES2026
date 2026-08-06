import pytest
from src_0293 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'id': [1, 1, 2, 2, 3, 3],
        'age': [25, 30, 35, 40, 45, 50],
        'income': [50000, 60000, 70000, 80000, 90000, 100000]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    df_grouped, (hist, bins) = task_func(sample_df)

    # Check if the DataFrame is grouped correctly
    assert df_grouped.shape == (6, 2)
    assert all(df_grouped.index.get_level_values('id').isin([1, 2, 3]))

    # Check if the scaling is correct
    assert df_grouped.loc[1, 'age'].between(0, 1)
    assert df_grouped.loc[1, 'income'].between(0, 1)

    # Check if the histogram has the correct shape
    assert len(hist) == 10
    assert len(bins) == 11

    # Check if the bins are in ascending order
    assert np.all(np.diff(bins) > 0)