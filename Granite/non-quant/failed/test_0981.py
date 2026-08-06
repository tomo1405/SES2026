import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from src_0981 import task_func

def test_task_func():
    df = pd.DataFrame({
        'A': np.random.rand(100),
        'B': np.random.rand(100),
        'C': ['foo', 'bar'] * 50
    })
    expected_df = df.copy()
    expected_df['A'] = StandardScaler().fit_transform(expected_df['A'].values.reshape(-1, 1))
    expected_df['B'] = StandardScaler().fit_transform(expected_df['B'].values.reshape(-1, 1))
    expected_fig, ax = plt.subplots()
    sns.heatmap(expected_df.corr(), ax=ax)

    actual_df, actual_fig = task_func(df)

    assert actual_df.equals(expected_df)
    assert actual_fig == expected_fig

def test_task_func_ raises_error():
    df = pd.DataFrame({
        'A': ['foo', 'bar'] * 50,
        'B': np.random.rand(100),
        'C': np.random.rand(100)
    })

    with pytest.raises(ValueError):
        task_func(df)