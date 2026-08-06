import pandas as pd
from src_1056 import task_func


def test_task_func():
    colors = ["Red", "Blue", "Green"]
    states = ["CA", "NY", "FL"]
    expected_data = {
        "Color:State 1": ["Red:CA", "Blue:NY", "Green:FL"],
        "Color:State 2": ["Red:NY", "Blue:FL", "Green:CA"],
        "Color:State 3": ["Red:FL", "Blue:CA", "Green:NY"]
    }
    expected_df = pd.DataFrame(expected_data)

    actual_df = task_func(colors, states)

    assert actual_df.equals(expected_df)