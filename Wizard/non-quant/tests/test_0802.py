python
import collections
import numpy as np
import pytest

def task_func(file_name):
    data = np.genfromtxt(file_name, delimiter=',', names=True,
                         dtype=None, encoding=None)
    common_values = {}

    if len(np.atleast_1d(data)) == 0:
        return {}

    if len(np.atleast_1d(data)) == 1:
        for col in data.dtype.names:
            common_values[col] = data[col].item()

    else:
        for col in data.dtype.names:
            counter = collections.Counter(data[col])
            if counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
                common_values[col] = sorted(counter.items())[0][0]
            else:
                common_values[col] = counter.most_common(1)[0][0]

    return common_values

def test_task_func():
    # Test case 1: Empty input
    assert task_func('') == {}

    # Test case 2: Single row input
    data = '1,2,3\n'
    with open('test.csv', 'w') as f:
        f.write(data)
    assert task_func('test.csv') == {'1': 1, '2': 2, '3': 3}
    import os
    os.remove('test.csv')

    # Test case 3: Multi-row input
    data = '1,2,3\n4,5,6\n7,8,9\n'
    with open('test.csv', 'w') as f:
        f.write(data)
    assert task_func('test.csv') == {'1': 1, '2': 2, '3': 3}
    os.remove('test.csv')

    # Test case 4: Multi-row input with duplicates
    data = '1,2,3\n4,5,6\n7,8,9\n1,2,3\n'
    with open('test.csv', 'w') as f:
        f.write(data)
    assert task_func('test.csv') == {'1': 1, '2': 2, '3': 3}
    os.remove('test.csv')

    # Test case 5: Multi-row input with all duplicates
    data = '1,2,3\n1,2,3\n1,2,3\n'
    with open('test.csv', 'w') as f:
        f.write(data)
    assert task_func('test.csv') == {'1': 1, '2': 2, '3': 3}
    os.remove('test.csv')

    # Test case 6: Multi-row input with mixed types
    data = '1,2,3\n4,5,6\n7,8,9\n1,2,3.5\n'
    with open('test.csv', 'w') as f:
        f.write(data)
    assert task_func('test.csv') == {'1': 1, '2': 2, '3': 3.5}
    os.remove('test.csv')

    # Test case 7: Multi-row input with mixed types and duplicates
    data = '1,2,3\n4,5,6\n7,8,9\n1,2,3.5\n1,2,3\n'
    with open('test.csv', 'w') as f:
        f.write(data)
    assert task_func('test.csv') == {'1': 1, '2': 2, '3': 3.5}
    os.remove('test.csv')