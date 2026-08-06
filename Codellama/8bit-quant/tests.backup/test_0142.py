import pytest
from src_0142 import task_func

def test_task_func():
    rows = 10
    columns = ['A', 'B', 'C', 'D', 'E', 'F']
    seed = 42

    df, stats_dict = task_func(rows, columns, seed)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(stats_dict, dict)
    assert len(stats_dict) == len(columns)
    assert all(col in columns for col in stats_dict.keys())
    assert all(isinstance(stats_dict[col]['mean'], float) for col in columns)
    assert all(isinstance(stats_dict[col]['median'], float) for col in columns)