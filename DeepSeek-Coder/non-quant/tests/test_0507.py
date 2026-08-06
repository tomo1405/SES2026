import pytest
from src_0507 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    data = {
        "Date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "Temperature": [25, 26, 24],
        "Humidity": [40, 45, 42],
        "Wind Speed": [10, 12, 11],
        "Precipitation": [0, 0, 1]
    }
    COLUMNS = ["Date", "Temperature", "Humidity", "Wind Speed", "Precipitation"]
    df = pd.DataFrame(data, columns=COLUMNS)

    result = task_func("Temperature", data)

    assert result["sum"] == 75
    assert result["mean"] == 25.0
    assert result["min"] == 24
    assert result["max"] == 26
    assert isinstance(result["plot"], plt.Axes)

    plt.close()