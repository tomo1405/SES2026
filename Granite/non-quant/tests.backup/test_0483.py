import pandas as pd
import random
import re
import pytest
from src_0483 import task_func

def test_task_func():
    data_list = ["apple, banana, orange", "cat, dog, mouse", "one, two, three, four"]
    seed = 123
    df = task_func(data_list, seed)
    assert isinstance(df, pd.DataFrame)
    assert "Original String" in df.columns
    assert "Modified String" in df.columns
    assert len(df) == len(data_list)
    for s in data_list:
        substrings = re.split(", ", s)
        operation = random.choice(["remove", "replace", "shuffle", "randomize"])
        if operation == "remove":
            if len(substrings) > 1:
                assert len(df.loc[df["Original String"] == s, "Modified String"].values[0].split(", ")) < len(substrings)
            else:
                assert df.loc[df["Original String"] == s, "Modified String"].values[0] == s
        elif operation == "replace":
            assert "random_string" in df.loc[df["Original String"] == s, "Modified String"].values[0]
        elif operation == "shuffle":
            assert df.loc[df["Original String"] == s, "Modified String"].values[0] != ", ".join(substrings)
        elif operation == "randomize":
            modified_substrings = df.loc[df["Original String"] == s, "Modified String"].values[0].split(", ")
            random_positions = random.sample(range(len(substrings)), len(substrings))
            assert ", ".join([substrings[i] for i in random_positions]) == ", ".join(modified_substrings)