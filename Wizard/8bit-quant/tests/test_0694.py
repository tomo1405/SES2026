python
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pytest

def task_func(tuples_list, columns):
    df = pd.DataFrame(tuples_list, columns=columns)
    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

    return df_scaled

def test_task_func():
    tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    columns = ['a', 'b', 'c']
    df_scaled = task_func(tuples_list, columns)

    assert df_scaled.shape == (3, 3)
    assert df_scaled.columns.tolist() == ['a', 'b', 'c']
    assert df_scaled.iloc[0].tolist() == [-1.224744871391589, -0.33686029439201355, -0.4472135954999579]
    assert df_scaled.iloc[1].tolist() == [0.0, 0.0, 0.0]
    assert df_scaled.iloc[2].tolist() == [1.2247448713915893, 0.33686029439201367, 0.4472135954999579]