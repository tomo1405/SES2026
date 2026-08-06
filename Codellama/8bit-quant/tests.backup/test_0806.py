import pytest
from src_0806 import task_func

def test_task_func():
    dictionary = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    item = 5
    seed = 1234
    expected_positions = [(1, 'b'), (2, 'c')]
    expected_length = 2
    expected_df = pd.DataFrame(dictionary)

    positions, length, df = task_func(dictionary, item, seed)

    assert positions == expected_positions
    assert length == expected_length
    assert df.equals(expected_df)