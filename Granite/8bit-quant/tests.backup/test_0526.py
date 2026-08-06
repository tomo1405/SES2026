import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
from unittest.mock import patch, mock_open, MagicMock

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
    input_file = "input.json"
    data = [{"key1": 1, "key2": 2}, {"key1": 3, "key2": 4}]
    with patch("src_0526.open", mock_open(read_data=json.dumps(data))):
        result, plots = task_func(input_file)
        assert result == {"key1": {"mean": 2.0, "median": 2.0}, "key2": {"mean": 3.0, "median": 3.0}}
        assert len(plots) == 2
        assert isinstance(plots[0], MagicMock)
        assert plots[0].set_title.called