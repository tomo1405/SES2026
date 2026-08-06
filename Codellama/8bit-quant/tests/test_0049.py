import os
import time
from datetime import datetime

from src_0049 import task_func


def test_task_func():
    n = 10
    output_path = "test_output.png"
    timestamps = task_func(n, output_path)
    assert len(timestamps) == n
    assert all(isinstance(t, str) for t in timestamps)
    assert all(t.startswith(datetime.utcfromtimestamp(0).strftime(DATE_FORMAT)) for t in timestamps)
    assert all(t.endswith(datetime.utcfromtimestamp(int(time.time())).strftime(DATE_FORMAT)) for t in timestamps)
    assert plt.hist([datetime.strptime(t, DATE_FORMAT) for t in timestamps])
    if output_path:
        assert os.path.exists(output_path)
    else:
        plt.show()