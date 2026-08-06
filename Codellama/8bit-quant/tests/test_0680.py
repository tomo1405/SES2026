import pandas as pd
from src_0680 import task_func


def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 3, 4, 5, 6]})
    expected_result = {(1, 2): 1, (2, 3): 1, (3, 4): 1, (4, 5): 1, (5, 6): 1}
    assert task_func(df) == expected_result