import pandas as pd
import random
import re
import pytest
from src_0482 import task_func

def test_task_func():
    data_list = ["apple,banana,orange", "cat,dog,bird", "one,two,three,four"]
    df = task_func(data_list)
    assert isinstance(df, pd.DataFrame)
    assert "Original String" in df.columns
    assert "Randomized String" in df.columns
    for i, row in df.iterrows():
        original_string = row["Original String"]
        randomized_string = row["Randomized String"]
        substrings = re.split("\s*,\s*", original_string)
        random_positions = random.sample(range(len(substrings)), len(substrings))
        expected_randomized_string = ", ".join([substrings[i] for i in random_positions])
        assert randomized_string == expected_randomized_string