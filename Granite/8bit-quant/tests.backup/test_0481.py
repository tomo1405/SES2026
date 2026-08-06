import re
import random
import pandas as pd
from src_0481 import task_func

def test_task_func():
    data_list = ["apple, banana, orange", "cat, dog, mouse", "1, 2, 3, 4, 5"]
    seed = 123
    df = task_func(data_list, seed)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert df["Original String"].tolist() == data_list
    shuffled_strings = []
    for s in data_list:
        substrings = re.split("\s*,\s*", s)
        random.seed(seed)
        random.shuffle(substrings)
        shuffled_s = ", ".join(substrings)
        shuffled_strings.append(shuffled_s)
    assert df["Shuffled String"].tolist() == shuffled_strings