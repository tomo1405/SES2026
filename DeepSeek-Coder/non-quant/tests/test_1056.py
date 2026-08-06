import pytest
from src_1056 import task_func
import pandas as pd
import itertools
import random

def test_task_func():
    colors = ["red", "blue"]
    states = ["NY", "CA"]
    expected_df = pd.DataFrame({
        "Color:State 1": ["red:NY", "blue:NY", "red:CA", "blue:CA"],
        "Color:State 2": ["red:NY", "blue:NY", "red:CA", "blue:CA"]
    })
    
    result_df = task_func(colors, states)
    pd.testing.assert_frame_equal(result_df, expected_df)