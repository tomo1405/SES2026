import pytest
from src_0041 import task_func
import pandas as pd
import seaborn as sns
from scipy.stats import zscore

def test_task_func():
    data_matrix = pd.DataFrame({"Feature 1": [1, 2, 3], "Feature 2": [4, 5, 6]})
    expected_df = pd.DataFrame({"Feature 1": [1, 2, 3], "Feature 2": [4, 5, 6]})
    expected_ax = sns.heatmap(expected_df.corr(), annot=True, fmt=".2f")
    df, ax = task_func(data_matrix)
    assert df.equals(expected_df)
    assert ax.equals(expected_ax)