import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import zscore
from src_0041 import task_func

def test_task_func():
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected_feature_columns = ["Feature 1", "Feature 2", "Feature 3"]
    expected_df = pd.DataFrame(zscore(data_matrix, axis=1), columns=expected_feature_columns)
    expected_df["Mean"] = expected_df.mean(axis=1)
    expected_correlation_matrix = expected_df.corr()
    expected_ax = sns.heatmap(expected_correlation_matrix, annot=True, fmt=".2f")

    df, ax = task_func(data_matrix)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.Axes)
    assert df.columns.tolist() == expected_feature_columns
    assert df.equals(expected_df)
    assert ax == expected_ax