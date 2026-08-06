import pytest
from src_0503 import task_func

def test_task_func():
    # Test with default parameters
    ax, df = task_func()
    assert isinstance(ax, plt.Axes), "Expected ax to be an instance of plt.Axes"
    assert isinstance(df, pd.DataFrame), "Expected df to be a pandas DataFrame"
    assert len(df) > 0, "Expected df to contain data"

    # Test with custom days_in_past
    ax, df = task_func(days_in_past=14)
    assert len(df) > 0, "Expected df to contain data for the specified number of days"

    # Test with invalid days_in_past
    with pytest.raises(ValueError):
        task_func(days_in_past=-1)