import pandas as pd
import itertools
import random
from src_1056 import task_func

def test_task_func():
    colors = ["red", "green", "blue"]
    states = ["ON", "OFF"]
    df = task_func(colors, states)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (len(colors), len(states))
    assert all(df.columns == [f"Color:State {i+1}" for i in range(len(states))])
    assert all(df.index == [f"Color:{color}" for color in colors])
    for i in range(len(colors)):
        for j in range(len(states)):
            assert df.loc[f"Color:{colors[i]}", f"Color:State {j+1}"] == f"{colors[i]}:{states[j]}"