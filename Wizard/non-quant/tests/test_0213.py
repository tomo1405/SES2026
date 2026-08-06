python
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt

def task_func(data):
    max_y_point = max(data, key=itemgetter(1))
    points = np.array(data)
    x = points[:,0]
    y = points[:,1]

    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Points')
    ax.scatter(*max_y_point, color='red', label='Max Y Point')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Points with Max Y Point Highlighted')
    ax.legend()
    return ax, max_y_point

def test_task_func():
    data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    ax, max_y_point = task_func(data)
    assert max_y_point == (7, 8)
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Points with Max Y Point Highlighted'
    assert ax.get_legend_handles_labels()[0] == [ax.collections[0], ax.collections[1]]
    assert ax.get_legend_handles_labels()[1] == ['Points', 'Max Y Point']
    assert ax.collections[0].get_offsets() == [(1, 2), (3, 4), (5, 6), (7, 8)]
    assert ax.collections[1].get_offsets() == [(7, 8)]
    assert ax.collections[1].get_facecolors() == ['#ff0000']
    assert ax.collections[1].get_edgecolors() == ['#ff0000']
    assert ax.collections[1].get_sizes() == [100]
    assert ax.collections[1].get_label() == 'Max Y Point'
    plt.close()

test_task_func()