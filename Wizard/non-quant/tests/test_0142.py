python
import pytest
from src_0142 import task_func

def test_task_func():
    # Test valid input
    df, stats_dict = task_func(10)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(stats_dict, dict)
    assert len(df) == 10
    assert len(stats_dict) == 6
    assert all(col in df.columns for col in ['A', 'B', 'C', 'D', 'E', 'F'])
    assert all(col in stats_dict for col in ['A', 'B', 'C', 'D', 'E', 'F'])
    assert all(isinstance(stats_dict[col]['mean'], float) for col in stats_dict)
    assert all(isinstance(stats_dict[col]['median'], float) for col in stats_dict)
    
    # Test invalid input
    with pytest.raises(ValueError):
        task_func(-1)
    with pytest.raises(ValueError):
        task_func(0)
    with pytest.raises(ValueError):
        task_func(10.5)
    with pytest.raises(ValueError):
        task_func('10')