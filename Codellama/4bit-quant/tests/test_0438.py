import os

import pandas as pd
from src_0438 import task_func


def test_task_func():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    file_name = "test_save.pkl"
    loaded_df = task_func(df, file_name)
    assert loaded_df.equals(df)
    os.remove(file_name)