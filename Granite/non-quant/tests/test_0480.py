import pandas as pd
from src_0480 import task_func


def test_task_func():
    data_list = ["apple, banana, carrot", "dog, cat, mouse", ""]
    seed = 0
    df = task_func(data_list, seed)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert df.columns.tolist() == ["Original String", "Modified String"]
    expected_modified_strings = [
        "apple, banana, carrot",
        "dog, cat, mouse",
        "",
    ]
    assert df["Modified String"].tolist() == expected_modified_strings