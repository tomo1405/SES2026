import pandas as pd
from src_0052 import task_func


def test_task_func():
    # Test case 1: Filtered DataFrame has at least 3 rows
    df = pd.DataFrame({"Age": [18, 25, 30, 35, 40], "Height": [170, 180, 190, 175, 160]})
    age = 20
    height = 180
    selected_df, ax = task_func(df, age, height)
    assert len(selected_df) >= 3
    assert selected_df["Cluster"].isin([0, 1, 2]).all()
    assert ax is not None

    # Test case 2: Filtered DataFrame has less than 3 rows
    df = pd.DataFrame({"Age": [18, 25, 30], "Height": [170, 180, 190]})
    age = 20
    height = 180
    selected_df, ax = task_func(df, age, height)
    assert len(selected_df) < 3
    assert selected_df["Cluster"].isin([0]).all()
    assert ax is None

    # Test case 3: KMeans clustering is applied correctly
    df = pd.DataFrame({"Age": [18, 25, 30, 35, 40], "Height": [170, 180, 190, 175, 160]})
    age = 20
    height = 180
    selected_df, ax = task_func(df, age, height)
    assert len(selected_df) >= 3
    assert selected_df["Cluster"].isin([0, 1, 2]).all()
    assert ax is not None
    assert ax.get_xlabel() == "Age"
    assert ax.get_ylabel() == "Height"
    assert ax.get_title() == "KMeans Clustering based on Age and Height"