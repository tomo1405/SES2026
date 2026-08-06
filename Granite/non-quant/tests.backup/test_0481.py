import re
import random
import pandas as pd
from src_0481 import task_func

def test_task_func():
    data_list = ["apple,banana,orange", "cat,dog,bird", "red,green,blue"]
    seed = 123
    df = task_func(data_list, seed)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert df.columns.tolist() == ["Original String", "Shuffled String"]
    expected_shuffled_strings = [
        "apple,banana,orange",
        "cat,dog,bird",
        "blue,green,red",
    ]
    assert df["Shuffled String"].tolist() == expected_shuffled_strings