import json
import pandas as pd
import numpy as np
from collections import defaultdict
from src_0527 import task_func
def test_task_func():
    input_file = "data.json"
    with open(input_file, "r") as f:
        data = json.load(f)
    df = task_func(input_file)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (len(data), len(data[0]))
    for col in df.columns:
        assert np.all(df[col].isna() | df[col].dtype == np.float64)
def test_task_func_with_missing_data():
    input_file = "data.json"
    with open(input_file, "r") as f:
        data = json.load(f)
    data[0]["key1"] = "value1"
    df = task_func(input_file)
    assert np.all(df["key1"].isna())
def test_task_func_with_non_numeric_data():
    input_file = "data.json"
    with open(input_file, "r") as f:
        data = json.load(f)
    data[0]["key1"] = "value1"
    data[1]["key2"] = "value2"
    df = task_func(input_file)
    assert np.all(df["key1"].isna())
    assert np.all(df["key2"].isna())