import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
from unittest.mock import patch

def task_func(input_file):
    with open(input_file, "r") as f:
        data = json.load(f)

    stats = defaultdict(list)
    for d in data:
        for key, value in d.items():
            stats[key].append(value)

    result = {k: {"mean": np.mean(v), "median": np.median(v)} for k, v in stats.items()}

    plots = []
    for key, values in result.items():
        _, ax = plt.subplots()
        ax.bar(["mean", "median"], [values["mean"], values["median"]])
        ax.set_title(f"Statistics of {key}")
        plots.append(ax)
    return result, plots

def test_task_func():
    input_file = "test_data.json"
    with open(input_file, "w") as f:
        json.dump([{"a": 1, "b": 2}, {"a": 3, "b": 4}], f)

    result, plots = task_func(input_file)

    assert isinstance(result, dict)
    for key, values in result.items():
        assert isinstance(key, str)
        assert isinstance(values, dict)
        assert "mean" in values and "median" in values
        assert isinstance(values["mean"], float)
        assert isinstance(values["median"], float)

    assert isinstance(plots, list)
    for ax in plots:
        assert isinstance(ax, plt.Axes)

    plt.savefig("test_plot.png")

if __name__ == "__main__":
    test_task_func()