import pandas as pd
from src_0806 import task_func


def test_task_func():
    dictionary = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    item = 5
    seed = 1234
    expected_positions = [(0, 'b'), (1, 'b')]
    expected_len = 2
    expected_df = pd.DataFrame(dictionary)
    positions, len_positions, df = task_func(dictionary, item, seed)
    assert positions == expected_positions
    assert len_positions == expected_len
    assert df.equals(expected_df)