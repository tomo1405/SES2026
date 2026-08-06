import pandas as pd
from src_0599 import task_func


def test_task_func():
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry']})
    letter = 'a'
    expected_count_dict = {'3': 2, '5': 1, '6': 1}

    count_dict = task_func(df, letter)

    assert count_dict == expected_count_dict