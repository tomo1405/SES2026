import pytest
from src_1067 import task_func

def test_task_func():
    # Test with default values
    data, outliers, ax = task_func()
    assert len(data) == 100
    assert len(outliers) == 5
    assert ax.get_title() == "Histogram of Data"
    assert ax.get_xlabel() == "Data"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xlim() == (-10, 10)
    assert ax.get_ylim() == (0, 100)

    # Test with custom values
    data, outliers, ax = task_func(num_samples=50, num_outliers=10)
    assert len(data) == 50
    assert len(outliers) == 10
    assert ax.get_title() == "Histogram of Data"
    assert ax.get_xlabel() == "Data"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xlim() == (-10, 10)
    assert ax.get_ylim() == (0, 100)

    # Test with no outliers
    data, outliers, ax = task_func(num_samples=50, num_outliers=0)
    assert len(data) == 50
    assert len(outliers) == 0
    assert ax.get_title() == "Histogram of Data"
    assert ax.get_xlabel() == "Data"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xlim() == (-10, 10)
    assert ax.get_ylim() == (0, 100)

    # Test with no data
    data, outliers, ax = task_func(num_samples=0, num_outliers=5)
    assert len(data) == 0
    assert len(outliers) == 5
    assert ax.get_title() == "Histogram of Data"
    assert ax.get_xlabel() == "Data"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xlim() == (-10, 10)
    assert ax.get_ylim() == (0, 100)