import pandas as pd
from src_0142 import task_func


def test_task_func():
    rows = 10
    columns = ['A', 'B', 'C', 'D', 'E', 'F']
    seed = 42

    df, stats_dict = task_func(rows, columns, seed)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(stats_dict, dict)
    assert len(stats_dict) == len(columns)
    assert all(col in stats_dict for col in columns)
    assert all(isinstance(stats_dict[col], dict) for col in columns)
    assert all('mean' in stats_dict[col] for col in columns)
    assert all('median' in stats_dict[col] for col in columns)
    assert all(isinstance(stats_dict[col]['mean'], float) for col in columns)
    assert all(isinstance(stats_dict[col]['median'], float) for col in columns)

    assert df.shape == (rows, len(columns))
    assert all(df[col].dtype == np.int64 for col in columns)
    assert all(df[col].min() >= 1 for col in columns)
    assert all(df[col].max() <= 100 for col in columns)

    assert all(stats_dict[col]['mean'] >= 1 for col in columns)
    assert all(stats_dict[col]['mean'] <= 100 for col in columns)
    assert all(stats_dict[col]['median'] >= 1 for col in columns)
    assert all(stats_dict[col]['median'] <= 100 for col in columns)