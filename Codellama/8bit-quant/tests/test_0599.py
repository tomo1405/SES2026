import time

import pandas as pd
from src_0599 import task_func


def test_task_func():
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry']})
    letter = 'a'
    count_dict = task_func(df, letter)
    assert count_dict == {'3': 2, '5': 1, '6': 1}

def test_task_func_time():
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry']})
    letter = 'a'
    start_time = time.time()
    task_func(df, letter)
    end_time = time.time()
    assert end_time - start_time < 1