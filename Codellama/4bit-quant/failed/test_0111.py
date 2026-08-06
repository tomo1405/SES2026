import pytest
from src_0111 import task_func

def test_task_func():
    # Test 1: Valid DataFrame with 'Date' and 'Sales' columns
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Sales': [10, 20, 30]})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Daily Turnover'
    assert ax.get_ylabel() == 'Sales'

    # Test 2: Invalid DataFrame with missing 'Date' column
    df = pd.DataFrame({'Sales': [10, 20, 30]})
    with pytest.raises(ValueError):
        task_func(df)

    # Test 3: Invalid DataFrame with missing 'Sales' column
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03']})
    with pytest.raises(ValueError):
        task_func(df)

    # Test 4: Empty DataFrame
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

    # Test 5: DataFrame with no sales
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Sales': [0, 0, 0]})
    with pytest.raises(ValueError):
        task_func(df)