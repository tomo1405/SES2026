python
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytest

from src_0361 import task_func

def test_task_func():
    # Test case 1: file not found
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_file.xlsx", "Sheet1")

    # Test case 2: sheet not found
    with pytest.raises(ValueError):
        task_func("test_data.xlsx", "non_existent_sheet")

    # Test case 3: valid input
    result, fig = task_func("test_data.xlsx", "Sheet1")
    assert isinstance(result, dict)
    assert isinstance(fig, plt.Figure)
    assert len(result) == 3
    assert "A" in result
    assert "B" in result
    assert "C" in result
    assert "mean" in result["A"]
    assert "std" in result["A"]
    assert "mean" in result["B"]
    assert "std" in result["B"]
    assert "mean" in result["C"]
    assert "std" in result["C"]
    assert isinstance(result["A"]["mean"], float)
    assert isinstance(result["A"]["std"], float)
    assert isinstance(result["B"]["mean"], float)
    assert isinstance(result["B"]["std"], float)
    assert isinstance(result["C"]["mean"], float)
    assert isinstance(result["C"]["std"], float)
    assert isinstance(fig, plt.Figure)