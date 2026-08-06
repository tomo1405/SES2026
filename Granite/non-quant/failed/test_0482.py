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
        assert isinstance(original_string, str)
        assert isinstance(randomized_string, str)
        assert len(randomized_string.split(", ")) == len(original_string.split(", "))