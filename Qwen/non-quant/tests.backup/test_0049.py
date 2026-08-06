import pytest
from src_0049 import task_func
from datetime import datetime
import os

@pytest.mark.parametrize("n", [0, 1, 5])
def test_task_func_output_length(n):
    timestamps = task_func(n)
    assert len(timestamps) == n

def test_task_func_timestamp_format():
    timestamps = task_func(1)
    assert isinstance(timestamps[0], str)
    assert datetime.strptime(timestamps[0], "%Y-%m-%d %H:%M:%S")

def test_task_func_output_file(tmp_path):
    output_path = tmp_path / "test_output.png"
    task_func(1, output_path=str(output_path))
    assert output_path.exists()

def test_task_func_no_output_file():
    with pytest.raises(AssertionError):
        task_func(1, output_path=None)

def test_task_func_timestamp_order():
    timestamps = task_func(5)
    sorted_timestamps = sorted(timestamps, key=lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
    assert timestamps == sorted_timestamps