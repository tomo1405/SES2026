import pandas as pd
from src_0702 import task_func


def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target = 'C'
    expected_score = 0.5

    score = task_func(df, target)

    assert score == expected_score