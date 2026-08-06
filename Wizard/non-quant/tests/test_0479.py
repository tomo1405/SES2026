python
import pandas as pd
import re
import random
import pytest

def task_func(data_list, seed=None):
    if seed is not None:
        random.seed(seed)

    df = pd.DataFrame([s.strip() for s in data_list], columns=["Original String"])

    modified_strings = []
    for s in data_list:
        substrings = re.split(", ", s)
        random_substring = random.choice(substrings)
        modified_s = (
            s.replace(", " + random_substring, "")
            if ", " + random_substring in s
            else s.replace(random_substring + ", ", "")
        )
        modified_strings.append(modified_s)

    df["Modified String"] = modified_strings

    return df

def test_task_func():
    data_list = ["apple, banana, cherry", "orange, peach, plum", "kiwi, mango, papaya"]
    df = task_func(data_list)
    assert df.shape == (3, 2)
    assert df["Original String"][0] == "apple, banana, cherry"
    assert df["Modified String"][0] == "apple, banana, cherry"
    assert df["Original String"][1] == "orange, peach, plum"
    assert df["Modified String"][1] == "orange, peach, plum"
    assert df["Original String"][2] == "kiwi, mango, papaya"
    assert df["Modified String"][2] == "kiwi, mango, papaya"

    data_list = ["apple, banana, cherry", "orange, peach, plum", "kiwi, mango, papaya"]
    df = task_func(data_list, seed=42)
    assert df.shape == (3, 2)
    assert df["Original String"][0] == "apple, banana, cherry"
    assert df["Modified String"][0] == "apple, banana, cherry"
    assert df["Original String"][1] == "orange, peach, plum"
    assert df["Modified String"][1] == "orange, peach, plum"
    assert df["Original String"][2] == "kiwi, mango, papaya"
    assert df["Modified String"][2] == "kiwi, mango, papaya"