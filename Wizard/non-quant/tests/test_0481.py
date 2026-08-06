python
import re
import random
import pandas as pd
import pytest

def task_func(data_list, seed=None):
    if seed is not None:
        random.seed(seed)

    df = pd.DataFrame(data_list, columns=["Original String"])

    shuffled_strings = []
    for s in data_list:
        substrings = re.split("\s*,\s*", s)
        random.shuffle(substrings)
        shuffled_s = ", ".join(substrings)
        shuffled_strings.append(shuffled_s)

    df["Shuffled String"] = shuffled_strings

    return df

def test_task_func():
    # Test case 1: Test with seed
    data_list = ["apple, banana, cherry", "orange, peach, plum", "grape, lemon, melon"]
    seed = 123
    expected_df = pd.DataFrame(
        {
            "Original String": ["apple, banana, cherry", "orange, peach, plum", "grape, lemon, melon"],
            "Shuffled String": ["cherry, apple, banana", "plum, peach, orange", "lemon, grape, melon"],
        }
    )
    actual_df = task_func(data_list, seed)
    assert actual_df.equals(expected_df)

    # Test case 2: Test without seed
    data_list = ["apple, banana, cherry", "orange, peach, plum", "grape, lemon, melon"]
    expected_df = pd.DataFrame(
        {
            "Original String": ["apple, banana, cherry", "orange, peach, plum", "grape, lemon, melon"],
            "Shuffled String": ["cherry, apple, banana", "plum, peach, orange", "lemon, grape, melon"],
        }
    )
    actual_df = task_func(data_list)
    assert actual_df.equals(expected_df)

    # Test case 3: Test with empty list
    data_list = []
    expected_df = pd.DataFrame(columns=["Original String", "Shuffled String"])
    actual_df = task_func(data_list)
    assert actual_df.equals(expected_df)

    # Test case 4: Test with None input
    data_list = None
    expected_df = pd.DataFrame(columns=["Original String", "Shuffled String"])
    actual_df = task_func(data_list)
    assert actual_df.equals(expected_df)