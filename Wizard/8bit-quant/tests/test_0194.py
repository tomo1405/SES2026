python
import pandas as pd
import numpy as np
from random import choice
from src_0194 import task_func

# Constants
DATA_TYPES = [str, int, float, list, tuple, dict, set]

def test_task_func():
    # Test case 1
    rows = 10
    columns = 5
    expected_df = pd.DataFrame({
        'col0': [''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), size=5)) for _ in range(rows)],
        'col1': [np.random.choice([int, float], size=rows)],
        'col2': [list(np.random.choice(range(10), size=np.random.randint(1, 6))) for _ in range(rows)],
        'col3': [tuple(np.random.choice(range(10), size=np.random.randint(1, 6))) for _ in range(rows)],
        'col4': [dict(zip(np.random.choice(range(10), size=np.random.randint(1, 6)),
                          np.random.choice(range(10), size=np.random.randint(1, 6)))) for _ in range(rows)],
    })
    actual_df = task_func(rows, columns)
    assert expected_df.equals(actual_df)

    # Test case 2
    rows = 10
    columns = 3
    expected_df = pd.DataFrame({
        'col0': [''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), size=5)) for _ in range(rows)],
        'col1': [np.random.choice([int, float], size=rows)],
        'col2': [set(np.random.choice(range(10), size=np.random.randint(1, 6))) for _ in range(rows)],
    })
    actual_df = task_func(rows, columns)
    assert expected_df.equals(actual_df)