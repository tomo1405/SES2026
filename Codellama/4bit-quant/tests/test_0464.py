import pytest
from src_0464 import task_func

def test_task_func():
    data_str = "1,2,3,4,5"
    data, ax = task_func(data_str)
    assert data.size == 5
    assert ax.get_xlabel() == "Data"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Histogram of Data"

    data_str = "1,2,3,4,5"
    data, ax = task_func(data_str, separator=" ")
    assert data.size == 5
    assert ax.get_xlabel() == "Data"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Histogram of Data"

    data_str = "1,2,3,4,5"
    data, ax = task_func(data_str, bins=10)
    assert data.size == 5
    assert ax.get_xlabel() == "Data"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Histogram of Data"

    data_str = "1,2,3,4,5"
    data, ax = task_func(data_str, separator=" ", bins=10)
    assert data.size == 5
    assert ax.get_xlabel() == "Data"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Histogram of Data"

    data_str = "1,2,3,4,5"
    data, ax = task_func(data_str, bins=10, rwidth=0.5)
    assert data.size == 5
    assert ax.get_xlabel() == "Data"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Histogram of Data"

    data_str = "1,2,3,4,5"
    data, ax = task_func(data_str, separator=" ", bins=10, rwidth=0.5)
    assert data.size == 5
    assert ax.get_xlabel() == "Data"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Histogram of Data"

    data_str = "1,2,3,4,5"
    data, ax = task_func(data_str, bins=10, color="#607c8e")
    assert data.size == 5
    assert ax.get_xlabel() == "Data"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Histogram of Data"

    data_str = "1,2,3,4,5"
    data, ax = task_func(data_str, separator=" ", bins=10, color="#607c8e")
    assert data.size == 5
    assert ax.get_xlabel() == "Data"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Histogram of Data"

    data_str = "1,2,3,4,5"
    data, ax = task_func(data_str, bins=10, rwidth=0.5, color="#607c8e")
    assert data.size == 5
    assert ax.get_xlabel() == "Data"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Histogram of Data"

    data_str = "1,2,3,4,5"
    data, ax = task_func(data_str, separator=" ", bins=10, rwidth=0.5, color="#607c8e")
    assert data.size == 5
    assert ax.get_xlabel() == "Data"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Histogram of Data"