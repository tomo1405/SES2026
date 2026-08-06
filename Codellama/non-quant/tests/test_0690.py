import pandas as pd
from src_0690 import task_func


def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    p_values = task_func(df)
    assert p_values['A'] > 0.05
    assert p_values['B'] > 0.05