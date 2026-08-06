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

# Test the function
def test_task_func():
    colors = ["Red", "Green", "Blue"]
    states = ["California", "Texas", "New York"]
    expected_df = pd.DataFrame({
        "Color:State 1": ["Red:California", "Green:California", "Blue:California"],
        "Color:State 2": ["Red:Texas", "Green:Texas", "Blue:Texas"],
        "Color:State 3": ["Red:New York", "Green:New York", "Blue:New York"]
    })
    assert task_func(colors, states).equals(expected_df)

test_task_func()