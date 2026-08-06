import pandas as pd
from src_0052 import task_func


def test_task_func():
    # Test case 1: No filtering
    df = pd.DataFrame({"Age": [10, 20, 30, 40, 50], "Height": [150, 160, 170, 180, 190]})
    age = 20
    height = 165
    selected_df, ax = task_func(df, age, height)
    assert selected_df.equals(df)
    assert ax is None

    # Test case 2: Filtering with at least 3 rows
    df = pd.DataFrame({"Age": [10, 20, 30, 40, 50], "Height": [150, 160, 170, 180, 190]})
    age = 20
    height = 165
    selected_df, ax = task_func(df, age, height)
    assert selected_df.equals(df[df["Age"] > age])
    assert ax is not None
    assert ax.get_xlabel() == "Age"
    assert ax.get_ylabel() == "Height"
    assert ax.get_title() == "KMeans Clustering based on Age and Height"

    # Test case 3: Filtering with less than 3 rows
    df = pd.DataFrame({"Age": [10, 20, 30, 40, 50], "Height": [150, 160, 170, 180, 190]})
    age = 20
    height = 165
    selected_df, ax = task_func(df, age, height)
    assert selected_df.equals(df[df["Age"] > age])
    assert ax is None