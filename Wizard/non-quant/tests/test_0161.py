python
import pandas as pd
import seaborn as sns
from scipy import stats
import pytest

# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def task_func(data):
    if data.shape[1] != 8:
        raise ValueError("Data must contain exactly eight columns.")
    df = pd.DataFrame(data, columns=COLUMN_NAMES)
    df['Average'] = df.mean(axis=1)

    ax = sns.kdeplot(df['Average'], linewidth=3)

    # Check if there are enough samples for normaltest
    if len(df['Average']) >= 20:
        k2, p = stats.normaltest(df['Average'])
    else:
        p = None

    return df, ax, p

# Test case 1
def test_task_func_valid_data():
    data = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]
    df, ax, p = task_func(data)
    assert df.shape == (2, 9)
    assert ax is not None
    assert p is None

# Test case 2
def test_task_func_invalid_data():
    data = [[1, 2, 3, 4, 5, 6, 7], [9, 10, 11, 12, 13, 14, 15]]
    with pytest.raises(ValueError):
        task_func(data)

# Test case 3
def test_task_func_insufficient_samples():
    data = [[1, 2, 3, 4, 5, 6, 7, 8]]
    df, ax, p = task_func(data)
    assert df.shape == (1, 9)
    assert ax is not None
    assert p is None