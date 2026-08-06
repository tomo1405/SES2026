python
import numpy as np
import pandas as pd
import seaborn as sns
import pytest

# Constants
PLOT_TITLE = "Value Distribution"

def task_func(data_dict):
    df = pd.DataFrame(data_dict).dropna()

    if df.empty or df.nunique().min() < 2:
        return df, None

    min_val, max_val = df.values.min(), df.values.max()
    num_bins = max(min(11, len(df) // 2), 2)
    bin_edges = np.linspace(min_val, max_val, num_bins)

    plot = sns.histplot(df.values.flatten(), bins=bin_edges, kde=False)
    plot.set_title(PLOT_TITLE)

    return df, plot

# Test cases
def test_task_func_empty_df():
    data_dict = {}
    df, plot = task_func(data_dict)
    assert df.empty
    assert plot is None

def test_task_func_single_value_df():
    data_dict = {'col1': [1]}
    df, plot = task_func(data_dict)
    assert df.empty
    assert plot is None

def test_task_func_valid_df():
    data_dict = {'col1': [1, 2, 3, 4, 5]}
    df, plot = task_func(data_dict)
    assert not df.empty
    assert plot is not None

# Run tests
if __name__ == '__main__':
    pytest.main(['-v', __file__])