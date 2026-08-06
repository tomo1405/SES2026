import pytest
from src_0142 import task_func

def test_task_func():
    # Test case 1: rows is a positive integer
    df, stats_dict = task_func(rows=5)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(stats_dict, dict)
    for col in df.columns:
        assert isinstance(stats_dict[col]['mean'], float)
        assert isinstance(stats_dict[col]['median'], float)
    
    # Test case 2: rows is not a positive integer
    with pytest.raises(ValueError):
        task_func(rows=-1)
    
    # Test case 3: rows is not an integer
    with pytest.raises(ValueError):
        task_func(rows=10.5)
    
    # Test case 4: rows is 0
    with pytest.raises(ValueError):
        task_func(rows=0)