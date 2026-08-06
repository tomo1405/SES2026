import pytest
from src_1002 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

@pytest.fixture
def sample_csv():
    data = io.StringIO("column1\n1\n2\n3\n4\n5")
    return data

def test_task_func(sample_csv):
    # Mock the pd.read_csv to return a DataFrame with the sample data
    df = pd.read_csv(sample_csv)
    ax = task_func(sample_csv)

    # Check if the DataFrame has the expected columns
    assert "column1" in df.columns
    assert "column1_normalized" in df.columns

    # Check if the normalization is correct
    mean = df["column1"].mean()
    std = df["column1"].std()
    expected_normalized = (df["column1"] - mean) / std
    assert df["column1_normalized"].equals(expected_normalized)

    # Check if the plot title, x-label, and y-label are set correctly
    assert ax.get_title() == "%*s : %*s" % (20, "Plot Title", 20, "Normalized Column 1")
    assert ax.get_xlabel() == "%*s : %*s" % (20, "Index", 20, "Normalized Value")
    assert ax.get_ylabel() == "%*s : %*s" % (20, "Frequency", 20, "Normalized Value")

    # Check if the plot contains the expected data
    lines = ax.get_lines()
    assert len(lines) == 1
    assert lines[0].get_ydata().tolist() == df["column1_normalized"].tolist()

# To run the tests, use the following command in your terminal:
# pytest -v