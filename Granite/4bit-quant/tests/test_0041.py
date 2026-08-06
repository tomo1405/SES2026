import pandas as pd
import seaborn as sns
from scipy.stats import zscore
import pytest

def task_func(data_matrix):
    z_scores = zscore(data_matrix, axis=1)
    feature_columns = ["Feature " + str(i + 1) for i in range(data_matrix.shape[1])]
    df = pd.DataFrame(z_scores, columns=feature_columns)
    df["Mean"] = df.mean(axis=1)
    correlation_matrix = df.corr()
    ax = sns.heatmap(correlation_matrix, annot=True, fmt=".2f")
    return df, ax

def test_task_func():
    data_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    df, ax = task_func(data_matrix)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.Axes)
    assert df.shape == (3, 4)
    assert df.columns[0] == "Feature 1"
    assert df.columns[1] == "Feature 2"
    assert df.columns[2] == "Feature 3"
    assert df.columns[3] == "Mean"
    assert df["Mean"].mean() == pytest.approx(5)
    correlation_matrix = df.corr()
    assert correlation_matrix.shape == (4, 4)
    assert correlation_matrix.iloc[0, 1] == pytest.approx(1)
    assert correlation_matrix.iloc[1, 2] == pytest.approx(1)
    assert correlation_matrix.iloc[2, 3] == pytest.approx(1)