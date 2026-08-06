import pytest
from src_0702 import task_func

def test_task_func():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    target = 'c'
    expected_score = 0.5

    score = task_func(df, target)

    assert score == expected_score