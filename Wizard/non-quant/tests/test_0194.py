python
import pandas as pd
import numpy as np
from random import choice

# Constants
DATA_TYPES = [str, int, float, list, tuple, dict, set]

def task_func(rows, columns):
    data = {}
    for col in range(columns):
        data_type = choice(DATA_TYPES)
        if data_type == str:
            data['col' + str(col)] = [''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), size=5)) for _ in
                                      range(rows)]
        elif data_type in [int, float]:
            data['col' + str(col)] = np.random.choice([data_type(i) for i in range(10)], size=rows)
        elif data_type == list:
            data['col' + str(col)] = [list(np.random.choice(range(10), size=np.random.randint(1, 6))) for _ in
                                      range(rows)]
        elif data_type == tuple:
            data['col' + str(col)] = [tuple(np.random.choice(range(10), size=np.random.randint(1, 6))) for _ in
                                      range(rows)]
        elif data_type == dict:
            data['col' + str(col)] = [dict(zip(np.random.choice(range(10), size=np.random.randint(1, 6)),
                                               np.random.choice(range(10), size=np.random.randint(1, 6)))) for _ in
                                      range(rows)]
        elif data_type == set:
            data['col' + str(col)] = [set(np.random.choice(range(10), size=np.random.randint(1, 6))) for _ in
                                      range(rows)]

    df = pd.DataFrame(data)
    return df

# Test the function
def test_task_func():
    # Test case 1
    df = task_func(10, 3)
    assert df.shape == (10, 3)
    assert df.dtypes.tolist() == [object, object, object]

    # Test case 2
    df = task_func(5, 4)
    assert df.shape == (5, 4)
    assert df.dtypes.tolist() == [object, object, object, object]

    # Test case 3
    df = task_func(10, 1)
    assert df.shape == (10, 1)
    assert df.dtypes.tolist() == [object]

    # Test case 4
    df = task_func(10, 0)
    assert df.shape == (10, 0)
    assert df.empty

    # Test case 5
    df = task_func(0, 3)
    assert df.shape == (0, 3)
    assert df.empty

    # Test case 6
    df = task_func(10, -1)
    assert df.shape == (10, 0)
    assert df.empty

    # Test case 7
    df = task_func(-1, 3)
    assert df.shape == (0, 3)
    assert df.empty

    # Test case 8
    df = task_func(10, 10)
    assert df.shape == (10, 10)
    assert df.dtypes.tolist() == [object] * 10

    # Test case 9
    df = task_func(10, 100)
    assert df.shape == (10, 100)
    assert df.dtypes.tolist() == [object] * 100

    # Test case 10
    df = task_func(100, 10)
    assert df.shape == (100, 10)
    assert df.dtypes.tolist() == [object] * 10

    # Test case 11
    df = task_func(1000, 100)
    assert df.shape == (1000, 100)
    assert df.dtypes.tolist() == [object] * 100

    # Test case 12
    df = task_func(10000, 1000)
    assert df.shape == (10000, 1000)
    assert df.dtypes.tolist() == [object] * 1000

test_task_func()