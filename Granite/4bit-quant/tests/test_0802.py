import collections

import numpy as np
from src_0802 import task_func


def test_task_func():
    file_name = "example.csv"
    data = np.genfromtxt(file_name, delimiter=',', names=True, dtype=None, encoding=None)
    common_values = task_func(file_name)

    assert isinstance(common_values, dict)
    if len(np.atleast_1d(data)) == 0:
        assert len(common_values) == 0
    elif len(np.atleast_1d(data)) == 1:
        for col in data.dtype.names:
            assert common_values[col] == data[col].item()
    else:
        for col in data.dtype.names:
            counter = collections.Counter(data[col])
            if counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
                assert common_values[col] == sorted(counter.items())[0][0]
            else:
                assert common_values[col] == counter.most_common(1)[0][0]