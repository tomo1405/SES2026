python
import pandas as pd
import numpy as np
import pytest

from src_0513 import task_func

def test_task_func():
    data = [
        ["Product A", 10, 100],
        ["Product B", 20, 200],
        ["Product C", 30, 300],
    ]
    column = "Quantity Sold"

    result, ax = task_func(column, data)

    assert result["sum"] == 60
    assert result["mean"] == 20
    assert result["min"] == 10
    assert result["max"] == 30

    assert ax.get_title() == "Bar Chart of Quantity Sold"