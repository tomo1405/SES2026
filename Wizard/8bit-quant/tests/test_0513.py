python
import pandas as pd
import numpy as np
import pytest

def task_func(column, data):
    COLUMNS = ["Product", "Quantity Sold", "Total Sales"]
    df = pd.DataFrame(data, columns=COLUMNS)
    if (df["Quantity Sold"] < 0).any() or (df["Total Sales"] < 0).any():
        raise ValueError("Value must not be negative")
    column_data = df[column]

    result = {
        "sum": np.sum(column_data),
        "mean": np.mean(column_data),
        "min": np.min(column_data),
        "max": np.max(column_data),
    }

    ax = df.plot.bar(x="Product", y=column, title=f"Bar Chart of {column}")

    return result, ax

def test_task_func():
    data = [
        ["Product1", 10, 50],
        ["Product2", 20, 100],
        ["Product3", 30, 150],
    ]
    result, ax = task_func("Quantity Sold", data)
    assert result["sum"] == 60
    assert result["mean"] == 20
    assert result["min"] == 10
    assert result["max"] == 30
    assert ax.get_title() == "Bar Chart of Quantity Sold"

    data = [
        ["Product1", -10, 50],
        ["Product2", 20, -100],
        ["Product3", 30, 150],
    ]
    with pytest.raises(ValueError):
        task_func("Quantity Sold", data)