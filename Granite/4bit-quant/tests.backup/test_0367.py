import matplotlib.pyplot as plt
import random
import pytest

COLORS = ['#00bfbf', '#000000', '#0000ff']

def task_func(number_list, bins):
    fig, ax = plt.subplots()
    color = random.choice(COLORS)  # Randomly select color from the COLORS constant
    ax.hist(number_list, bins=bins, color=color)
    ax.set_title('Histogram')
    ax.set_xlabel('Number')
    ax.set_ylabel('Frequency')
    return ax

def test_task_func():
    number_list = [random.randint(1, 100) for _ in range(100)]
    bins = 10
    ax = task_func(number_list, bins)
    assert ax is not None
    assert ax.get_title() == 'Histogram'
    assert ax.get_xlabel() == 'Number'
    assert ax.get_ylabel() == 'Frequency'