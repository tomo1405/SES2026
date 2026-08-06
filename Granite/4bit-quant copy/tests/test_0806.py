import pandas as pd
import random
import pytest

from src_0806 import task_func

@pytest.mark.parametrize("dictionary, item, seed, expected_output", [
    ({"A": [1, 2, 3], "B": [4, 5, 6]}, 2, 123, ([(0, 'A'), (0, 'B'), (2, 'A'), (2, 'B')], 8, pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})),
    ({"C": [7, 8, 9], "D": [10, 11, 12]}, 3, 456, ([(0, 'C'), (0, 'D'), (2, 'C'), (2, 'D')], 10, pd.DataFrame({"C": [7, 8, 9], "D": [10, 11, 12]})),
])
def test_task_func(dictionary, item, seed, expected_output):
    random.seed(seed)
    result = task_func(dictionary, item, seed)
    assert result == expected_output