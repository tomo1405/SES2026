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

# Test the function
def test_task_func():
    # Test case 1
    timestamps = task_func(10)
    assert len(timestamps) == 10
    assert all(isinstance(t, str) for t in timestamps)

    # Test case 2
    timestamps = task_func(10, output_path='test.png')
    assert len(timestamps) == 10
    assert all(isinstance(t, str) for t in timestamps)
    assert 'test.png' in plt.gcf().canvas.get_supported_filetypes()

    # Test case 3
    timestamps = task_func(0)
    assert len(timestamps) == 0
    assert all(isinstance(t, str) for t in timestamps)

    # Test case 4
    timestamps = task_func(-1)
    assert len(timestamps) == 0
    assert all(isinstance(t, str) for t in timestamps)

    # Test case 5
    timestamps = task_func(1000000)
    assert len(timestamps) == 1000000
    assert all(isinstance(t, str) for t in timestamps)

    # Test case 6
    timestamps = task_func(1000000, output_path='test.png')
    assert len(timestamps) == 1000000
    assert all(isinstance(t, str) for t in timestamps)
    assert 'test.png' in plt.gcf().canvas.get_supported_filetypes()

    # Test case 7
    timestamps = task_func(1000000, output_path='test.pdf')
    assert len(timestamps) == 1000000
    assert all(isinstance(t, str) for t in timestamps)
    assert 'test.pdf' in plt.gcf().canvas.get_supported_filetypes()

    # Test case 8
    timestamps = task_func(1000000, output_path='test.jpg')
    assert len(timestamps) == 1000000
    assert all(isinstance(t, str) for t in timestamps)
    assert 'test.jpg' in plt.gcf().canvas.get_supported_filetypes()

    # Test case 9
    timestamps = task_func(1000000, output_path='test.svg')
    assert len(timestamps) == 1000000
    assert all(isinstance(t, str) for t in timestamps)
    assert 'test.svg' in plt.gcf().canvas.get_supported_filetypes()

    # Test case 10
    timestamps = task_func(1000000, output_path='test.txt')
    assert len(timestamps) == 1000000
    assert all(isinstance(t, str) for t in timestamps)
    assert 'test.txt' not in plt.gcf().canvas.get_supported_filetypes()