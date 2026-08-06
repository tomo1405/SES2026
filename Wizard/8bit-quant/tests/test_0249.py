python
import numpy as np
import matplotlib.pyplot as plt
import itertools

def task_func(data_list):
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
    if len(unzipped_data) == 0:
        raise ValueError('Empty data_list')
    
    fig, ax = plt.subplots()
    for i, column in enumerate(unzipped_data[1:], start=1):
        ax.plot(column, label='Position {}'.format(i))
    ax.legend()
    return ax

# Test case 1
data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ax = task_func(data_list)
assert ax.get_xlabel() == 'Position 1'
assert ax.get_ylabel() == 'Position 2'
assert ax.get_zlabel() == 'Position 3'

# Test case 2
data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
ax = task_func(data_list)
assert ax.get_xlabel() == 'Position 1'
assert ax.get_ylabel() == 'Position 2'
assert ax.get_zlabel() == 'Position 3'

# Test case 3
data_list = []
try:
    ax = task_func(data_list)
except ValueError as e:
    assert str(e) == 'Empty data_list'
else:
    assert False, 'Expected ValueError'

# Test case 4
data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, 13]]
ax = task_func(data_list)
assert ax.get_xlabel() == 'Position 1'
assert ax.get_ylabel() == 'Position 2'
assert ax.get_zlabel() == 'Position 3'