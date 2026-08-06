python
import pandas as pd
import random
import re

def task_func(data_list, seed=42):
    random.seed(seed)

    df = pd.DataFrame(data_list, columns=["Original String"])

    randomized_strings = []
    for s in data_list:
        substrings = re.split("\s*,\s*", s)
        random_positions = random.sample(range(len(substrings)), len(substrings))
        randomized_s = ", ".join([substrings[i] for i in random_positions])
        randomized_strings.append(randomized_s)

    df["Randomized String"] = randomized_strings

    return df

def test_task_func():
    data_list = ["apple, banana, cherry", "orange, grape, peach", "kiwi, mango, papaya"]
    df = task_func(data_list)
    assert df.shape == (3, 2)
    assert df["Original String"].tolist() == data_list
    assert df["Randomized String"].tolist() == ["banana, apple, cherry", "grape, orange, peach", "mango, kiwi, papaya"]