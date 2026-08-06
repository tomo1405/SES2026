import pytest
from src_0050 import task_func

def test_task_func():
    # Test case 1: input list of timestamps is empty
    with pytest.raises(ValueError):
        task_func([])

    # Test case 2: input list of timestamps is not empty
    timestamps = [1647225600, 1647225601, 1647225602]
    df, ax = task_func(timestamps)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(df) == len(timestamps)
    assert len(ax.get_xticks()) == len(timestamps)
    plt.close()

if __name__ == "__main__":
    pytest.main()