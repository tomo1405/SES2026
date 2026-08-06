import pandas as pd
from src_1056 import task_func


def test_task_func():
    colors = ["Red", "Blue", "Green"]
    states = ["CA", "NY", "FL"]
    expected_output = pd.DataFrame({
        "Color:State 1": ["Red:CA", "Blue:NY", "Green:FL"],
        "Color:State 2": ["Red:NY", "Blue:CA", "Green:FL"],
        "Color:State 3": ["Red:FL", "Blue:NY", "Green:CA"]
    })

    output = task_func(colors, states)

    assert output.equals(expected_output)