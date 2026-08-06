import pandas as pd
from collections import Counter
from pytest import mark

def task_func(d):
    df = pd.DataFrame(d)
    counts = {}

    for key in ['x', 'y', 'z']:
        if key in df.columns:
            counts[key] = Counter(df[key].dropna().tolist())
        else:
            counts[key] = Counter()

    return counts

@mark.parametrize("d, expected", [
    (
        {'x': [1, 2, 3], 'y': [4, 5, 6], 'z': [7, 8, 9]},
        {'x': Counter({1: 1, 2: 1, 3: 1}), 'y': Counter({4: 1, 5: 1, 6: 1}), 'z': Counter({7: 1, 8: 1, 9: 1})}
    ),
    (
        {'x': [1, 2, 3], 'y': [4, 5, 6]},
        {'x': Counter({1: 1, 2: 1, 3: 1}), 'y': Counter({4: 1, 5: 1, 6: 1}), 'z': Counter()}
    ),
    (
        {'x': [1, 2, 3], 'y': [4, 5, 6], 'z': [7, 8, 9], 'w': [10, 11, 12]},
        {'x': Counter({1: 1, 2: 1, 3: 1}), 'y': Counter({4: 1, 5: 1, 6: 1}), 'z': Counter({7: 1, 8: 1, 9: 1})}
    ),
])
def test_task_func(d, expected):
    assert task_func(d) == expected