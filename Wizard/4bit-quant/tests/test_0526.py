python
import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
from src_0526 import task_func

def test_task_func():
    input_file = "data.json"
    with open(input_file, "w") as f:
        json.dump([{"a": 1, "b": 2}, {"a": 3, "b": 4}], f)

    result, plots = task_func(input_file)

    assert len(result) == 2
    assert "a" in result
    assert "b" in result
    assert len(result["a"]["mean"]) == 2
    assert len(result["a"]["median"]) == 2
    assert len(result["b"]["mean"]) == 2
    assert len(result["b"]["median"]) == 2

    assert len(plots) == 2
    assert isinstance(plots[0], plt.Axes)
    assert isinstance(plots[1], plt.Axes)