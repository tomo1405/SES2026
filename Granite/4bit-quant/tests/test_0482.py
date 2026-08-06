import pandas as pd
import random
import re
from src_0482 import task_func

def test_task_func():
    data_list = ["apple,banana,cherry", "grape,kiwi,orange", "pineapple,watermelon,mango"]
    df = task_func(data_list)
    assert isinstance(df, pd.DataFrame)
    assert "Original String" in df.columns
    assert "Randomized String" in df.columns
    for s in data_list:
        substrings = re.split("\s*,\s*", s)
        random_positions = random.sample(range(len(substrings)), len(substrings))
        randomized_s = ", ".join([substrings[i] for i in random_positions])
        assert randomized_s in df["Randomized String"].values