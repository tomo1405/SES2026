python
import random
import string
import pandas as pd
import pytest

def task_func(data_list, seed=0):
    random.seed(seed)

    df = pd.DataFrame(data_list, columns=["Original String"])

    modified_strings = []
    for s in data_list:
        s = s.strip()
        if not s:
            modified_strings.append(s)
            continue
        substrings = [ss.strip() for ss in s.split(",")]
        replace_idx = random.randint(0, len(substrings) - 1)
        random_string = "".join(
            random.choices(string.ascii_lowercase, k=len(substrings[replace_idx]))
        )
        substrings[replace_idx] = random_string
        modified_string = ", ".join(substrings)
        modified_strings.append(modified_string)

    df["Modified String"] = modified_strings

    return df

def test_task_func():
    data_list = [
        "Hello, World!",
        "Python is awesome",
        " ",
        "",
        "1, 2, 3",
        "4, 5, 6",
        "7, 8, 9",
    ]
    expected_df = pd.DataFrame(
        [
            ["Hello, World!", "Hello, World!"],
            ["Python is awesome", "Python is awesome"],
            [" ", " "],
            ["", ""],
            ["1, 2, 3", "1, 2, 3"],
            ["4, 5, 6", "4, 5, 6"],
            ["7, 8, 9", "7, 8, 9"],
        ],
        columns=["Original String", "Modified String"],
    )
    assert task_func(data_list) == expected_df