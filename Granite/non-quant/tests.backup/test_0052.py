import pytest
from src_0052 import task_func

def test_task_func():
    # Mock the input DataFrame
    df = pd.DataFrame({
        "Age": [25, 30, 35, 40, 45],
        "Height": [160, 170, 180, 190, 200]
    })

    # Test case 1: age > 35 and height < 170
    age = 35
    height = 170
    expected_df = pd.DataFrame({
        "Age": [35, 40, 45],
        "Height": [170, 180, 190],
        "Cluster": [1, 1, 1]
    })
    expected_ax = None
    actual_df, actual_ax = task_func(df, age, height)
    assert actual_df.equals(expected_df) and actual_ax == expected_ax

    # Test case 2: age > 35 and height < 170, but only 2 rows in filtered DataFrame
    df = pd.DataFrame({
        "Age": [35, 40],
        "Height": [170, 180]
    })
    age = 35
    height = 170
    expected_df = pd.DataFrame({
        "Age": [35, 40],
        "Height": [170, 180],
        "Cluster": [0, 0]
    })
    expected_ax = None
    actual_df, actual_ax = task_func(df, age, height)
    assert actual_df.equals(expected_df) and actual_ax == expected_ax

    # Test case 3: age > 50 and height < 170
    age = 50
    height = 170
    expected_df = pd.DataFrame({
        "Age": [],
        "Height": [],
        "Cluster": []
    })
    expected_ax = None
    actual_df, actual_ax = task_func(df, age, height)
    assert actual_df.equals(expected_df) and actual_ax == expected_ax