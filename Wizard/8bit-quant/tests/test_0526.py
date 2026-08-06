python
import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
import pytest

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
    input_file = "data.json"
    result, plots = task_func(input_file)
    assert len(result) == 2
    assert len(plots) == 2
    assert result["age"]["mean"] == 30.5
    assert result["age"]["median"] == 30.0
    assert result["gender"]["mean"] == 0.5
    assert result["gender"]["median"] == 0.0
    assert isinstance(plots[0], plt.Axes)
    assert isinstance(plots[1], plt.Axes)

if __name__ == "__main__":
    test_task_func()