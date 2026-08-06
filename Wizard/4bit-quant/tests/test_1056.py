python
import pandas as pd
import itertools
import random

def task_func(colors, states):
    combinations = list(itertools.product(colors, states))
    random.seed(42)
    random.shuffle(combinations)
    num_columns = min(len(colors), len(states))

    data = {
        f"Color:State {i+1}": [
            f"{comb[0]}:{comb[1]}" for comb in combinations[i::num_columns]
        ]
        for i in range(num_columns)
    }
    df = pd.DataFrame(data)

    return df

def test_task_func():
    colors = ["Red", "Green", "Blue"]
    states = ["California", "Texas", "New York"]
    df = task_func(colors, states)
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ["Color:State 1", "Color:State 2", "Color:State 3"]
    assert df.iloc[0, 0] == "Red:California"
    assert df.iloc[1, 1] == "Green:Texas"
    assert df.iloc[2, 2] == "Blue:New York"