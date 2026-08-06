python
import pytest
from src_0052 import task_func

def test_task_func():
    # Test case 1: Valid input, 3 clusters expected
    df = {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200]}
    selected_df, ax = task_func(df, 25, 185)
    assert len(selected_df) == 3
    assert selected_df["Cluster"].tolist() == [0, 1, 1]
    assert ax is not None

    # Test case 2: Valid input, 2 clusters expected
    df = {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200]}
    selected_df, ax = task_func(df, 25, 175)
    assert len(selected_df) == 2
    assert selected_df["Cluster"].tolist() == [0, 0]
    assert ax is not None

    # Test case 3: Valid input, no clusters expected
    df = {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200]}
    selected_df, ax = task_func(df, 50, 150)
    assert len(selected_df) == 0
    assert selected_df["Cluster"].tolist() == []
    assert ax is None

    # Test case 4: Invalid input, age is not an integer
    df = {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200]}
    with pytest.raises(TypeError):
        selected_df, ax = task_func(df, "25", 185)

    # Test case 5: Invalid input, height is not an integer
    df = {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200]}
    with pytest.raises(TypeError):
        selected_df, ax = task_func(df, 25, "185")

    # Test case 6: Invalid input, age is negative
    df = {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200]}
    with pytest.raises(ValueError):
        selected_df, ax = task_func(df, -25, 185)

    # Test case 7: Invalid input, height is negative
    df = {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200]}
    with pytest.raises(ValueError):
        selected_df, ax = task_func(df, 25, -185)

    # Test case 8: Invalid input, age is greater than 100
    df = {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200]}
    with pytest.raises(ValueError):
        selected_df, ax = task_func(df, 120, 185)

    # Test case 9: Invalid input, height is greater than 250
    df = {"Age": [20, 25, 30, 35, 40], "Height": [160, 170, 180, 190, 200]}
    with pytest.raises(ValueError):
        selected_df, ax = task_func(df, 25, 280)