import pandas as pd
import re
import random
from src_0479 import task_func

def test_task_func():
    data_list = ["apple, banana, orange", "grape, melon, watermelon", "lemon, lime, grapefruit"]
    seed = 123
    random.seed(seed)
    df = task_func(data_list, seed)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert df.columns.tolist() == ["Original String", "Modified String"]
    expected_modified_strings = [
        "apple banana orange",
        "grape melon watermelon",
        "lemon lime grapefruit",
    ]
    assert df["Modified String"].tolist() == expected_modified_strings