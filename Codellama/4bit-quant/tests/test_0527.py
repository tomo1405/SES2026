import json

from src_0527 import task_func


def test_task_func():
    input_file = "data.json"
    with open(input_file, "w") as f:
        json.dump([{"a": 1, "b": 2}, {"a": 3, "b": 4}], f)

    df = task_func(input_file)

    assert df.columns.to_list() == ["a", "b"]
    assert df.index.to_list() == ["mean", "median"]
    assert df.loc["mean", "a"] == 2
    assert df.loc["mean", "b"] == 3
    assert df.loc["median", "a"] == 1.5
    assert df.loc["median", "b"] == 2.5