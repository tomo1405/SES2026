import pandas as pd
from src_0154 import task_func


def test_task_func():
    data = ['a', 'b', 'c', 'd', 'e']
    expected_encoded = [0, 1, 2, 3, 4]
    expected_df = pd.DataFrame({'Category': data, 'Encoded': expected_encoded})

    result = task_func(data)

    assert result.equals(expected_df)