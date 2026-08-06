import json
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import defaultdict
def task_func(input_file: str) -> plt.Axes:
    with open(input_file, "r") as f:
        data = json.load(f)

    stats = defaultdict(list)
    for d in data:
        for key, value in d.items():
            stats[key].append(value)

    results = {
        k: {"mean": np.mean(v), "median": np.median(v)} for k, v in stats.items()
    }

    data = pd.DataFrame(data).melt(var_name="X", value_name="Y")
    ax = sns.boxplot(data=data, x="X", y="Y")
    ax.set_title("Boxplot of Values for Each Key")
    return results, ax
import pytest
def test_task_func():
    input_file = "input.json"
    with open(input_file, "w") as f:
        json.dump([{"key1": 1, "key2": 2}, {"key1": 3, "key2": 4}], f)
    results, ax = task_func(input_file)
    assert isinstance(results, dict)
    assert isinstance(ax, plt.Axes)
    assert "key1" in results
    assert "key2" in results
    assert "mean" in results["key1"]
    assert "median" in results["key1"]
    assert "mean" in results["key2"]
    assert "median" in results["key2"]
    assert isinstance(results["key1"]["mean"], float)
    assert isinstance(results["key1"]["median"], float)
    assert isinstance(results["key2"]["mean"], float)
    assert isinstance(results["key2"]["median"], float)
    assert ax.get_title() == "Boxplot of Values for Each Key"
def test_task_func_with_invalid_input_file():
    input_file = "invalid_input.json"
    with pytest.raises(FileNotFoundError):
        task_func(input_file)