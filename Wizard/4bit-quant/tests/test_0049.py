python
import time
from datetime import datetime
import random
import matplotlib.pyplot as plt

# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def task_func(n, output_path=None):
    timestamps = []
    for _ in range(n):
        timestamp = random.randint(0, int(time.time()))
        formatted_time = datetime.utcfromtimestamp(timestamp).strftime(DATE_FORMAT)
        timestamps.append(formatted_time)

    plt.hist([datetime.strptime(t, DATE_FORMAT) for t in timestamps])

    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
    return timestamps

# Test cases
def test_task_func_1():
    timestamps = task_func(10)
    assert len(timestamps) == 10
    assert all(isinstance(t, str) for t in timestamps)

def test_task_func_2():
    timestamps = task_func(10, output_path="test.png")
    assert len(timestamps) == 10
    assert all(isinstance(t, str) for t in timestamps)
    assert "test.png" in plt.gcf().canvas.get_supported_filetypes()

def test_task_func_3():
    timestamps = task_func(10, output_path="test.pdf")
    assert len(timestamps) == 10
    assert all(isinstance(t, str) for t in timestamps)
    assert "test.pdf" in plt.gcf().canvas.get_supported_filetypes()

def test_task_func_4():
    timestamps = task_func(10, output_path="test.jpg")
    assert len(timestamps) == 10
    assert all(isinstance(t, str) for t in timestamps)
    assert "test.jpg" in plt.gcf().canvas.get_supported_filetypes()

def test_task_func_5():
    timestamps = task_func(10, output_path="test.svg")
    assert len(timestamps) == 10
    assert all(isinstance(t, str) for t in timestamps)
    assert "test.svg" in plt.gcf().canvas.get_supported_filetypes()

def test_task_func_6():
    timestamps = task_func(10, output_path="test.gif")
    assert len(timestamps) == 10
    assert all(isinstance(t, str) for t in timestamps)
    assert "test.gif" in plt.gcf().canvas.get_supported_filetypes()

def test_task_func_7():
    timestamps = task_func(10, output_path="test.txt")
    assert len(timestamps) == 10
    assert all(isinstance(t, str) for t in timestamps)
    assert "test.txt" not in plt.gcf().canvas.get_supported_filetypes()