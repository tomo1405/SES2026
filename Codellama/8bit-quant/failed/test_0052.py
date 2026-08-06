import pytest
from src_0052 import task_func

def test_task_func_with_valid_input():
    df = pd.DataFrame({"Age": [20, 25, 30, 35, 40], "Height": [170, 180, 190, 195, 200]})
    age = 25
    height = 185
    expected_selected_df = pd.DataFrame({"Age": [25, 30, 35], "Height": [180, 190, 195], "Cluster": [0, 1, 2]})
    expected_ax = None

    selected_df, ax = task_func(df, age, height)

    assert selected_df.equals(expected_selected_df)
    assert ax is expected_ax

def test_task_func_with_invalid_input():
    df = pd.DataFrame({"Age": [20, 25, 30, 35, 40], "Height": [170, 180, 190, 195, 200]})
    age = 25
    height = 185
    expected_selected_df = pd.DataFrame({"Age": [25, 30, 35], "Height": [180, 190, 195], "Cluster": [0, 1, 2]})
    expected_ax = None

    selected_df, ax = task_func(df, age, height)

    assert selected_df.equals(expected_selected_df)
    assert ax is expected_ax