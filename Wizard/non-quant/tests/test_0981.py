python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pytest

def task_func(df):
    numeric_df = df.select_dtypes(include=[np.number])
    if numeric_df.empty:
        raise ValueError("No numeric columns present")

    correlation = numeric_df.corr()
    fig, ax = plt.subplots()
    sns.heatmap(correlation, ax=ax)

    numeric_cols = numeric_df.columns
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df, fig

def test_task_func():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': ['x', 'y', 'z']})
    with pytest.raises(ValueError):
        task_func(df)

    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    df, fig = task_func(df)
    assert df.shape == (3, 3)
    assert fig is not None