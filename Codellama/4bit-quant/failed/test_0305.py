import pytest
from src_0305 import task_func

def test_task_func():
    # Test case 1: Empty dataframe
    df = pd.DataFrame()
    explained_variance_ratio, ax = task_func(df)
    assert explained_variance_ratio == 0
    assert ax is None

    # Test case 2: Non-empty dataframe
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [10, 20, 30]})
    explained_variance_ratio, ax = task_func(df)
    assert explained_variance_ratio == [0.5, 0.3, 0.2]
    assert ax.get_title() == 'Explained Variance Ratio of Principal Components'
    assert ax.get_xlabel() == 'Principal Component'
    assert ax.get_ylabel() == 'Explained Variance Ratio'
    assert len(ax.get_xticks()) == 3
    assert len(ax.get_yticks()) == 3
    assert ax.get_xticks()[0] == 0
    assert ax.get_yticks()[0] == 0
    assert ax.get_xticks()[1] == 1
    assert ax.get_yticks()[1] == 0.5
    assert ax.get_xticks()[2] == 2
    assert ax.get_yticks()[2] == 1