import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src_0507 import task_func

def test_task_func():
    data = [
        ["2022-01-01", 25, 60, 10, 0.2],
        ["2022-01-02", 28, 58, 12, 0.3],
        ["2022-01-03", 22, 62, 8, 0.1],
        ["2022-01-04", 18, 64, 6, 0.0],
    ]
    df = pd.DataFrame(data, columns=["Date", "Temperature", "Humidity", "Wind Speed", "Precipitation"])

    result = task_func("Temperature", data)

    assert result["sum"] == 113
    assert result["mean"] == 28.25
    assert result["min"] == 18
    assert result["max"] == 28
    assert isinstance(result["plot"], plt.Axes)