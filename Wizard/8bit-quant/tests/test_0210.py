python
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    max_tuple = max(data, key=itemgetter(1))
    tuples = np.array(data)
    x = tuples[:,0]
    y = tuples[:,1]
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Data')
    ax.scatter(*max_tuple, color='red', label='Max Tuple')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Max Tuple Highlighted')
    ax.legend()
    return ax

# Test Cases
def test_task_func():
    data = [(1, 2), (3, 4), (5, 6)]
    ax = task_func(data)
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Max Tuple Highlighted'
    assert ax.get_legend_handles_labels()[0] == [None, 'Max Tuple']
    assert ax.get_legend_handles_labels()[1] == ['Data']
    assert ax.collections[0].get_offsets().data.tolist() == [(1, 2), (3, 4), (5, 6)]
    assert ax.collections[1].get_offsets().data.tolist() == [5, 6]
    assert ax.collections[1].get_facecolors().data.tolist() == [(1.0, 0.0, 0.0, 1.0)]
    assert ax.collections[1].get_edgecolors().data.tolist() == [(1.0, 0.0, 0.0, 1.0)]
    assert ax.collections[1].get_label() == 'Max Tuple'
    plt.close()

test_task_func()